from boole.analysis.parser import Parser
from boole.analysis.ast import *
from boole.analysis.token import TokenTypes
from boole.analysis.symbolTable import SymbolTable
from boole.analysis.symbolTable import SymbolTableBuilder

from typing import Optional

class InterpreterError(Exception):
    pass

class Interpreter(object):
    def __init__(self) -> None:
        self.parser = Parser()
        self.variables: dict[str, bool] = {}
        self.symbolTableBuilder = SymbolTableBuilder()
        self.symbolTable: SymbolTable = None 

    def visitUnaryOperator(self, node: UnaryOperatorNode) -> bool:
        if node.token.type == TokenTypes.NOT:
            return not self.visit(node.expr)
        
        raise InterpreterError("invalid unary operator")

    def visitBinaryOperator(self, node: BinaryOperatorNode) -> bool:
        token = node.token

        if token.type == TokenTypes.AND:
            return self.visit(node.left) and self.visit(node.right)
        
        if token.type == TokenTypes.OR:
            return self.visit(node.left) or self.visit(node.right)
        
        raise InterpreterError("invalid binary operator")

    def visitLiteralBit(self, node: LiteralBitNode) -> bool:
        return node.value

    def visitCompound(self, node: CompoundNode) -> None:
        for statement in node.statements:
            self.visit(statement)

    def visitNoOperation(self, node: NoOperationNode) -> None:
        return None

    def visitAssign(self, node: AssignmentNode) -> None:
        variableName = node.left.value
        variableSymbol = self.symbolTable.lookup(variableName)

        if not variableSymbol:
             raise InterpreterError(f"{ variableName } not declared")

        self.variables.update({
            variableName: self.visit(node.right)
        })

    def visitVariable(self, node: VariableNode) -> bool:
        return self.variables.get(node.value)

    def visitType(self, node: TypeNode) -> None:
        pass

    def visitVariableDeclaration(self, node: VariableDeclarationNode) -> None:
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
        
        if node.type == ASTNodeTypes.LITERALBIT:
            return self.visitLiteralBit(node)

        raise InterpreterError("Invalid AST node")

    def eval(self, text): 
        ast = self.parser.parse(text)
        self.symbolTable = self.symbolTableBuilder.build(ast)

        return self.visit(ast)
