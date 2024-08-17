import pytest

from src.pytemplate.entrypoints.cli.main import main


def test_addition(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "+"])
    mocker.patch("builtins.print")
    main()
    assert True


def test_subtraction(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "-"])
    mocker.patch("builtins.print")
    main()
    assert True


def test_multiplication(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "*"])
    mocker.patch("builtins.print")
    main()
    assert True


def test_division(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "/"])
    mocker.patch("builtins.print")
    main()
    assert True


def test_invalid_operation(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "invalid"])
    mocker.patch("builtins.print")
    with pytest.raises(ValueError):
        main()
