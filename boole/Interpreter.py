from boole.analysis.parser import Parser

from boole.analysis.ast import AST
from boole.analysis.ast import BinaryOperator
from boole.analysis.ast import UnaryOperator
from boole.analysis.ast import Logic
from boole.analysis.ast import ASTNodeTypes

from boole.analysis.token import TokenTypes

class InterpreterError(Exception):
    pass

class Interpreter(object):
    def __init__(self) -> None:
        self.parser = Parser()

    def visitUnaryOperator(self, node: UnaryOperator) -> bool:
        if node.token.type == TokenTypes.NOT:
            return not self.visit(node.expr)
        
        raise InterpreterError("invalid unary operator")

    def visitBinaryOperator(self, node: BinaryOperator) -> bool:
        token = node.token

        if token.type == TokenTypes.AND:
            return self.visit(node.left) and self.visit(node.right)
        
        if token.type == TokenTypes.OR:
            return self.visit(node.left) or self.visit(node.right)
        
        raise InterpreterError("invalid binary operator")

    def visitLogic(self, node: Logic) -> bool:
        return node.value

    def visit(self, node: AST) -> bool:

        if node.type == ASTNodeTypes.UNARYOPERATOR:
            return self.visitUnaryOperator(node)

        if node.type == ASTNodeTypes.BINARYOPERATOR:
            return self.visitBinaryOperator(node)
        
        if node.type == ASTNodeTypes.LOGIC:
            return self.visitLogic(node)

        raise InterpreterError("Invalid AST node")

    def eval(self, text): 
        ast = self.parser.parse(text)

        return self.visit(ast)
