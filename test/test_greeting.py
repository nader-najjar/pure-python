import pytest
from pydantic import ValidationError

from greeting import Greeting


@pytest.mark.parametrize("name", ["Ada", "  Ada  ", "\tAda\n"])
def test_greets_with_a_trimmed_name(name: str) -> None:
    assert Greeting(name=name).message() == "Hello, Ada!"


@pytest.mark.parametrize("name", ["", " ", "\t\n", None, 1, True, [], {}])
def test_rejects_missing_or_non_string_names(name: object) -> None:
    with pytest.raises(ValidationError):
        Greeting.model_validate({"name": name})


def test_requires_a_name() -> None:
    with pytest.raises(ValidationError):
        Greeting.model_validate({})


def test_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Greeting.model_validate({"name": "Ada", "unexpected": True})
