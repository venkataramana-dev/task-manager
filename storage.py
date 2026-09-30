



def save_tasks(tasks):
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks():
    file = open("tasks.txt", "r")
    tasks = []

    for line in file:
        tasks.append(line.strip())

    return tasks
