import nox

@nox.session
def test(session):
    session.install("pytest", "pytest-cookies")
    session.run("pytest")