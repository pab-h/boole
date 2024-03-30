from unittest import TestCase

from boole.Interpreter import Interpreter

class TextLexer(TestCase):
    def setUp(self) -> None:
        self.interpreter = Interpreter()

    def testOROperator(self) -> None:
        self.assertFalse(self.interpreter.eval("0+0"))
        self.assertTrue(self.interpreter.eval("0|1"))
        self.assertTrue(self.interpreter.eval("1+0"))
        self.assertTrue(self.interpreter.eval("1+1"))

    def testANDOperator(self) -> None:
        self.assertFalse(self.interpreter.eval("0*0"))
        self.assertFalse(self.interpreter.eval("0&1"))
        self.assertFalse(self.interpreter.eval("1*0"))
        self.assertTrue(self.interpreter.eval("1*1"))

    def testNOTOperator(self) -> None:
        self.assertTrue(self.interpreter.eval("!0"))
        self.assertFalse(self.interpreter.eval("!!0"))
        self.assertFalse(self.interpreter.eval("!1"))

    def testCompositeExpression(self) -> None:
        text = "!((1+0)+1)"
        self.assertFalse(self.interpreter.eval(text))
