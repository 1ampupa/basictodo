from datetime import datetime, date, time, timedelta

class DateTime:
    # Class Variables

    # Format Config
    _DateFormat : str = "%d/%m/%Y"
    _FullDateFormat : str = "%A %d/%m/%Y"
    _TimeFormat : str = "%H:%M"
    _FullTimeFormat : str = "%H:%M:%S"

    # Constructor
    def __init__(self, DateTime: datetime = None):
        self.now : datetime = DateTime or datetime.now()

        self.year : int = int(self.now.strftime("%Y"))
        self.month : int = int(self.now.strftime("%m"))
        self.date : int = int(self.now.strftime("%d"))
        self.day : str = self.now.strftime("%A")
        self.hour : int = int(self.now.strftime("%H"))
        self.minute : int = int(self.now.strftime("%M"))
        self.second : int = int(self.now.strftime("%S"))

        self.fullDate : str = date(year=self.year, month=self.month, day=self.date).isoformat()
        self.fullTime : str = time(hour=self.hour, minute=self.minute, second=self.second).isoformat()

    # Query Functions

    def GetNowAsString(self, IncludeSeconds : bool = False) -> str:
        if not isinstance(IncludeSeconds, bool): 
            return self.now.strftime(DateTime._TimeFormat)
        if IncludeSeconds:
            return self.now.strftime(DateTime._FullTimeFormat)
        return self.now.strftime(DateTime._TimeFormat)
    
    def GetTodayAsString(self, IncludeWeekday : bool = False) -> str:
        if not isinstance(IncludeWeekday, bool): 
            return self.now.strftime(DateTime._DateFormat)
        if IncludeWeekday:
            return self.now.strftime(DateTime._FullDateFormat)
        return self.now.strftime(DateTime._DateFormat)
    
    def GetDateTimeAsDict(self) -> dict:
        return {
            "date": self.fullDate,
            "time": self.fullTime
        }
    
    @staticmethod
    def FromDictToDateTime(DateTimeDict : dict) -> DateTime:
        if "date" not in DateTimeDict or "time" not in DateTimeDict:
            return False
        DateTimeDict = DateTime(datetime.fromisoformat(f"{DateTimeDict["date"]}T{DateTimeDict["time"]}"))
        return DateTimeDict
    
    # Date Time Calculation Functions

    def Add(self, **kwargs) -> DateTime:
        try:
            New_DateTime = self.now + timedelta(**kwargs)
            return DateTime(New_DateTime)
        except Exception:
            return False

    def Subtract(self, **kwargs) -> DateTime:
        try:
            New_DateTime = self.now - timedelta(**kwargs)
            return DateTime(New_DateTime)
        except Exception:
            return False

    # Date Time Comparation Functions
    def DiffWithDateTime(self, OtherDatetime : DateTime, Unit : str) -> tuple:
        DateTimeDifference : timedelta = self.now - OtherDatetime.now
        Difference : int = 0
        Status : str = ""

        match Unit.lower():
            case "days":
                Difference = int(DateTimeDifference.total_seconds() / 864000)
            case "hours":
                Difference = int(DateTimeDifference.total_seconds() / 3600)
            case "minutes":
                Difference = int(DateTimeDifference.total_seconds() / 60)
            case "seconds":
                Difference = int(DateTimeDifference.total_seconds())
            case _:
                Difference = int(DateTimeDifference.total_seconds() / 864000)
        
        # Compare
        if Difference == 0:
            Status = "Exact"
        elif Difference > 0:
            Status = "Ahead"
        elif Difference < 0:
            Status = "Behind"

        return Status, Difference

    def __str__(self):
        return f"{self.fullDate}T{self.fullTime}"
