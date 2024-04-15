from typing import Optional

from boole.analysis.ast import *

class Symbol(object): 
    def __init__(self, name: str, type: 'Symbol' = None) -> None:
        self.name = name
        self.type = type 

    def __repr__(self) -> str:
        return f"<symbol: { self.name }>"

class BuiltinTypeSymbol(Symbol):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class VariableSymbol(Symbol):
    def __init__(self, name: str, symbol: BuiltinTypeSymbol) -> None:
        super().__init__(name, symbol)

class SymbolTable(object):
    def __init__(self) -> None:
        self.symbols: dict[str, Symbol] = {}

        self.define(BuiltinTypeSymbol("BIT"))

    def __repr__(self) -> str:
        return str(self.symbols)

    def define(self, symbol: Symbol) -> None:
        self.symbols.update({ symbol. name: symbol })

    def lookup(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)
    
class SymbolTableBuilder(object): 
    def __init__(self) -> None:
        self.table = SymbolTable()

    def __repr__(self) -> str:
        return str(self.table)

    def visitCompound(self, node: CompoundNode) -> None:
        for statement in node.statements:
            self.visit(statement)

    def visitVariableDeclaration(self, node: VariableDeclarationNode) -> None:
        typeName = node.type.value
        typeSymbol = self.table.lookup(typeName)
        
        variableName = node.assignment.left.value
        variableSymbol = VariableSymbol(
            name = variableName,
            symbol = typeSymbol
        )

        self.table.define(variableSymbol)

    def visit(self, node: AST) -> None:
        if node.type == ASTNodeTypes.COMPOUND:
            self.visitCompound(node)

        if node.type == ASTNodeTypes.VARIABLEDECLARATION:
            self.visitVariableDeclaration(node)

    def build(self, ast: AST) -> SymbolTable:
        self.visit(ast)
        return self.table
