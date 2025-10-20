import json

from lib.initialise import Initialise

# Task Instance

class Task:
    # Class Variables
    _TasksDict = {}
    _TaskIdIndexCounter = 1
    _TasksRefPath = None
    _TasksFolderPath = None

    # Constructor
    def __init__(self, TaskId=None, TaskName=None, TaskDue=None) -> None:
        # Check for TasksRefPath and TasksFolderPath
        Task._CheckPath()

        # Check Arguments and assign Task properties
        TaskId, TaskName, TaskDue = Task._CheckArgs(TaskId, TaskName, TaskDue)

        # Construct Task
        self.id = TaskId
        self.name = TaskName
        self.due = TaskDue
        self.path = Task._TasksFolderPath / f"{self.id}.json"

        Task._TaskIdIndexCounter += 1

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
    def _CheckArgs(TaskId, TaskName, TaskDue) -> list:
        TaskId = TaskId or f"Task{Task._TaskIdIndexCounter}"
        TaskName = TaskName or f"Task {Task._TaskIdIndexCounter}"
        TaskDue = TaskDue or None
        return TaskId, TaskName, TaskDue
    
    def _CreateTaskJSON(self) -> None:
        # Create reference into Task Dictionary
        Task._TasksDict[self.id] = str(self.path)
        
        # Create Task.json data
        TaskData = {
            "name": self.name,
            "due": str(self.due)
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
