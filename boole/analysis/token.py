from typing import Union

from enum import Enum
from enum import auto

class TokenError(Exception):
    pass

class TokenTypes(Enum):
    EOF = auto()
    AND = auto()
    OR = auto()
    LOGIC = auto()
    LEFTBRACKET = auto()
    RIGHTBRACKET = auto()
    WHITESPACE = auto()

class Token(object): 
    def __init__(self, type: TokenTypes, value: Union[str, bool, None]) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        return f"Token[{ self.type.name }, { self.value }]"

    def __eq__(self, otherToken: 'Token') -> bool:
        return self.type == otherToken.type and\
            self.value == otherToken.value

