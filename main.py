import sys


class PlusExpression:
    def apply(self, a:int, b: int):
        return  a + b

class SubstractExpression:
    def apply(self, a:int, b:int):
        return  a - b

class MultiExpression:
    def apply(self, a:int, b:int):
        return  a * b

class DivisionExpression:
    def apply(self, a:int, b:int):
        return  a / b

class Calculator:
    def __init__(self, expression):
        self.__expression = expression

    def apply(self, a: int, b: int):
        return self.__expression.apply(a, b)


if __name__ == "__main__":
    expression = MultiExpression()
    calculator = Calculator(expression)
    print(calculator.apply(2, 3))