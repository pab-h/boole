from boole.analysis.ast import *
from boole.analysis.token import TokenTypes

class Translator:
    def visitBit(self, node: BitNode) -> str:
        return str(node.token.value)

    def visitAssign(self, node: AssignNode) -> str:
        identifier = node.identifier.value

        return f"{identifier} = {self.visit(node.value)}" 

    def visitBinaryOperation(self, node: BinaryOperationNode) -> str:
        operator = node.operator

        if operator.type == TokenTypes.IMPLICATION:
            return f"implication({self.visit(node.left)}, {self.visit(node.right)})"

        if operator.type == TokenTypes.BIIMPLICATION:
            return f"biimplication({self.visit(node.left)}, {self.visit(node.right)})"

        return self.visit(node.left) + \
                f" {operator.value} " + \
                self.visit(node.right)

    def visitCompound(self, node: CompoundNode) -> str:
        result = ""

        for child in node.children:
            result += self.visit(child) + "\n"

        return result

    def visitFunctionCall(self, node: FunctionCallNode) -> str:
        identifier = node.identifier.value

        arguments = []

        for argument in node.arguments:
            argumentBin = self.visit(argument)
            arguments.append(argumentBin)

        return f"{identifier}(" + ",".join(arguments) + ")"
    
    def visitFunctionDefinition(self, node: FunctionDefinitionNode) -> str:
        identifier = node.identifier.value

        params = []

        for param in node.params:
            params.append(param.value)

        body = self.visit(node.body)

        return f"{identifier} = lambda {",".join(params)}: {body}"


    def visitIdentifier(self, node: IdentifierNode) -> str:
        return node.identifier.value

    def visitStream(self, node: StreamNode) -> str:
        identifier = node.identifier.value

        bits = []

        for bit in node.bits:
            bits.append(str(bit.value))

        return f"{identifier} = [{", ".join(bits)}]"

    def visitUnary(self, node: UnaryOperationNode) -> str:
        operator = node.operator

        if operator.type == TokenTypes.OUT:
            return f"print({self.visit(node.value)})"
        
        return f"not {self.visit(node.value)}"

    def visit(self, node: AST) -> str:
        if node.type == ASTTypes.BIT:
            return self.visitBit(node)
        
        if node.type == ASTTypes.ASSIGN:
            return self.visitAssign(node)
        
        if node.type == ASTTypes.BINARY_OPERATION:
            return self.visitBinaryOperation(node)

        if node.type == ASTTypes.COMPOUND:
            return self.visitCompound(node)

        if node.type == ASTTypes.FUNCTION_CALL:
            return self.visitFunctionCall(node)
        
        if node.type == ASTTypes.FUNCTION_DEFINITION:
            return self.visitFunctionDefinition(node)

        if node.type == ASTTypes.IDENTIFIER:
            return self.visitIdentifier(node)
        
        if node.type == ASTTypes.STREAM:
            return self.visitStream(node)

        if node.type == ASTTypes.UNARY_OPERATION:
            return self.visitUnary(node)

    def translate(self, head: AST) -> str:
        return self.visit(head)
