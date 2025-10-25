from datetime import datetime, date, time, timedelta
from typing import Optional

class DateTime:
    # Class Variables

    # Format Config
    _date_format : str = "%d/%m/%Y"
    _full_date_format : str = "%A %d/%m/%Y"
    _time_format : str = "%H:%M"
    _full_time_format : str = "%H:%M:%S"

    # Constructor
    def __init__(self, DateTime: Optional[datetime] = None):
        self.now : datetime = DateTime or datetime.now()

        self.year : int = int(self.now.strftime("%Y"))
        self.month : int = int(self.now.strftime("%m"))
        self.date : int = int(self.now.strftime("%d"))
        self.day : str = self.now.strftime("%A")
        self.hour : int = int(self.now.strftime("%H"))
        self.minute : int = int(self.now.strftime("%M"))
        self.second : int = int(self.now.strftime("%S"))

        self.full_date : str = date(year=self.year, month=self.month, day=self.date).isoformat()
        self.full_time : str = time(hour=self.hour, minute=self.minute, second=self.second).isoformat()

    # Query Functions

    def get_now_as_string(self, include_seconds : bool = False) -> str:
        if not isinstance(include_seconds, bool): 
            return self.now.strftime(DateTime._time_format)
        if include_seconds:
            return self.now.strftime(DateTime._full_time_format)
        return self.now.strftime(DateTime._time_format)
    
    def get_today_as_string(self, include_weekday : bool = False) -> str:
        if not isinstance(include_weekday, bool): 
            return self.now.strftime(DateTime._date_format)
        if include_weekday:
            return self.now.strftime(DateTime._full_date_format)
        return self.now.strftime(DateTime._date_format)
    
    def from_DateTime_to_dict(self) -> dict:
        return {
            "date": self.full_date,
            "time": self.full_time
        }
    
    @staticmethod
    def from_dict_to_DateTime(date_time_dict : dict) -> DateTime:
        if "date" not in date_time_dict or "time" not in date_time_dict:
            raise ValueError
        new_date_time = DateTime(datetime.fromisoformat(f"{date_time_dict['date']}T{date_time_dict['time']}"))
        return new_date_time
    
    # Date Time Calculation Functions

    def add(self, **kwargs) -> DateTime:
        try:
            new_date_time = self.now + timedelta(**kwargs)
            return DateTime(new_date_time)
        except Exception:
            raise ValueError

    def subtract(self, **kwargs) -> DateTime:
        try:
            new_date_time = self.now - timedelta(**kwargs)
            return DateTime(new_date_time)
        except Exception:
            raise ValueError

    # Date Time Comparation Functions
    def diff_with_DateTime(self, other_Date_Time : DateTime, unit : str) -> tuple:
        date_time_difference : timedelta = self.now - other_Date_Time.now
        difference : int = 0
        status : str = ""

        match unit.lower():
            case "days":
                difference = date_time_difference.days
            case "hours":
                difference = int(date_time_difference.total_seconds() / 3600)
            case "minutes":
                difference = int(date_time_difference.total_seconds() / 60)
            case "seconds":
                difference = int(date_time_difference.total_seconds())
            case _:
                difference = date_time_difference.days
        
        # Compare
        if difference == 0:
            status = "Exact"
        elif difference > 0:
            status = "Ahead"
        elif difference < 0:
            status = "Behind"

        return status, difference

    def __str__(self):
        return f"{self.full_date}T{self.full_time}"
