from boole.analysis.parser import Parser

from boole.analysis.ast import *

from boole.analysis.token import TokenTypes

from typing import Optional

class InterpreterError(Exception):
    pass

class Interpreter(object):
    def __init__(self) -> None:
        self.parser = Parser()
        self.variables: dict[str, bool] = {}

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

    def visitLogic(self, node: LogicLiteral) -> bool:
        return node.value

    def visitCompound(self, node: Compound) -> None:
        for statement in node.statements:
            self.visit(statement)

    def visitNoOperation(self, node: NoOperation) -> None:
        return None

    def visitAssign(self, node: Assignment) -> None:
        variableName = node.left.value

        self.variables.update({
            variableName: self.visit(node.right)
        })

    def visitVariable(self, node: Variable) -> Optional[None]:
        variableName = node.value
        variableValue = self.variables.get(variableName)

        if variableValue == None:
            raise InterpreterError(f"variable { variableName } not found")

        return variableValue

    def visitType(self, node: Type) -> None:
        pass

    def visitVariableDeclaration(self, node: VariableDeclaration) -> None:
        return self.visit(node.assignment)

    def visit(self, node: AST) -> Optional[bool]:
        if node.type == ASTNodeTypes.VARIABLEDECLARATION:
            return self.visitVariableDeclaration(node)

        if node.type == ASTNodeTypes.TYPE:
            return self.visitType(node)

        if node.type == ASTNodeTypes.NOOPERATION:
            return self.visitNoOperation(node)

        if node.type == ASTNodeTypes.VARIABLE:
            return self.visitVariable(node)

        if node.type == ASTNodeTypes.ASSIGN:
            return self.visitAssign(node)

        if node.type == ASTNodeTypes.COMPOUND:
            return self.visitCompound(node)

        if node.type == ASTNodeTypes.UNARYOPERATOR:
            return self.visitUnaryOperator(node)

        if node.type == ASTNodeTypes.BINARYOPERATOR:
            return self.visitBinaryOperator(node)
        
        if node.type == ASTNodeTypes.LOGICLITERAL:
            return self.visitLogic(node)

        raise InterpreterError("Invalid AST node")

    def eval(self, text): 
        ast = self.parser.parse(text)

        return self.visit(ast)
