"""
Basic tests if generating template works.

Uses [Pytest-Cookies pytest plugin](https://github.com/hackebrot/pytest-cookies). It provides `cookies` fixture which is a Cookiecutter API.
"""
from pytest_cookies.plugin import Cookies


def test_bake(cookies: Cookies):
    result = cookies.bake(extra_context={"project_slug": "mytheme"})

    assert result.exit_code == 0
    assert result.exception is None
