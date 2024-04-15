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

    def testIdentifier(self) -> None:
        identifierParsed = self.lexer.process("abaco").pop()

        self.assertTrue(
            identifierParsed.type, 
            TokenTypes.IDENTIFIER
        )

    def testAssign(self) -> None:
        assignParsed = self.lexer.process("=").pop()

        self.assertTrue(
            assignParsed.type, 
            TokenTypes.ASSIGN
        )

    def testBreakLine(self) -> None:
        breaklineParsed = self.lexer.process("\n").pop()

        self.assertTrue(
            breaklineParsed.type, 
            TokenTypes.BREAKLINE
        )

    def testNot(self) -> None:
        not1Parsed = self.lexer.process("!").pop()
        not2Parsed = self.lexer.process("~").pop()

        self.assertTrue(
            not1Parsed.type, 
            TokenTypes.NOT
        )
        self.assertTrue(
            not2Parsed.type, 
            TokenTypes.NOT
        )

    def testOr(self) -> None:
        or1Parsed = self.lexer.process("|").pop()
        or2Parsed = self.lexer.process("+").pop()

        self.assertTrue(
            or1Parsed.type, 
            TokenTypes.NOT
        )
        self.assertTrue(
            or2Parsed.type, 
            TokenTypes.NOT
        )

    def testAnd(self) -> None:
        and1Parsed = self.lexer.process("*").pop()
        and2Parsed = self.lexer.process("&").pop()

        self.assertTrue(
            and1Parsed.type, 
            TokenTypes.AND
        )
        self.assertTrue(
            and2Parsed.type, 
            TokenTypes.AND
        )

    def testLeftBracket(self) -> None:
        leftBracket1Parsed = self.lexer.process("(").pop()
        leftBracket2Parsed = self.lexer.process("{").pop()
        leftBracket3Parsed = self.lexer.process("[").pop()

        self.assertTrue(
            leftBracket1Parsed.type, 
            TokenTypes.LEFTBRACKET
        )
        self.assertTrue(
            leftBracket2Parsed.type, 
            TokenTypes.LEFTBRACKET
        )
        self.assertTrue(
            leftBracket3Parsed.type, 
            TokenTypes.LEFTBRACKET
        )

    def testRightBracket(self) -> None:
        rightBracket1Parsed = self.lexer.process("]").pop()
        rightBracket2Parsed = self.lexer.process("}").pop()
        rightBracket3Parsed = self.lexer.process(")").pop()

        self.assertTrue(
            rightBracket1Parsed.type, 
            TokenTypes.RIGHTBRACKET
        )
        self.assertTrue(
            rightBracket2Parsed.type, 
            TokenTypes.RIGHTBRACKET
        )
        self.assertTrue(
            rightBracket3Parsed.type, 
            TokenTypes.RIGHTBRACKET
        )
