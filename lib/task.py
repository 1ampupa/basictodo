import json

from lib.initialise import initialise
from lib.datetime_handler import DateTime

from pathlib import Path
from typing import Optional
from datetime import datetime

# Task Instance

class Task:
    # Class Variables
    _tasks_dict : dict[str, str] = {}
    _task_id_index_counter : int = 1
    _tasks_ref_path : Path = Path()
    _tasks_folder_path : Path = Path()

    # Constructor
    def __init__(self, task_name : Optional[str], task_due : Optional[DateTime]) -> None:
        # Check for TasksRefPath and TasksFolderPath
        Task._check_path()

        # Check Arguments and assign Task properties
        checked_name, checked_due = Task._check_arguments(task_name, task_due)

        # Construct Task
        self.id : str = f"Task{Task._task_id_index_counter}"
        self.name : str = checked_name
        self.status : str = "Incomplete"
        self.due : DateTime | None = checked_due or None
        self.path : Path = Task._tasks_folder_path / f"{self.id}.json"

        Task._task_id_index_counter += 1

        # Create reference into Task Dictionary
        Task._tasks_dict[self.id] = str(self.path)

        # Create Task JSON file
        Task._create_task_as_JSON(self)

        # Update Task reference from Tasks list
        Task._update_tasks_ref()
    
    # Class Functions
    @staticmethod
    def _check_path() -> None:
        if not Task._tasks_ref_path.is_file() or not Task._tasks_folder_path.is_dir():
            Task._tasks_ref_path, Task._tasks_folder_path = initialise()

    @staticmethod
    def _check_arguments(task_name : str|None, task_due : DateTime|None) -> tuple[str, DateTime|None]:
        task_name = task_name or f"Untitled Task {Task._task_id_index_counter}"
        task_due = task_due or None
        return task_name, task_due
    
    def _create_task_as_JSON(self) -> None:
        # Create Task.json data
        task_data : dict = {
            "name": self.name,
            "status": self.status,
            "due": str(self.due) if self.due else None
        }

        # Create Task.json file
        with open(self.path, "w") as file:
            json.dump(task_data, file, indent=4)

    @classmethod
    def _update_tasks_ref(cls) -> None:
        with open(cls._tasks_ref_path,"w") as file:
            json.dump(cls._tasks_dict.copy(), file, indent=4)

    def get_task_data(self) -> dict:
        with open(self.path, "r") as file:
            data = json.load(file)
        return data
