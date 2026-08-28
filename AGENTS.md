# AGENTS.md

Tiny CLI: SVG → PNG, wraps `resvg-py`. Single entry point.

## Layout

- `src/svg2png_cli/cli.py` — the whole CLI (argparse + `resvg_py.svg_to_bytes`). No other modules.
- `pyproject.toml` — setuptools, `svg2png` console script → `svg2png_cli.cli:main`.
- `.github/workflows/publish.yml` — builds + publishes to PyPI on GitHub release (Trusted Publishing, no stored token).
- No test suite, no linter config. Keep changes proportional — this is a ~30-line script, not a framework.

## Commands

```bash
pip install -e .          # install for local dev
svg2png some.svg           # smoke-test the CLI
python -m build            # build sdist + wheel
```

## Conventions

- English for commits and README (per repo owner's global rule).
- Commit language: English.
- Version bump: `pyproject.toml` `[project].version`. Publish flow is GitHub Release → tag → `publish.yml` builds and pushes to PyPI.
- Never re-tag a version already released on PyPI — cut a new patch instead.
- `banners/svg2png-cli.png` is the README hero image — regenerate via the `portfolio-banner` skill if it needs to change, don't hand-edit.
