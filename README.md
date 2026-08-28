# svg2png-cli

Tiny CLI to convert SVG to PNG. Wraps [resvg-py](https://pypi.org/project/resvg-py/) (pure Rust, no native Cairo/Inkscape dependency — the reason `cairosvg` fails out of the box on Windows).

## Install

```bash
pip install git+https://github.com/jeffersongoncalves/svg2png-cli.git
```

Or clone and install in editable mode:

```bash
git clone https://github.com/jeffersongoncalves/svg2png-cli.git
pip install -e ./svg2png-cli
```

## Usage

```bash
svg2png banner.svg                     # writes banner.png next to it
svg2png banner.svg out.png             # explicit output path
svg2png banner.svg out.png --width 1200 --height 630
```

Exits non-zero with an error message if the input file doesn't exist.
