from boole.analysis.token import Token

from enum import Enum
from enum import auto

class ASTTypes(Enum):
    ABSTRACT = auto()

    COMPOUND = auto()
    ASSIGN = auto()
    FUNCTION_DEFINITION = auto()
    FUNCTION_CALL = auto()

    UNARY_OPERATION = auto()
    BINARY_OPERATION = auto()

    BIT = auto()
    STREAM = auto()
    IDENTIFIER = auto()

class AST:
    def __init__(self) -> None:
        self.type = ASTTypes.ABSTRACT

class UnaryOperationNode(AST): 
    def __init__(self, operator: Token, value: AST) -> None:
        super().__init__()

        self.type = ASTTypes.UNARY_OPERATION

        self.operator = operator
        self.value = value

class BinaryOperationNode(AST):
    def __init__(self, operator: Token, left: AST, right: AST) -> None:
        super().__init__()

        self.type = ASTTypes.BINARY_OPERATION

        self.operator = operator
        self.left = left
        self.right = right

class AssignNode(AST):
    def __init__(self, identifier: Token, value: AST) -> None:
        super().__init__()

        self.type = ASTTypes.ASSIGN

        self.identifier = identifier
        self.value = value

class CompoundNode(AST):
    def __init__(self, children: list[AST]) -> None:
        super().__init__()

        self.type = ASTTypes.COMPOUND

        self.children = children

class FunctionDefinitionNode(AST):
    def __init__(self, identifier: Token, params: list[Token], body: AST) -> None:
        super().__init__()

        self.type = ASTTypes.FUNCTION_DEFINITION

        self.identifier = identifier
        self.params = params
        self.body = body

class FunctionCallNode(AST):
    def __init__(self, identifier: Token, arguments: list[AST]) -> None:
        super().__init__()

        self.type = ASTTypes.FUNCTION_CALL

        self.identifier = identifier
        self.arguments = arguments

class BitNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.type = ASTTypes.BIT

        self.token = token

class StreamNode(AST):
    def __init__(self, identifier: Token, bits: list[Token]) -> None:
        super().__init__()

        self.type = ASTTypes.STREAM

        self.identifier = identifier
        self.bits = bits

class IdentifierNode(AST):
    def __init__(self, identifier: Token) -> None:
        super().__init__()

        self.type = ASTTypes.IDENTIFIER
        self.identifier = identifier
