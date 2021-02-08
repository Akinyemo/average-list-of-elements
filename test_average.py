import unittest
import average

class Testvolume(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average.calc_average([1,2,3,4,5]),3)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            average.calc_average([])
    
    def test_type(self):
        with self.assertRaises(TypeError):
            average.calc_average('Bolaji')

if __name__ == "__main__":
    unittest.main()