from boole.analysis.token import *
from boole.analysis.ast import *

class Parser:
    def __init__(self) -> None:
        self.index = 0
        self.stream: list[Token] = []

    @property
    def currentToken(self) -> Token:
        return self.stream[self.index]
    
    @property
    def nextToken(self) -> Token:
        return self.stream[self.index + 1]
    
    @property
    def hasNextToken(self) -> bool:
        return len(self.stream) > self.index
    
    def eat(self, tokenType: TokenTypes):
        token = self.currentToken

        if token.type == tokenType:
            self.index += 1
            return
        
        raise SyntaxError(f"Unexpected Token { token.value }")

    def factor(self) -> AST:
        if self.currentToken.type == TokenTypes.IDENTIFIER:
            if self.hasNextToken and self.nextToken.type == TokenTypes.LEFT_PARENT:
                return self.functionCall()
            
            identifier = self.currentToken
            self.eat(TokenTypes.IDENTIFIER)

            return IdentifierNode(identifier)

        if self.currentToken.type == TokenTypes.BIT:
            bitToken = self.currentToken
            self.eat(TokenTypes.BIT)

            return BitNode(bitToken)
        
        if self.currentToken.type == TokenTypes.LEFT_PARENT:
            self.eat(TokenTypes.LEFT_PARENT)
            expression = self.expression()
            self.eat(TokenTypes.RIGHT_PARENT)

            return expression
        
        if self.currentToken.type == TokenTypes.NOT:
            notOperator = self.currentToken
            self.eat(TokenTypes.NOT)

            return UnaryOperationNode(
                notOperator,
                self.factor()
            )

    def term(self) -> AST:
        node = self.factor()

        while self.currentToken.type in [
            TokenTypes.AND, 
            TokenTypes.XOR
        ]:
            operator = self.currentToken
            self.eat(operator.type)

            node = BinaryOperationNode(
                operator,
                node,
                self.factor()
            )
        
        return node

    def expression(self) -> AST:
        node = self.term()

        while self.currentToken.type in [
            TokenTypes.OR, 
            TokenTypes.IMPLICATION, 
            TokenTypes.BIIMPLICATION
        ]:
            operator = self.currentToken
            self.eat(operator.type)

            node = BinaryOperationNode(
                operator,
                node,
                self.term()
            )
        
        return node

    def functionDefinition(self) -> FunctionDefinitionNode:
        self.eat(TokenTypes.FN)

        identifier = self.currentToken
        self.eat(TokenTypes.IDENTIFIER)
        
        self.eat(TokenTypes.LEFT_PARENT)

        params = []

        while self.currentToken.type != TokenTypes.RIGHT_PARENT:
            param = self.currentToken
            self.eat(TokenTypes.IDENTIFIER)
            
            if self.currentToken.type == TokenTypes.COMMA:
                self.eat(TokenTypes.COMMA)

            params.append(param)

        self.eat(TokenTypes.RIGHT_PARENT) 

        self.eat(TokenTypes.ASSIGN)

        functionDefinition = FunctionDefinitionNode(
            identifier,
            params,
            self.expression()
        ) 
        self.eat(TokenTypes.BREAKLINE)

        return functionDefinition

    def functionCall(self) -> FunctionCallNode:
        identifier = self.currentToken
        self.eat(TokenTypes.IDENTIFIER)
        
        self.eat(TokenTypes.LEFT_PARENT)

        params = []

        while self.currentToken.type != TokenTypes.RIGHT_PARENT:
            param = self.expression()
            
            if self.currentToken.type == TokenTypes.COMMA:
                self.eat(TokenTypes.COMMA)

            params.append(param)

        self.eat(TokenTypes.RIGHT_PARENT) 

        functionCall = FunctionCallNode(
            identifier,
            params
        ) 

        return functionCall

    def _stream(self) -> StreamNode:
        identifier = self.currentToken
        self.eat(TokenTypes.IDENTIFIER)
        
        self.eat(TokenTypes.LEFT_BRACKET)
        self.eat(TokenTypes.RIGHT_BRACKET)
        self.eat(TokenTypes.ASSIGN)

        self.eat(TokenTypes.LEFT_BRACKET)

        bits = []

        while self.currentToken.type != TokenTypes.RIGHT_BRACKET:
            bit = self.currentToken
            self.eat(TokenTypes.BIT)

            if self.currentToken.type == TokenTypes.COMMA:
                self.eat(TokenTypes.COMMA)

            bits.append(bit)

        self.eat(TokenTypes.RIGHT_BRACKET)

        stream = StreamNode(
            identifier, 
            bits
        )
        self.eat(TokenTypes.BREAKLINE)

        return stream

    def assign(self) -> AssignNode:
        identifier = self.currentToken
        self.eat(TokenTypes.IDENTIFIER)

        self.eat(TokenTypes.ASSIGN)
        
        assign = AssignNode(
            identifier, 
            self.expression()
        )

        return assign

    def statement(self) -> AST:
        if self.currentToken.type == TokenTypes.FN:
            return self.functionDefinition()

        if self.currentToken.type == TokenTypes.IDENTIFIER:

            if self.hasNextToken and self.nextToken.type == TokenTypes.LEFT_BRACKET:
                return self._stream()

            if self.hasNextToken and self.nextToken.type == TokenTypes.ASSIGN:
                return self.assign()

            return self.expression()

        return self.expression()

    def cleanBreaklines(self):
        while self.currentToken.type == TokenTypes.BREAKLINE:
            self.eat(TokenTypes.BREAKLINE)

    def program(self) -> CompoundNode:
        self.cleanBreaklines()

        statements = []

        while self.currentToken.type != TokenTypes.EOF:
            outOperator = None

            if self.currentToken.type == TokenTypes.OUT:
                outOperator = self.currentToken
                self.eat(TokenTypes.OUT)

            statement = self.statement()

            if outOperator:
                statement = UnaryOperationNode(
                    outOperator,
                    statement
                )

            statements.append(statement)

            self.cleanBreaklines()

        return CompoundNode(
            statements
        )

    def parse(self, stream: list[Token]) -> CompoundNode:
        self.index = 0
        self.stream = stream

        program = self.program()

        if self.currentToken.type != TokenTypes.EOF:
            raise SyntaxError(
                f"Not expect {self.currentToken} token"
            )

        return program