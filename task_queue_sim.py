# Robot Task Queue & State Simulation
# Simulates sequential task execution for a robot
# Tracks task states and total execution time

tasks = [
    {"name": "Move to Station A", "time": 3, "state": "moving"},
    {"name": "Pick Object", "time": 2, "state": "picking"},
    {"name": "Move to Station B", "time": 4, "state": "moving"},
    {"name": "Place Object", "time": 2, "state": "placing"},
]

elapsed_time = 0
state_log = []  # keep track of robot states

print("Starting robot task execution...\n")

for task in tasks:
    print(f"Executing: {task['name']} | State: {task['state']}")
    elapsed_time += task["time"]
    state_log.append(task["state"])
    print(f"Time for this task: {task['time']} units")
    print(f"Total elapsed time so far: {elapsed_time} units\n")

print("All tasks completed.")
print("Total execution time:", elapsed_time)
print("State Log:", state_log)
