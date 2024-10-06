from enum import Enum
from enum import auto

class UnrecognizedTokenError(Exception):
    pass

class MalformedTokenError(Exception):
    pass

class TokenTypes(Enum):
    BIT = auto()
    IDENTIFIER = auto()

    OR = auto()
    AND = auto()
    NOT = auto()
    XOR = auto()
    IMPLICATION = auto()
    BIIMPLICATION = auto()
    
    LEFT_PARENT = auto()
    RIGHT_PARENT = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    
    ASSIGN = auto()
    COMMA = auto()
    
    FN = auto()
    OUT = auto()

    WHITESPACE = auto()
    BREAKLINE = auto()
    EOF = auto()

class Token:
    def __init__(self, value, _type: TokenTypes) -> None:
        self.value = value
        self.type = _type

    def __repr__(self) -> str:
        return f"Token[value = \"{self.value}\", type = {self.type.name}]"
