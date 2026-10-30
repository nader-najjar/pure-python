load("@rules_pyrefly//pyrefly:pyrefly.bzl", "pyrefly")

pyrefly_aspect = pyrefly(preset = "strict")
