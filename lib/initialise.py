import json

from pathlib import Path

# Constant
DefaultTasksRefData = {"tasks":[]}

# Create Default tasksref.json file
def CreateDefaultTasksRefJSON(TasksRefPath):
    with open(TasksRefPath, 'w') as file:
        json.dump(DefaultTasksRefData, file, indent=4)
    return DefaultTasksRefData

# Init function
def Initialise():
    # Get data folder
    DataFolderPath = Path("data")
    DataFolderPath.mkdir(exist_ok=True) # Create if not exist

    # Get taskref.json
    TasksRefPath = DataFolderPath / "tasksref.json"

    try: # Check if tasksref.json is empty or not
        with open(TasksRefPath, 'r') as file:
            TasksRefData = json.load(file)
        # Check tasksref.json
        if "tasks" not in TasksRefData or not isinstance(TasksRefData["tasks"], list):
            TasksRefData = CreateDefaultTasksRefJSON(TasksRefPath)
    except (FileNotFoundError, json.JSONDecodeError):
        TasksRefData = CreateDefaultTasksRefJSON(TasksRefPath)

    return TasksRefPath # Return only PATH because its data can be updated anytime.