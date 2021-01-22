import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("isort finitefloat tests")
    c.run("black finitefloat tests")
    c.run("flake8 finitefloat tests")
    c.run("mypy finitefloat tests")
    c.run("pytest tests")
