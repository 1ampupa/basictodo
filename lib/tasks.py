import json

from pathlib import Path

from lib.initialise import Initialise

# Global Variables

TasksDict = {}
_TaskIdIndexCounter = 1
_TasksRefPath = None
_TasksFolderPath = None

# Task Instance

class Task:
    def __init__(self, TaskId=None, TaskName=None, TaskDue=None) -> None:
        global _TaskIdIndexCounter, _TasksRefPath, _TasksFolderPath
        # Check for TasksRefPath and TasksFolderPath
        if _TasksRefPath is None or _TasksFolderPath is None:
            _TasksRefPath, _TasksFolderPath = Initialise()

        # Check Arguments and assign Task's properties
        if TaskId is None:
            TaskId = f'Task{_TaskIdIndexCounter}'
        if TaskName is None:
            TaskName = f'Task {_TaskIdIndexCounter}'
        if TaskDue is None:
            pass
        
        # Construct Task
        self.id = TaskId
        self.name = TaskName
        self.due = TaskDue
        self.path = f'{_TasksFolderPath}\\{self.id}.json'

        _TaskIdIndexCounter += 1

        # Create reference into Task Dictionary
        TasksDict[TaskId] = self.path
        
        # Create Task.json data
        TaskData = {
            "name": self.name,
            "due": self.due
        }

        # Create Task.json file
        with open(self.path, 'w') as file:
            json.dump(TaskData, file, indent=4)

        # Update Task reference from Tasks list
        _UpdateTasksRef()

# Private Functions

def _UpdateTasksRef() -> None:
    global _TasksRefPath
    with open(_TasksRefPath,'w+') as file:
        json.dump(TasksDict.copy(), file, indent=4)
    
def GetTaskData(Task: Task) -> dict:
    _Data = json.load(open(TasksDict[Task.id]))
    return _Data
