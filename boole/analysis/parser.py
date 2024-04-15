from boole.analysis.ast import *

from boole.analysis.lexer import Lexer

from boole.analysis.token import TokenTypes
from boole.analysis.token import Token

class ParserError(Exception):
    pass

class Parser(object):
    def __init__(self) -> None:
        self.lexer = Lexer()
        self.tokens: list[Token] = []
        self.index = 0

    def currentToken(self) -> Token:
        return self.tokens[self.index]

    def eat(self, tokenType: TokenTypes) -> None:
        if self.currentToken().type != tokenType:
            raise ParserError(f"expected a { tokenType.name } token")
        
        self.index += 1

    def program(self) -> AST:
        return self.statementList()
    
    def statementList(self) -> AST:
        compound = CompoundNode()

        statement = self.statement()
        compound.statements.append(statement)

        while self.currentToken().type == TokenTypes.BREAKLINE:
            self.eat(TokenTypes.BREAKLINE)

            statement = self.statement()
            compound.statements.append(statement)

        if self.currentToken().type == TokenTypes.IDENTIFIER:
            raise ParserError(f"what { self.currentToken().value } is doing here?")
        
        return compound
        
    def statement(self) -> AST:
        if self.currentToken().type == TokenTypes.BIT:
            return self.declarationStatement()

        if self.currentToken().type == TokenTypes.IDENTIFIER:
            return self.assignmentStatement()
        
        return self.empty()
    
    def type(self) -> AST:
        type = TypeNode(self.currentToken())
        
        if type.token.type == TokenTypes.BIT:
            self.eat(TokenTypes.BIT)

        return type

    def declarationStatement(self) -> AST:
        declaration = VariableDeclarationNode()

        declaration.variableType = self.type()
        declaration.assignment = self.assignmentStatement() 

        return declaration

    def assignmentStatement(self) -> AST:
        variable = self.variable()

        assignment = AssignmentNode(self.currentToken())
        self.eat(TokenTypes.ASSIGN)

        expression = self.expr() 

        assignment.left = variable
        assignment.right = expression

        return assignment

    def variable(self) -> AST:
        variable = VariableNode(self.currentToken())
        self.eat(TokenTypes.IDENTIFIER)

        return variable

    def empty(self) -> AST:
        return NoOperationNode()

    def factor(self) -> AST:

        if self.currentToken().type == TokenTypes.LITERALBIT:
            logicToken = self.currentToken()
            self.eat(TokenTypes.LITERALBIT)

            return LiteralBitNode(logicToken)
        
        if self.currentToken().type == TokenTypes.LEFTBRACKET:
            self.eat(TokenTypes.LEFTBRACKET)
            node = self.expr()
            self.eat(TokenTypes.RIGHTBRACKET)

            return node
        
        if self.currentToken().type == TokenTypes.NOT:
            notToken = self.currentToken()
            self.eat(TokenTypes.NOT)

            node = UnaryOperatorNode(notToken)
            node.expr = self.factor()

            return node

        return self.variable()
    
    def term(self) -> AST:

        node = self.factor()

        while self.currentToken().type == TokenTypes.AND:
            operator = self.currentToken()
            self.eat(TokenTypes.AND)

            newNode = BinaryOperatorNode(operator)
            newNode.left = node
            newNode.right = self.factor()

            node = newNode

        return node

    def expr(self) -> AST:

        node = self.term()

        while self.currentToken().type == TokenTypes.OR:
            operator = self.currentToken()
            self.eat(TokenTypes.OR)

            newNode = BinaryOperatorNode(operator)
            newNode.left = node
            newNode.right = self.term()
            
            node = newNode

        return node
    
    def parse(self, text: str) -> AST:
        self.tokens = self.lexer.process(text)
        self.index = 0

        program = self.program()

        if self.currentToken().type != TokenTypes.EOF:
            raise ParserError(f"The program is bad formated. Not expect { self.currentToken() } token")

        return program
