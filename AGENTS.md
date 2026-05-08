# AGENTS.md

## Commands

- `uv run mkdocs serve` — start live-reload docs server
- `uv run mkdocs build` — build static site to `build/`
- `uv run mkdocs gh-deploy` — deploy to GitHub Pages from `build/`

## Stack

- Python 3.13, managed with `uv` (see `uv.lock`, `.venv`)
- MkDocs for documentation site; source in `docs/`, output in `build/`

## Conventions

- `build/` is the output directory (configured via `site_dir` in `mkdocs.yml`)
- No tests, linting, or typechecking configured
- `main.py` is a scratch script, not the project entrypoint
