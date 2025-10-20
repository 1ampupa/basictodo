import unittest
from datetime import date, time, datetime, timedelta
from lib import datetime_handler as DTH

class Test(unittest.TestCase):
    def test_01_func_GetNowAsString(self):
        dt = DTH.DateTime()
        result = dt.GetNowAsString(True)
        print(result)
        self.assertIsInstance(result, str)

    def test_02_func_Add(self):
        dt = DTH.DateTime()
        result = dt.Add("days",1)
        print(result)
        self.assertIsInstance(result, datetime)

    def test_03_func_Sub(self):
        dt = DTH.DateTime()
        result = dt.Subtract("days",1)
        print(result)
        self.assertIsInstance(result, datetime)


if __name__ == "__main__":
    unittest.main()
