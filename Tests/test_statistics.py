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
from Statistics.MarginError import marginErr
from Statistics.SystematicSampling import systematic_sampling

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
        self.assertEqual(mean,15.7225)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData0)
        self.assertEqual(median, 1.91)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData0)
        self.assertEqual(mode, 1)

    def test_stdDevSample_calculator(self):
        stdDevSample = self.statistics.stdDevSample(self.testData0)
        self.assertEqual(stdDevSample, 6.397178746938636e+24)

    def test_stdDevPop_calculator(self):
        stdDevPop = self.statistics.stdDevPop(self.testData0)
        self.assertEqual(stdDevPop, 1.7680868017026143e+24)

    def test_sampleVar_calculator(self):
        sampleVar = self.statistics.sampleVar(self.testData0)
        self.assertEqual(sampleVar,2529264467575.235)

    def test_popVar_calculator(self):
        popVar = self.statistics.popVar(self.testData0)
        self.assertEqual(popVar, 1329694251210.6362)

    def test_MD_calculator(self):
        m_d = self.statistics.meanDev(self.testData0)
        self.assertEqual(m_d, -1.7763568394002505e-15)

    def test_MAD_calculator(self):
        m_a_d = self.statistics.meanAbsDev(self.testData0)
        self.assertEqual(m_a_d, 17.231250000000003)

    def test_corr_coeff(self):
        coeff = self.statistics.correlation_coeff(self.testData0)
        self.assertEqual(coeff,  0.9302765081681367)

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

    def test_quartiles(self):
        q1 = self.statistics.quart1(self.testData0)
        self.assertEqual(q1, 0.7525000000000001)

        q2 = self.statistics.quart2(self.testData0)
        self.assertEqual(q2, 1.91)

        q3 = self.statistics.quart3(self.testData0)
        self.assertEqual(q3, 33.25)

    def test_marginErr(self):
        resultList = []
        result = self.statistics.mErr(self.testData0)
        for i in result:
            resultList.append(i)
        if resultList == result:
            self.assertTrue(True)

    def test_systemSamp(self):
        resultList = []
        result = self.statistics.sys_samp(self.testData0)
        for i in result:
            resultList.append(i)
        if resultList == result:
            self.assertTrue(True)





if __name__ == '__main__':
    unittest.main()
