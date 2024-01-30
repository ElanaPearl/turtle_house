import tempfile
import unittest
from pathlib import Path

from matplotlib.testing.compare import compare_images
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

import draw_house


def convert_house_to_png(svg_path: Path) -> Path:
    """Converts svg to png using reportlab

    :param svg_path: path to svg file
    :return: path to png file
    """
    png_path = svg_path.parent / (svg_path.stem + ".png")
    house = svg2rlg(svg_path)
    renderPM.drawToFile(house, png_path, fmt="PNG")

    return png_path


class TestHouse(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # convert house.svg to png only once so all tests can use it
        cls.true_house_png = convert_house_to_png(Path("test_data/house.svg"))

    def test_house_drawing(self, TOLERANCE: float = 1.0):
        """This tests that the house drawing is the same as the original house drawing

        :param TOLERANCE: The tolerance for the comparison
        """

        with tempfile.TemporaryDirectory() as tmpdirname:
            svg_path = Path(tmpdirname) / "house.svg"
            draw_house.main(output_file=svg_path)
            new_house_png = convert_house_to_png(svg_path=svg_path)

            # does matplotlib compare, if within tolerance returns none else returns rmsd
            self.assertIsNone(
                compare_images(new_house_png, self.true_house_png, TOLERANCE)
            )

    def test_house_mismatch(self, TOLERANCE: float = 1.0):
        """This tests that compare_images doesn't return None when there is a mismatch"""
        with tempfile.TemporaryDirectory() as tmpdirname:
            svg_path = Path(tmpdirname) / "house.svg"
            draw_house.main(output_file=svg_path, start=(-100, -100))
            new_house_png = convert_house_to_png(svg_path=svg_path)

            self.assertIsNotNone(
                compare_images(new_house_png, self.true_house_png, TOLERANCE)
            )


if __name__ == "__main__":
    unittest.main()
