import unittest
from random import choice, randint
from app import Figure

class TestFigure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once before all tests"""
        print("Starting TestFigure tests")

    def setUp(self) -> None:
        """Runs before each test"""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Testing type: expected {self.figure}, got {self.obj.get_figure_type}")
        self.assertEqual(
            self.figure, 
            self.obj.get_figure_type,
            "Property get_figure_type returned wrong figure!"
        )

    def test_figure_length(self):
    
        self.assertEqual(
            self.length,
            self.obj.get_figure_length,
            "Property get_figure_length returned wrong length!"
        )

    def test_obj_creation_invalid(self):
       
        with self.assertRaises(AssertionError):
            Figure("circle", 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)  
