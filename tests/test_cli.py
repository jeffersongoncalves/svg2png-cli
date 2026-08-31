import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from svg2png_cli.cli import convert

SVG = b'<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"><rect width="10" height="10" fill="red"/></svg>'


def test_convert_writes_png() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        svg, png = tmp / "a.svg", tmp / "a.png"
        svg.write_bytes(SVG)

        output = convert(svg)

        assert output == png
        assert png.exists()
        assert png.stat().st_size > 0


def test_convert_missing_file_raises() -> None:
    try:
        convert(Path("does-not-exist.svg"))
    except FileNotFoundError:
        return
    raise AssertionError("expected FileNotFoundError")


if __name__ == "__main__":
    test_convert_writes_png()
    test_convert_missing_file_raises()
    print("ok")
