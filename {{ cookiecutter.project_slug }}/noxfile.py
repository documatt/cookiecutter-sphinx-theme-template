import nox

THEME_NAME = "{{ cookiecutter.project_slug }}"

SOURCEDIR = "sample_docs"
BUILDDIR = f"{SOURCEDIR}/build"
SPHINXOPTS = [
    {%- if cookiecutter.ablog %}
    # Cannot use maximum CPUs
    # "-j", "auto",
    # Due to the issue with Ablog which incorrectly claims itself as parallel
    # read safe, but it's not. See https://github.com/sunpy/ablog/issues/297.
    # Until fixed, we need to disable parallel builds.
    "-j", "1",
    {% endif -%}
    "-b",
    "html",
    "-T",
    "-W",
    "-q",
    "-D",
    f"html_theme={THEME_NAME}",
    SOURCEDIR,
    f"{BUILDDIR}/html",
]

NPM_INSTALL = ["npm", "--prefix", f"src/{THEME_NAME}", "install"]
NPM_BUILD = ["npm", "--prefix", f"src/{THEME_NAME}", "run", "build"]

# Default sessions when only "nox" is run
nox.options.sessions = ["build_theme", "build_docs"]

nox.options.reuse_existing_virtualenvs = True


@nox.session
def build_theme(session):
    """Build the theme."""
    # Build the theme with Node.js
    session.run(*NPM_INSTALL, external=True)
    session.run(*NPM_BUILD, external=True)


@nox.session
def build_docs(session):
    """Use the theme with sample Sphinx docs."""
    session.install("-e", ".")  # Install itself in editable mode
    session.run("sphinx-build", *SPHINXOPTS)


# To invoke other sessions, use "nox -s <session_name>[,<session_name>]"


@nox.session
def clean(session):
    session.run("rm", "-rf", BUILDDIR, external=True)


@nox.session
def preview(session):
    """Build and serve the documentation and theme with automatic reload on change."""
    build_theme(session)

    clean(session)

    session.install(
        "-e",
        ".",
        "sphinx-autobuild==2024.10.3",
    )

    autobuild_args = [
        # Watch theme files and Tailwind config
        "--watch",
        "src",
        # Build theme before building the docs
        "--pre-build",
        " ".join(NPM_BUILD),
        # Disable Sphinx's incremental build, recommended when developing themes
        "-a",
    ]

    session.run(
        "sphinx-autobuild",
        *SPHINXOPTS,
        *autobuild_args
    )


@nox.session
def test(session):
    session.install("pytest")
    session.run("pytest")