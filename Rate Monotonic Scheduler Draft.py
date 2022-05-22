import copy

tasks = {0: {'Period': 20, 'Execution': 3}, 1: {'Period': 10, 'Execution': 2}, 2: {'Period': 5, 'Execution': 2}}
lcm = 20
print("The number of tasks are 3 with an lcm of 20")

def PriorityCalculator(TaskOrder_Priority):
    lcm = 20
    Priority = -1
    for i in TaskOrder_Priority.keys():
        if (TaskOrder_Priority[i]["Execution"] != 0):
            if (lcm > TaskOrder_Priority[i]["Period"] or lcm > tasks[i]["Period"]):
                lcm = tasks[i]["Period"]  # Checks the priority of each task based on period
                Priority = i
    return Priority

TempTask = copy.deepcopy(tasks)
for time in range(lcm):
    priority = PriorityCalculator(TempTask)

    if (priority==-1):
        print("Time Slot %d to Time Slot %d will be idle\n" % (time,time+1))
    else:
        print("Time Slot %d to Time slot %d is Task %d \n" % (time, time + 1, priority))

        TempTask[priority]["Execution"] -= 1 # Since the task has been executed, its exe will naturally decrease


    for i in TempTask.keys():
        TempTask[i]["Period"] -= 1 # The Period for each task decreases by 1 as time progresses
        if (TempTask[i]["Period"] == 0):
            TempTask[i] = copy.deepcopy(tasks[i])