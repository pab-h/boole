from boole.analysis.token import Token

from enum import Enum
from enum import auto

class ASTNodeTypes(Enum):
    ABSTRACT = auto()
    BINARYOPERATOR = auto()
    UNARYOPERATOR = auto()
    LOGICLITERAL = auto()
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

class BinaryOperator(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.BINARYOPERATOR
        self.left: AST = None 
        self.right: AST = None 

class UnaryOperator(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.UNARYOPERATOR
        self.expr: AST = None 

class LogicLiteral(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.token = token
        self.type = ASTNodeTypes.LOGICLITERAL
        self.value = token.value

class Compound(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.COMPOUND
        self.statements: list[AST] = []

class Assignment(BinaryOperator):
    def __init__(self, token: Token) -> None:
        super().__init__(token)

        self.type = ASTNodeTypes.ASSIGN

class Variable(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()

        self.type = ASTNodeTypes.VARIABLE
        self.token = token
        self.value = self.token.value

class Type(AST):
    def __init__(self, token: Token) -> None:
        super().__init__()
        self.type == ASTNodeTypes.TYPE
        self.token = token

class VariableDeclaration(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.VARIABLEDECLARATION

        self.variableType: Type = None
        self.assignment: Assignment = None

class NoOperation(AST):
    def __init__(self) -> None:
        super().__init__()

        self.type = ASTNodeTypes.NOOPERATION
