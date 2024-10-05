import os
from sys import executable

from argparse import ArgumentParser
from subprocess import run

from boole.analysis.lexer import Lexer
from boole.analysis.parser import Parser
from boole.translator import Translator

class Cli:
    def __init__(self) -> None:
        self.lexer = Lexer()
        self.parser = Parser()
        self.translator = Translator()

        self.argParser = ArgumentParser()

        self.argParser.add_argument("sourcePath")
        self.argParser.add_argument("--execute", action = "store_true")

    def run(self):
        args = self.argParser.parse_args()

        translation = ""

        filename = os.path.basename(args.sourcePath)
        dist = os.path.join(
            os.getcwd(),
            "bin"
        )

        if not os.path.exists(dist):
            os.getcwd(dist)     

        with open(args.sourcePath) as file:
            buffer = file.read()
            stream = self.lexer.lex(buffer)
            ast = self.parser.parse(stream)
            translation = self.translator.translate(ast)

        outputPath = os.path.join(dist, f"{filename}.py")

        with open(outputPath, "w") as file:
            file.write(translation)

        print(f"[CLI]: output in {outputPath}")

        if args.execute:
            print(f"[CLI]: running {outputPath}:")
            run([executable, outputPath])
