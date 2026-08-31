import argparse
import sys
from pathlib import Path

import resvg_py


def convert(svg: Path, png: Path | None = None, width: int | None = None, height: int | None = None) -> Path:
    if not svg.exists():
        raise FileNotFoundError(f"{svg} not found")

    output = png or svg.with_suffix(".png")

    kwargs = {"svg_path": str(svg)}
    if width:
        kwargs["width"] = width
    if height:
        kwargs["height"] = height

    data = resvg_py.svg_to_bytes(**kwargs)
    output.write_bytes(bytes(data))
    return output


def main() -> None:
    parser = argparse.ArgumentParser(prog="svg2png", description="Convert an SVG file to PNG.")
    parser.add_argument("svg", type=Path, help="Path to the source .svg file")
    parser.add_argument("png", type=Path, nargs="?", help="Output .png path (default: same name as SVG)")
    parser.add_argument("--width", type=int, help="Output width in px (default: SVG's own size)")
    parser.add_argument("--height", type=int, help="Output height in px (default: SVG's own size)")
    args = parser.parse_args()

    try:
        output = convert(args.svg, args.png, args.width, args.height)
    except FileNotFoundError as e:
        sys.exit(f"error: {e}")

    print(f"{output} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
