import json

from pathlib import Path

# Constant
_default_tasks_ref_data = {}

# Create Default tasksref.json file
def create_default_tasks_ref_JSON(_tasks_ref_path: Path) -> dict:
    with open(_tasks_ref_path, 'w') as file:
        json.dump(_default_tasks_ref_data.copy(), file, indent=4)
    return _default_tasks_ref_data

# Init function
def initialise() -> tuple[Path, Path]:
    # Get data folder
    _data_folder_path : Path = Path("data")
    _data_folder_path.mkdir(exist_ok=True) # Create if not exist

    # Get taskref.json
    _tasks_ref_path = _data_folder_path / "tasksref.json"

    try: # Check if tasksref.json is empty or not
        with open(_tasks_ref_path, 'r') as file:
            tasks_ref_data = json.load(file)
        # Check tasksref.json
        if "tasks" not in tasks_ref_data or not isinstance(tasks_ref_data["tasks"], list):
            tasks_ref_data = create_default_tasks_ref_JSON(_tasks_ref_path)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_ref_data = create_default_tasks_ref_JSON(_tasks_ref_path)

    # Get tasks folder
    _tasks_folder_path : Path = Path("data/tasks")
    _tasks_folder_path.mkdir(exist_ok=True, parents=True) # Create if not exist

    return _tasks_ref_path, _tasks_folder_path # Return only PATH because its data can be updated anytime.
