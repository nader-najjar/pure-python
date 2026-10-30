# pure-python

> Python best practices with Bazel.

### 1. Prerequisites

---

Linux or macOS, ARM64 or x86-64. Install [Bazelisk](https://bazel.build/install/bazelisk); Bazel supplies the pinned Python interpreter and tools. Run commands from the repository root.

### 2. Build and Test

---

#### Everyday Commands

| Goal | Command |
| --- | --- |
| Build production code | `bazel build //:app_bin` |
| Run | `bazel run //:app_bin -- Ada` |
| Unit tests | `bazel test //:all_tests` |
| Run one test | `bazel test //:all_tests --test_arg=-k --test_arg=test_requires_a_name` |
| Flake8 | `bazel test //:lint` |
| Strict type checking | `bazel build //:app //:entrypoint //:all_tests --output_groups=pyrefly` |
| Coverage | `bazel coverage //:all_tests` |
| Package | `bazel build //:app_archive` |
| Full verification | `bazel build //... && bazel test //... //:requirements.test && bazel coverage //:all_tests` |
| Clean | `bazel clean` |

Builds check types. Tests and packaging build prerequisites automatically. Full verification checks lock freshness online. Coverage measures production code; no minimum is enforced.

#### Outputs

- Application and runtime: `bazel-bin/app_archive.tar`.
- Test logs: `bazel-testlogs/<target>/test.log`.
- Coverage: `$(bazel info output_path)/_coverage/_coverage_report.dat`.

### 3. Development Workflows

---

#### Dependency Management

- Add/remove or upgrade: edit pins in `requirements.in` and the consuming target's `deps` in `BUILD.bazel`.
- Refresh the hashed lock: `bazel run //:requirements.update`.
- Check lock freshness: `bazel test //:requirements.test` (requires network access).
- Inspect versions: `requirements_lock.txt`; trace a dependency with `bazel query 'somepath(//:app, @python_dependencies//pydantic_core)'`.

#### Toolchain Changes

- Bazel: `.bazelversion`.
- Python: keep `.python-version`, `MODULE.bazel` and `pyproject.toml` aligned; refresh the Python lock.
- Rules and Pyrefly: `MODULE.bazel`; refresh `MODULE.bazel.lock` with `bazel mod deps --lockfile_mode=update`.

Run full verification after changing tools or dependencies.

### 4. IDE Setup

---

Create the IDE environment from Bazel's interpreter and the same dependency lock:

```sh
bazel build //:all_tests
python="$(bazel info execution_root)/$(bazel cquery @rules_python//python:current_py_toolchain --output=starlark --starlark:expr='providers(target)["TemplateVariableInfo"].variables["PYTHON3"]')"
"$python" -m venv --clear .venv
.venv/bin/python -m pip install --require-hashes --only-binary=:all: -r requirements_lock.txt
```

Follow the [IntelliJ IDEA](https://app.notion.com/p/f4c0a2b7875583b79fa5015d58412fea) or [VS Code](https://app.notion.com/p/4fd0a2b787558204a6c001d0b034f698) guide. Select `.venv/bin/python` and mark `src/` as a source root; Pyrefly reads `pyproject.toml`.

Print the pinned Pyrefly executable, replacing `<platform>` with `linux_x86_64`, `linux_arm64`, `macos_x86_64` or `macos_arm64`:

```sh
echo "$(bazel info execution_root)/$(bazel cquery '@pyrefly_toolchains//internal:<platform>_impl' --output=starlark --starlark:expr='providers(target)["ToolchainInfo"].pyrefly.executable.path')"
```

Recreate `.venv` after dependency/interpreter changes or cache cleanup. Bazel never uses it.

### 5. Concepts

---

- [Bazel Python rules](https://rules-python.readthedocs.io/)
- [Pyrefly configuration](https://pyrefly.org/en/docs/configuration/)

### License

---

All rights reserved. See [LICENSE](LICENSE).
