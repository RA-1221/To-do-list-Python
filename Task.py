import json

class Task:
    def __init__(self, title, is_done, Priority):
        self.title = title
        self.is_done = is_done
        self.priority = Priority

    def displayInfo(self):
        print("Title:", self.title)
        print("Status:", self.is_done)
        print("Priority:", self.priority)


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.loadTask()

    def addTask(self, task):
        self.tasks.append(task)
        self.saveTask()

    def viewTask(self):
        for task in self.tasks:
            task.displayInfo()

    def deleteTask(self):
        t = input("What's task you wanna remove? ")
        for task in self.tasks:
            if task.title == t:
                self.tasks.remove(task)
                self.saveTask()
                print("Task deleted")
                return

        print("Not found")


    def editTitle(self):
        found = False
        t = input("What task you wanna edit? ")

        for task in self.tasks:
            if task.title == t:

                newTitle = input("Enter the new title: ")
                task.title = newTitle
                self.saveTask()
                found = True
                break

        if found == False:
            print("Not found")


    def editPriority(self):
        found = False
        p = input("What task you wanna edit? ")

        for task in self.tasks:
            if task.priority == p:
                newPriority = input("Enter new priority: ")
                task.priority = newPriority
                self.saveTask()
                found = True
                break

        if found == False:
            print("Not found")


    def done(self):
        found = False
        d = input("Enter task title: ")

        for task in self.tasks:
            if task.title == d:
                task.is_done = True
                found = True
                self.saveTask()
                print("Task is done")
                break

        if found == False:
            print("Not found")


    def search(self):
        found = False
        s = input("Enter task: ")

        for task in self.tasks:
            if task.title == s:
                task.displayInfo()
                found = True
                break

        if found == False:
            print("Not found")


    def saveTask(self):
        data = []

        for task in self.tasks:
            taskData = {
                "title": task.title,
                "priority": task.priority,
                "is_done": task.is_done,
            }

            data.append(taskData)

        with open("tasks.json", "w") as file:
            json.dump(data, file)


    def loadTask(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

            self.tasks = []

            for task in data:
                newTask = Task(
                    task["title"],
                    task["is_done"],
                    task["priority"]
                )

                self.tasks.append(newTask)

        except FileNotFoundError:
            self.tasks = []


manager = TaskManager()

while True:
    print("===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Edit Title")
    print("5. Edit Priority")
    print("6. Delete Task")
    print("7. Mark Task as Done")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter title: ")
        priority = input("Enter priority: ")

        task = Task(title, False, priority)
        manager.addTask(task)

        print("Task added!")

    elif choice == "2":
        manager.viewTask()

    elif choice == "3":
        manager.search()

    elif choice == "4":
        manager.editTitle()

    elif choice == "5":
        manager.editPriority()

    elif choice == "6":
        manager.deleteTask()

    elif choice == "7":
        manager.done()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")