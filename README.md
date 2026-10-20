# pure-python

Bazel-managed Python template. Application source and tests are empty for now.

```sh
bazel build //...
bazel test //...
bazel run //:requirements.update
```

Bazel pins Python and Pyrefly. `requirements.in` declares Python packages; pip-tools generates the hashed `requirements_lock.txt`. Bazel target dependencies separate runtime, test, and development tools.

Pydantic handles parsing and validation, pytest is reserved for application tests, Flake8 checks style, and Pyrefly checks types in strict mode during builds. No formatter is configured. The Pyrefly editor extension reads `pyproject.toml`; Bazel uses `tools/typecheck.bzl`.

Input boundaries should use strict validation, reject duplicate JSON keys before Pydantic validation, and distinguish missing values from null.

Bug analysis, logging, and dependency injection remain TODOs in `requirements.in`. Additional structural style rules, including a complete multiline trailing-comma check, remain to be formalized.
