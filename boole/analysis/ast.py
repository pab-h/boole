from boole.analysis.token import Token

from enum import Enum
from enum import auto

from typing import Optional

class ASTNodeTypes(Enum):
    ABSTRACT = auto()
    BINARYOPERATOR = auto()
    LOGIC = auto()

class AST(object):
    def __init__(self, token: Token) -> None:
        self.token = token
        self.type = ASTNodeTypes.ABSTRACT

    def __repr__(self) -> str:
        return f"AST[token = { self.token }, type = { self.type.name }]"

class BinaryOperator(AST):
    def __init__(self, token: Token) -> None:
        super().__init__(token)
        self.type = ASTNodeTypes.BINARYOPERATOR
        self.left: Optional[AST] = None 
        self.right: Optional[AST] = None 

class Logic(AST):
    def __init__(self, token: Token) -> None:
        super().__init__(token)
        self.type = ASTNodeTypes.LOGIC
        self.value = token.value
