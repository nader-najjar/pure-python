import runpy
import sys


def main() -> None:
    module, *arguments = sys.argv[1:]
    sys.argv = [module, *arguments]
    runpy.run_module(module, run_name="__main__")


if __name__ == "__main__":
    main()
