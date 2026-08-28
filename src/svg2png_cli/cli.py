import argparse
import sys
from pathlib import Path

import resvg_py


def main() -> None:
    parser = argparse.ArgumentParser(prog="svg2png", description="Convert an SVG file to PNG.")
    parser.add_argument("svg", type=Path, help="Path to the source .svg file")
    parser.add_argument("png", type=Path, nargs="?", help="Output .png path (default: same name as SVG)")
    parser.add_argument("--width", type=int, help="Output width in px (default: SVG's own size)")
    parser.add_argument("--height", type=int, help="Output height in px (default: SVG's own size)")
    args = parser.parse_args()

    if not args.svg.exists():
        sys.exit(f"error: {args.svg} not found")

    output = args.png or args.svg.with_suffix(".png")

    kwargs = {"svg_path": str(args.svg)}
    if args.width:
        kwargs["width"] = args.width
    if args.height:
        kwargs["height"] = args.height

    data = resvg_py.svg_to_bytes(**kwargs)
    output.write_bytes(bytes(data))
    print(f"{output} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
