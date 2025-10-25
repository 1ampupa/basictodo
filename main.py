# Libraries
from datetime import datetime

import lib.task as Tasks
import lib.datetime_handler as DTH

# Create Example Task
task1 = Tasks.Task("Test Task A", DTH.DateTime().add(days=3)) # New Task, due in 3 days.
task2 = Tasks.Task("Test Task B", DTH.DateTime().add(days=3)) # New Task, due in 3 days.
task3 = Tasks.Task("Test Task C", DTH.DateTime().add(days=3)) # New Task, due in 3 days.
