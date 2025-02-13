from fractions import Fraction

def multiply():
    try:
        num1 = Fraction(input("first"))
        num2 = Fraction(input("second"))
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    except ValueError:
        print("请重新输入")


multiply()