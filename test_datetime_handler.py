import unittest
from datetime import date, time, datetime, timedelta
from lib import datetime_handler as DTH

class Test(unittest.TestCase):
    def test_01_func_GetNowAsString(self):
        dt = DTH.DateTime()
        result = dt.GetNowAsString(True)
        print(result)
        self.assertIsInstance(result, str) # Check if result is str
    
    def test_02_func_GetTodayAsString(self):
        dt = DTH.DateTime()
        result = dt.GetTodayAsString(True)
        print(result)
        self.assertIsInstance(result, str) # Check if result is str

    def test_03_func_GetDateTimeAsDict(self):
        dt = DTH.DateTime()
        result = dt.GetDateTimeAsDict()
        print(result)
        self.assertIsInstance(result, dict) # Check if result is dict

    def test_04_func_Add(self):
        dt = DTH.DateTime()
        result = dt.Add("days",1)
        print(result)
        self.assertIsInstance(result, datetime) # Check if result is datetime

    def test_05_func_Sub(self):
        dt = DTH.DateTime()
        result = dt.Subtract("days",1)
        print(result)
        self.assertIsInstance(result, datetime) # Check if result is datetime

    def test_06_func_DiffWithDateTime(self):
        dt1 = DTH.DateTime()
        dt2 = dt1.Add("days", 3) # Add 3 days into current Datetime
        print(dt1, dt2)
        result = dt1.DiffWithDateTime(dt2, "days") # Compare dt2 w/ dt1
        print(f"Diffrence between {dt1} and {dt2} is {result} days")
        self.assertIsInstance(result, tuple) # Check if result is int
        self.assertIsNot(dt1,dt2) # Check if dt 1 != dt2


if __name__ == "__main__":
    unittest.main()
