from boole.analysis.ast import AST 
from boole.analysis.ast import BinaryOperator 
from boole.analysis.ast import UnaryOperator
from boole.analysis.ast import Logic 

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

    def factor(self) -> AST:
        # factor: LOGIC('LEFTBRACKET' expr 'RIGHTBRACKET') | 'NOT' factor

        if self.currentToken().type == TokenTypes.LOGIC:
            logicToken = self.currentToken()
            self.eat(TokenTypes.LOGIC)

            return Logic(logicToken)
        
        if self.currentToken().type == TokenTypes.LEFTBRACKET:
            self.eat(TokenTypes.LEFTBRACKET)
            node = self.expr()
            self.eat(TokenTypes.RIGHTBRACKET)

            return node
        
        if self.currentToken().type == TokenTypes.NOT:
            notToken = self.currentToken()
            self.eat(TokenTypes.NOT)

            node = UnaryOperator(notToken)
            node.expr = self.factor()

            return node

        raise ParserError("Unexpected token in factor")
    
    def term(self) -> AST:
        # term: factor{'AND' factor}

        node = self.factor()

        while self.currentToken().type == TokenTypes.AND:
            operator = self.currentToken()
            self.eat(TokenTypes.AND)

            newNode = BinaryOperator(operator)
            newNode.left = node
            newNode.right = self.factor()

            node = newNode

        return node

    def expr(self) -> AST:
        # expr: term{'AND' term}

        node = self.term()

        while self.currentToken().type == TokenTypes.OR:
            operator = self.currentToken()
            self.eat(TokenTypes.OR)

            newNode = BinaryOperator(operator)
            newNode.left = node
            newNode.right = self.term()
            
            node = newNode

        return node
    
    def parse(self, text: str) -> AST:
        self.tokens = self.lexer.process(text)
        self.index = 0

        return self.expr()
