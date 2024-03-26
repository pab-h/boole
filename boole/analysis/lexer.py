from boole.analysis.token import Token
from boole.analysis.token import TokenTypes
from boole.analysis.token import TokenError

class Lexer(object):
    def createToken(self, charactere: str) -> Token:
        if charactere in "&*":
            return Token(
                type = TokenTypes.AND,
                value = TokenTypes.AND.name
            )
        
        if charactere in "|+":
            return Token(
                type = TokenTypes.OR,
                value = TokenTypes.OR.name
            )
        
        if charactere in "01":
            return Token(
                type = TokenTypes.LOGIC,
                value = charactere == "1"
            )
        
        raise TokenError(f"token '{charactere}' is not valid")

    def process(self, text) -> list[Token]:
        tokens = []

        for charactere in text: 
            token = self.createToken(charactere)
            tokens.append(token)

        eof = Token(
            type = TokenTypes.EOF, 
            value = None
        )

        tokens.append(eof)

        return tokens
