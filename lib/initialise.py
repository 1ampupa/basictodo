import json

from pathlib import Path

# Constant
_default_tasks_ref_data = {"tasks": []}

# Create Default tasksref.json file
def create_default_tasks_ref_JSON(tasks_ref_path: Path) -> dict:
    with open(tasks_ref_path, 'w') as file:
        json.dump(_default_tasks_ref_data.copy(), file, indent=4)
    return _default_tasks_ref_data

# Init function
def initialise() -> tuple[Path, Path]:
    # Get data folder
    data_folder_path : Path = Path("data")
    data_folder_path.mkdir(exist_ok=True) # Create if not exist

    # Get taskref.json
    tasks_ref_path = data_folder_path / "tasksref.json"

    try: # Check if tasksref.json is empty or not
        with open(tasks_ref_path, 'r') as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        create_default_tasks_ref_JSON(tasks_ref_path)

    # Get tasks folder
    tasks_folder_path : Path = Path("data/tasks")
    tasks_folder_path.mkdir(exist_ok=True, parents=True) # Create if not exist

    return tasks_ref_path, tasks_folder_path # Return only PATH because its data can be updated anytime.
