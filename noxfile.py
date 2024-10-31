import nox

@nox.session
def tests(session):
    session.install("pytest", "pytest-cookies")
    session.run("pytest")