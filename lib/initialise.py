import json

from pathlib import Path

# Constant
DefaultTasksRefData = {}

# Create Default tasksref.json file
def CreateDefaultTasksRefJSON(TasksRefPath) -> dict:
    with open(TasksRefPath, 'w') as file:
        json.dump(DefaultTasksRefData.copy(), file, indent=4)
    return DefaultTasksRefData

# Init function
def Initialise() -> Path:
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

    # Get tasks folder
    DataFolderPath = Path("data/tasks")
    DataFolderPath.mkdir(exist_ok=True, parents=True) # Create if not exist

    return TasksRefPath, DataFolderPath # Return only PATH because its data can be updated anytime.
