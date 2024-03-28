from boole.analysis.token import Token

from typing import Optional

class AST(object):
    def __init__(self, value: Token) -> None:
        self.value = value
        self.left: Optional[Token] = None
        self.right: Optional[Token] = None
