from pathlib import Path

from sphinx.application import Sphinx

THEME_NAME = "{{ cookiecutter.project_slug }}"

def setup(app: Sphinx) -> dict[str, bool]:
    """Setup the Sphinx application."""
    theme_path = (Path(__file__).parent / "theme" / THEME_NAME).resolve()
    app.add_html_theme(THEME_NAME, str(theme_path))

    return {"parallel_read_safe": True, "parallel_write_safe": True}