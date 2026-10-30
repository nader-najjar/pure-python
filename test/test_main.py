import pytest

from main import main


def test_prints_the_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main(["Ada"])
    captured = capsys.readouterr()
    assert captured.out == "Hello, Ada!\n"
    assert captured.err == ""


@pytest.mark.parametrize("arguments", [[], [""], [" "], ["Ada", "extra"]])
def test_rejects_invalid_arguments(arguments: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main(arguments)
    assert error.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "error:" in captured.err
