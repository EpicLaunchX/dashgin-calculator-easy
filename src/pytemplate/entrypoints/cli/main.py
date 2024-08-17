from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


class ActionEnum:
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def main():
    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    action = input("Enter the action (+, -, *, /): ")

    calculator = Calculator()
    operands = operands_factory(first_operand, second_operand)

    if action == ActionEnum.ADD:
        result = calculator.add(operands)
    elif action == ActionEnum.SUBTRACT:
        result = calculator.subtract(operands)
    elif action == ActionEnum.MULTIPLY:
        result = calculator.multiply(operands)
    elif action == ActionEnum.DIVIDE:
        result = calculator.divide(operands)
    else:
        raise ValueError("Invalid action")

    print(f"Result: {result}")
