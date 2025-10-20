import json

from lib.initialise import Initialise

from pathlib import Path

from typing import Optional

from datetime import datetime

# Task Instance

class Task:
    # Class Variables
    _TasksDict : dict = {}
    _TaskIdIndexCounter : int = 1
    _TasksRefPath : Path = None
    _TasksFolderPath : Path = None

    # Constructor
    def __init__(self, TaskName : Optional[str], TaskDue : Optional[datetime]) -> None:
        # Check for TasksRefPath and TasksFolderPath
        Task._CheckPath()

        # Check Arguments and assign Task properties
        TaskName, TaskDue = Task._CheckArgs(
            TaskName, TaskDue
        )

        # Construct Task
        self.id : str = f"Task{Task._TaskIdIndexCounter}"
        self.name : str = TaskName
        self.due : datetime = TaskDue
        self.status : str = "Incomplete"
        self.path : Path = Task._TasksFolderPath / f"{self.id}.json"

        Task._TaskIdIndexCounter += 1

        # Create reference into Task Dictionary
        Task._TasksDict[self.id] = str(self.path)

        # Create Task JSON file
        Task._CreateTaskJSON(self)

        # Update Task reference from Tasks list
        Task._UpdateTasksRef()
    
    # Class Functions
    @staticmethod
    def _CheckPath() -> None:
        if Task._TasksRefPath is None or Task._TasksFolderPath is None:
            Task._TasksRefPath, Task._TasksFolderPath = Initialise()

    @staticmethod
    def _CheckArgs(TaskName, TaskDue) -> list:
        TaskName : str = TaskName or f"Untitled Task {Task._TaskIdIndexCounter}"
        TaskDue : datetime = TaskDue or "No deadline"
        return TaskName, TaskDue
    
    def _CreateTaskJSON(self) -> None:
        # Create Task.json data
        TaskData : dict = {
            "name": self.name,
            "due": str(self.due),
            "status": self.status
        }

        # Create Task.json file
        with open(self.path, "w") as file:
            json.dump(TaskData, file, indent=4)

    @classmethod
    def _UpdateTasksRef(cls) -> None:
        with open(cls._TasksRefPath,"w+") as file:
            json.dump(cls._TasksDict.copy(), file, indent=4)

    def GetTaskData(self) -> dict:
        with open(self.path, "r") as file:
            _Data = json.load(file)
        return _Data
