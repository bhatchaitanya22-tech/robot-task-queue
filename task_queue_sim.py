# Robot Task Queue & State Simulation

tasks = [
    {"name": "Move to Station A", "time": 3, "state": "moving"},
    {"name": "Pick Object", "time": 2, "state": "picking"},
    {"name": "Move to Station B", "time": 4, "state": "moving"},
    {"name": "Place Object", "time": 2, "state": "placing"},
]

current_time = 0
state_log = []

print("Starting robot task execution...\n")

for task in tasks:
    print(f"Executing: {task['name']} | State: {task['state']}")
    current_time += task["time"]
    state_log.append(task["state"])
    print(f"Time taken: {task['time']} units")
    print(f"Total elapsed time: {current_time} units\n")

print("All tasks completed.")
print("Total execution time:", current_time)
print("State log:", state_log)
