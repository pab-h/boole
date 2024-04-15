from boole.analysis.token import Token

from enum import Enum
from enum import auto

class ASTNodeTypes(Enum):
    ABSTRACT = auto()
    BINARYOPERATOR = auto()
    UNARYOPERATOR = auto()
    LITERALBIT = auto()
    COMPOUND = auto()
    ASSIGN = auto()
    VARIABLE = auto()
    NOOPERATION = auto()
    VARIABLEDECLARATION = auto()
    TYPE = auto()

class AST(object):
    def __init__(self) -> None:
        self.type = ASTNodeTypes.ABSTRACT

    def __repr__(self) -> str:
        return f"AST[type = { self.type.name }]"

class BinaryOperatorNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.BINARYOPERATOR
        self.left: AST = None 
        self.right: AST = None 

class UnaryOperatorNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.UNARYOPERATOR
        self.expr: AST = None 

class LiteralBitNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.LITERALBIT
        self.value = token.value

class CompoundNode(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.COMPOUND
        self.statements: list[AST] = []

class AssignmentNode(BinaryOperatorNode):
    def __init__(self, token: Token) -> None:
        super().__init__(token)

        self.type = ASTNodeTypes.ASSIGN
        self.left: VariableNode = None

class VariableNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.type = ASTNodeTypes.VARIABLE
        self.token = token
        self.value = self.token.value

class TypeNode(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()
        self.type == ASTNodeTypes.TYPE
        self.token = token

class VariableDeclarationNode(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.VARIABLEDECLARATION

        self.variableType: TypeNode = None
        self.assignment: AssignmentNode = None

class NoOperationNode(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.NOOPERATION
