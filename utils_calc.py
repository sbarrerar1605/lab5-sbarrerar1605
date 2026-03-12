def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2


def exponent(base, exp):
    return base ** exp


def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2


def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2


def absolute(num):
    return abs(num)