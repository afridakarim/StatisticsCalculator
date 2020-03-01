import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from Statistics.randomData import *
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.statistics = Statistics()
        self.testData0 = randint(0, 10, 20)
        self.testData1 = random_code_no_seed()
        self.testData2 = random_select()
        self.testData3 = random_select_no_seed()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData0)
        self.assertEqual(mean, 4.25)



if __name__ == '__main__':
    unittest.main()
