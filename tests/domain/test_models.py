from src.pytemplate.domain.models import Operands, operands_factory


def test_Operands():
    operands = Operands(first_operand=1, second_operand=2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2


def test_operands_factory():
    operands = operands_factory(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2
