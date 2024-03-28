from boole.analysis.parser import Parser
from boole.analysis.ast import AST
from boole.analysis.token import TokenTypes

class Interpreter(object):
    def __init__(self) -> None:
        self.parser = Parser()

    def visit(self, node: AST) -> bool:
        token = node.value

        if token.type == TokenTypes.AND:
            return self.visit(node.left) and self.visit(node.right)
        
        if token.type == TokenTypes.OR:
            return self.visit(node.left) or self.visit(node.right)
        
        if token.type == TokenTypes.LOGIC:
            return token.value

    def eval(self, text): 
        ast = self.parser.parse(text)

        return self.visit(ast)
