from datetime import datetime, date, time, timedelta

class DateTime:
    # Class Variables

    # Format Config
    _DateFormat = "%d/%m/%Y"
    _FullDateFormat = "%A %d/%m/%Y"
    _TimeFormat = "%H:%M"
    _FullTimeFormat = "%H:%M:%S"

    # Constructor
    def __init__(self):
        self.now : datetime = datetime.now()
        self.year : int = int(self.now.strftime("%Y"))
        self.month : int = int(self.now.strftime("%m"))
        self.date : int = int(self.now.strftime("%d"))
        self.day : str = self.now.strftime("%A")
        self.hour : int = int(self.now.strftime("%H"))
        self.minute : int = int(self.now.strftime("%M"))
        self.second : int = int(self.now.strftime("%S"))

        self.fullDate : date = date(year=self.year, month=self.month, day=self.date)
        self.fullTime : time = time(hour=self.hour, minute=self.minute, second=self.second)

    # Query Functions

    def GetNowAsString(self, IncludeSecond : bool) -> str:
        if IncludeSecond:
            return self.now.strftime(DateTime._FullTimeFormat)
        return self.now.strftime(DateTime._TimeFormat)
    
    def GetTodayAsString(self, IncludeWeekday) -> str:
        if IncludeWeekday:
            return self.now.strftime(DateTime._FullDateFormat)
        return self.now.strftime(DateTime._DateFormat)
    
    def GetDateTimeAsDict(self) -> dict:
        return {
            "date": self.fullDate.isoformat(),
            "time": self.fullTime.strftime(self._TimeFormat)
        }
    
    # Date Time Calculation Functions

    def Add(self, _Attribute : str, _Value : int) -> datetime:
        try:
            _New_Time = self.now + timedelta(**{_Attribute:_Value})
            return _New_Time
        except Exception as _E:
            print(_E)

    def Subtract(self, _Attribute : str, _Value : int) -> datetime:
        try:
            _New_Time = self.now - timedelta(**{_Attribute:_Value})
            return _New_Time
        except Exception as _E:
            print(_E)

    # Date Time Comparation Functions
    def DiffWithDateTime(self, _OtherDatetime : datetime, _Unit : str) -> int:
        _Diff = self.now - _OtherDatetime
        _Diff_In_Seconds = _Diff.total_seconds()

        match _Unit.lower():
            case "seconds": return int(_Diff_In_Seconds)
            case "minutes": return int(_Diff_In_Seconds // 60)
            case "hours": return int(_Diff_In_Seconds // 3600)
            case "days": return _Diff.days
            case _:
                print("Error in function 'DateTime.DiffWithDateTime': Invalid unit received. Return day difference.")
                return _Diff.days

    def __str__(self):
        return f"{self.fullTime} {self.fullDate}"
