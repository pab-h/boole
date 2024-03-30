from unittest import TestCase

from boole.analysis.token import TokenError
from boole.analysis.token import TokenTypes
from boole.analysis.token import Token

from boole.analysis.lexer import Lexer

class TextLexer(TestCase):
    def setUp(self) -> None:
        self.lexer = Lexer()

    def testCoutOfTokens(self) -> None:
        text = "1+1*0"

        tokens = self.lexer.process(text)

        self.assertTrue(len(tokens) == len(text) + 1)

    def testRaiseInvalidToken(self) -> None:
        text = "2+1*0"

        with self.assertRaises(TokenError):
            self.lexer.process(text)

    def testEof(self) -> None:
        text = ""

        eofToken = self.lexer.process(text).pop()

        self.assertEqual(eofToken.type, TokenTypes.EOF)

    def testParsingTokenIsCorret(self) -> None:
        text = "1&0"

        tokensExpected = [
            Token(
                type = TokenTypes.LOGIC,
                value = True
            ),
            Token(
                type = TokenTypes.AND,
                value = TokenTypes.AND.name
            ),
            Token(
                type = TokenTypes.LOGIC,
                value = False
            ),
            Token(
                type = TokenTypes.EOF,
                value = None
            ),
        ]

        tokens = self.lexer.process(text)

        self.assertEqual(tokensExpected, tokens)

    def testSkipWhiteSpace(self) -> None:
        text = "1 & 0"

        tokens = self.lexer.process(text)

        self.assertTrue(len(tokens) == len(text) - 1)
