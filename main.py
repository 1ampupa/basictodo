# Libraries
import lib.task as Tasks
import lib.datetime_handler as DTH

# Create Example Task
task_1 = Tasks.Task("Test Task A", DTH.DateTime().add(days=1)) # New Task, due in 1 days.
task_2 = Tasks.Task("Test Task B", DTH.DateTime().add(days=3)) # New Task, due in 3 days.
task_3 = Tasks.Task("Test Task C", None) # New Task, without deadline.
