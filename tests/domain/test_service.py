from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add():
    calculator = Calculator()
    operands = operands_factory(45, 15)

    assert calculator.add(operands) == 60


def test_subtract():
    calculator = Calculator()
    operands = operands_factory(45, 15)

    assert calculator.subtract(operands) == 30


def test_multiply():
    calculator = Calculator()
    operands = operands_factory(45, 15)

    assert calculator.multiply(operands) == 675


def test_divide():
    calculator = Calculator()
    operands = operands_factory(45, 15)

    assert calculator.divide(operands) == 3.0
