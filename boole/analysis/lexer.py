from boole.analysis.token import *

def advance(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.index += 1
        
        return result
    
    return wrapper

class Lexer:
    def __init__(self) -> None:
        self.index = 0
        self.buffer = ""

    @property
    def hasNextChar(self) -> bool:
        return len(self.buffer) > self.index
    
    @property
    def currentChar(self) -> str:
        return self.buffer[self.index]

    def identifier(self) -> Token:
        identifier = ""

        while self.hasNextChar and self.currentChar.isalpha():
            identifier += self.currentChar
            self.index += 1

        return Token(
            identifier,
            TokenTypes.IDENTIFIER
        )
    
    def assign(self) -> Token:
        assign = self.currentChar
        self.index += 1

        if self.hasNextChar and self.currentChar == "=":
            assign += self.currentChar
            self.index += 1

        if assign != ":=":
            raise MalformedTokenError(
                f"Malformed attribution token: { assign }"
            )
        
        return Token(
            assign,
            TokenTypes.ASSIGN
        )
    
    def implication(self): 
        implication = self.currentChar
        self.index += 1

        if self.hasNextChar and self.currentChar == ">":
            implication += self.currentChar
            self.index += 1

        if implication != "->":
            raise MalformedTokenError(
                f"Malformed attribution token: { implication }"
            )
        
        return Token(
            implication,
            TokenTypes.IMPLICATION
        )
    
    def biimplication(self): 
        biimplication = self.currentChar
        self.index += 1

        if self.hasNextChar and self.currentChar == "-":
            biimplication += self.currentChar
            self.index += 1

        if self.hasNextChar and self.currentChar == ">":
            biimplication += self.currentChar
            self.index += 1

        if biimplication != "<->":
            raise MalformedTokenError(
                f"Malformed attribution token: { biimplication }"
            )
        
        return Token(
            biimplication,
            TokenTypes.IMPLICATION
        )

    @advance
    def out(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.OUT
        )

    @advance
    def bit(self) -> Token:
        return Token(
            self.currentChar == "1",
            TokenTypes.BIT
        )

    @advance
    def _and(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.AND
        )
    
    @advance
    def _or(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.OR
        )
    
    @advance
    def xor(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.XOR
        )
    
    @advance
    def _not(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.NOT
        )

    @advance
    def leftParent(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.LEFT_PARENT
        )
    
    @advance
    def rightParent(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.RIGHT_PARENT
        )
    
    @advance
    def leftBrackets(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.LEFT_BRACKETS
        )
    
    @advance
    def rightBrackets(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.RIGHT_BRACKETS
        )

    @advance
    def comma(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.COMMA
        )
    
    @advance
    def whitespace(self) -> Token:
        return Token(
            self.currentChar,
            TokenTypes.WHITESPACE
        )


    def nextToken(self) -> Token:
        if self.currentChar == ">":
            return self.out()

        if self.currentChar in "01":
            return self.bit()
        
        if self.currentChar == "*":
            return self._and()
        
        if self.currentChar == "+":
            return self._or()
        
        if self.currentChar == "^":
            return self.xor()
        
        if self.currentChar == "!":
            return self._not()
        
        if self.currentChar == "(":
            return self.leftParent()
        
        if self.currentChar == ")":
            return self.rightParent()
        
        if self.currentChar == "[":
            return self.leftBrackets()
        
        if self.currentChar == "]":
            return self.rightBrackets()
        
        if self.currentChar == ",":
            return self.comma()

        if self.currentChar == "-":
            return self.implication()
        
        if self.currentChar == "<":
            return self.biimplication()
        
        if self.currentChar == ":":
            return self.assign()
        
        if self.currentChar.isalpha():
            return self.identifier()

        if self.currentChar.isspace():
            return self.whitespace()

        raise UnrecognizedTokenError(
            f"Unrecognized token: { self.currentChar }"
        )

    def lex(self, buffer: str) -> list[Token]:
        self.buffer = buffer
        self.index = 0

        tokens = []

        while self.hasNextChar:
            token = self.nextToken()

            if token.type == TokenTypes.WHITESPACE:
                continue

            tokens.append(token)

        return tokens
