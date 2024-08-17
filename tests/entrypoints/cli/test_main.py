from src.pytemplate.entrypoints.cli.main import main


def test_main(mocker):
    mocker.patch("builtins.input", side_effect=["45", "15", "+"])
    mocker.patch("builtins.print")
    main()
    assert True
