from boole.analysis.token import Token
from boole.analysis.token import TokenTypes
from boole.analysis.token import TokenError

class Lexer(object):
    def __init__(self) -> None:
        self.text = ""
        self.index = 0
        self.textLen = 0

        self.keyworlds = {
            "bit": Token(
                type = TokenTypes.BIT,
                value = TokenTypes.BIT.name
            )
        }

    def nextToken(self) -> Token:
        currentCharactere = self.text[self.index]

        if currentCharactere in "&*":
            token = Token(
                type = TokenTypes.AND,
                value = TokenTypes.AND.name
            )
            self.index += 1

            return token
        
        if currentCharactere in "|+":
            token = Token(
                type = TokenTypes.OR,
                value = TokenTypes.OR.name
            )
            self.index += 1

            return token
        
        if currentCharactere in "01":
            token = Token(
                type = TokenTypes.LITERALBIT,
                value = currentCharactere == "1"
            )
            self.index += 1

            return token
        
        if currentCharactere in "({[":
            token = Token(
                type = TokenTypes.LEFTBRACKET,
                value = currentCharactere 
            )
            self.index += 1

            return token
        
        if currentCharactere in "]})":
            token = Token(
                type = TokenTypes.RIGHTBRACKET,
                value = currentCharactere 
            )
            self.index += 1

            return token
        
        if currentCharactere == " ":
            token = Token(
                type = TokenTypes.WHITESPACE,
                value = " "
            )
            self.index += 1

            return token

        if currentCharactere in "!~":
            token = Token(
                type = TokenTypes.NOT,
                value = currentCharactere
            )
            self.index += 1

            return token
        
        if currentCharactere == "\n":
            token = Token(
                type = TokenTypes.BREAKLINE,
                value = currentCharactere 
            )
            self.index += 1

            return token
        
        if currentCharactere.isalpha():
            token = self.identifier()

            return token
        
        if currentCharactere in "=":
            token = Token(
                type = TokenTypes.ASSIGN,
                value = currentCharactere
            )
            self.index += 1

            return token

        raise TokenError(f"token '{currentCharactere}' is not valid")

    def identifier(self) -> Token:
        identifier = ""

        while self.textLen > self.index and self.text[self.index].isalpha():
            identifier = identifier + self.text[self.index]
            self.index += 1

        token = self.keyworlds.get(
            identifier,
            Token(
                type = TokenTypes.IDENTIFIER,
                value = identifier
            )
        )

        return token

    def process(self, text) -> list[Token]:
        self.text = text
        self.textLen = len(self.text)
        self.index = 0

        tokens = []

        while self.textLen > self.index:
            token = self.nextToken()

            if token.type == TokenTypes.WHITESPACE:
                continue

            tokens.append(token)

        eof = Token(
            type = TokenTypes.EOF, 
            value = None
        )

        tokens.append(eof)

        return tokens
