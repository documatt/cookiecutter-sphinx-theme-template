# Sphinx Theme Template

<!-- https://github.com/TezRomacH/python-package-template/blob/master/README.md -->

<div style="margin: 0 auto;">

![GitHub License](https://img.shields.io/github/license/documatt/cookiecutter-sphinx-theme-template)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/documatt/cookiecutter-sphinx-theme-template/tests.yaml)

A Cookiecutter template for creating modern Sphinx documentation theme with Tailwind CSS, Alphine.js and automatic live reload on change.

</div>

## TL;DR

1. Install Cookiecutter.

2. Generate template by answering simple questions

   ```
   cookiecutter gh:documatt/cookiecutter-sphinx-theme-template
   ```

## Features

## Shared between project and template

The following files are shared between Cookiecutter project (`/`) and Cookiecutter template that will be generated (``{{ cookiecutter.project_slug }}/`):

- `.gitignore`
- `package.json` and `package-lock.json` for Prettier formatter
- `.vscode/extensions.json` - recommended VSCode extension
- `.vscode/settings.json` - VSCode settings
- `.github/workflows/tests.yaml`
