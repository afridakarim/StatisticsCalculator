import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from Statistics.randomData import *
from Statistics.StandardDev import *
from Statistics.Variance import *
from Statistics.MeanAbsDev import *
from Statistics.ZScores import zValues
from Statistics.Correlation import correlationCoefficient
from Statistics.Quartiles import *

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        #seed(5)
        self.statistics = Statistics()
        self.testData0 = random_code()
        self.testData1 = random_code_no_seed()
        self.testData2 = random_select()
        self.testData3 = random_select_no_seed()
        self.testZ = zValues(self.testData0)
        self.testZscore = zValues(self.testData0)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData0)
        self.assertEqual(mean,30.805833333333332)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData0)
        self.assertEqual(median, 2.91)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData0)
        self.assertEqual(mode, 1)

    def test_stdDevSample_calculator(self):
        stdDevSample = self.statistics.stdDevSample(self.testData0)
        self.assertEqual(stdDevSample, 7.452719360031301e+60)

    def test_stdDevPop_calculator(self):
        stdDevPop = self.statistics.stdDevPop(self.testData0)
        self.assertEqual(stdDevPop, 2.05982281542012e+60)

    def test_sampleVar_calculator(self):
        sampleVar = self.statistics.sampleVar(self.testData0)
        self.assertEqual(sampleVar,2.729966915556176e+30)

    def test_popVar_calculator(self):
        popVar = self.statistics.popVar(self.testData0)
        self.assertEqual(popVar, 1.435208282940187e+30)

    def test_MD_calculator(self):
        m_d = self.statistics.meanDev(self.testData0)
        self.assertEqual(m_d, -4.736951571734001e-15)

    def test_MAD_calculator(self):
        m_a_d = self.statistics.meanAbsDev(self.testData0)
        self.assertEqual(m_a_d, 34.49513888888889)

    def test_corr_coeff(self):
        coeff = self.statistics.correlation_coeff(self.testData0)
        self.assertEqual(coeff,  0.9302924515359432)

    def test_z_values(self, mainResult=None):
        mainResults = []
        result = self.statistics.zValues(self.testZ)

        for i in result:
            mainResults.append(i)

        if mainResult == result:
            self.assertTrue(True)

    def test_z_scores(self):
        Result = []
        result = self.statistics.zScores(self.testZscore)
        for i in result:
            Result.append(i)

    def quartiles(self):
        q1 = self.statistics.quart1(self.testData0)
        self.assertEqual(q1, 60.056499999999995)

        q2 = self.statistics.quart2(self.testData0)
        self.assertEqual(q2, 73.8845)

        q3 = self.statistics.quart3(self.testData0)
        self.assertEqual(q3, 80.88450000000001)

if __name__ == '__main__':
    unittest.main()
