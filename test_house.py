import unittest
import draw_house

from matplotlib.testing.compare import compare_images

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

class TestHouse(unittest.TestCase):
    
    def test_house_drawing(self, TOLERANCE: float = 1.0):
        '''
        This tests that the house drawing matches
        what is shown in the test directory

        @param TOLERANCE: 0,255 higher is more lax
        '''

        #draws house
        draw_house.main()

        #loads svg files
        generated_house = svg2rlg("house.svg")
        true_house = svg2rlg("test_data/house.svg")

        #stores them as pngs
        renderPM.drawToFile(generated_house, "house.png", fmt = "PNG")
        renderPM.drawToFile(true_house, "test_data/house.png", fmt = "PNG")
        
        #does matplotlib compare, if within tolerance returns none else returns rmsd
        self.assertIsNone(compare_images("house.png", "test_data/house.png", TOLERANCE))

if __name__ == "__main__":
    unittest.main()
