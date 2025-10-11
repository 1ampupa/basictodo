import json

from pathlib import Path

from lib.initialise import Initialise


class Tasks:
    _TaskIdIndexCounter = 1
    TasksDict = {}
    TasksRefPath = None
    TasksFolderPath = None
    
    def __init__(self, TaskId=None, TaskName=None, TaskDue=None) -> None:
        # Check for TasksRefPath and TasksFolderPath
        if Tasks.TasksRefPath is None or Tasks.TasksFolderPath is None:
            Tasks.TasksRefPath, Tasks.TasksFolderPath = Initialise()

        # Check Arguments and assign Task's properties
        if TaskId is None:
            TaskId = f'Task{Tasks._TaskIdIndexCounter}'
        if TaskName is None:
            TaskName = f'Task {Tasks._TaskIdIndexCounter}'
        if TaskDue is None:
            pass
        
        # Construct Task
        self.id = TaskId
        self.name = TaskName
        self.due = TaskDue
        self.path = f'{Tasks.TasksFolderPath}/{self.id}.json'

        Tasks._TaskIdIndexCounter += 1

        # Create reference into Task Dictionary
        Tasks.TasksDict[TaskId] = self.path

        # TODO Create Task .json file
        with open(self.path, 'w') as file:
            json.dump({}, file, indent=4)

        # Update Task reference from Tasks list
        print(Tasks.TasksDict)
        Tasks.UpdateTasksRef()


    @staticmethod
    def UpdateTasksRef() -> None:
        with open(Tasks.TasksRefPath,'w+') as file:
            json.dump(Tasks.TasksDict.copy(), file, indent=4)
    