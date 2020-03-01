import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from Statistics.randomData import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        #seed(5)
        self.statistics = Statistics()
        self.testData0 = random_code()
        self.testData1 = random_code_no_seed()
        self.testData2 = random_select()
        self.testData3 = random_select_no_seed()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData0)
        self.assertEqual(30.81, round(mean,2))

    def test_median_calculator(self):
        median = self.statistics.median(self.testData0)
        self.assertEqual(median, 2.91)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData0)
        self.assertEqual(mode, 1)



if __name__ == '__main__':
    unittest.main()
