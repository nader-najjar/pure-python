import argparse

from pydantic import ValidationError

from greeting import Greeting


def main(arguments: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    arguments_parsed = parser.parse_args(arguments)
    try:
        greeting = Greeting.model_validate(vars(arguments_parsed))
    except ValidationError as error:
        parser.error(str(error))
    print(greeting.message())


if __name__ == "__main__":
    main()
