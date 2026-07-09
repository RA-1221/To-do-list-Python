class Task:
    def __init__(self, title, is_done, Priority):
        self.title = title
        self.is_done = False
        self.priority = Priority

    def displayInfo(self):
        print("Title:", self.title)
        print("Status:", self.is_done)
        print("Priority:", self.priority)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def viewTask(self):
        for task in self.tasks:
            task.displayInfo()

    def deleteTask(self):
        t = input("What's task you wanna remove? ")
        for task in self.tasks:
            if task.title == t:
                self.tasks.remove(task)
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
                found = True
                break

        if found == False:
            print("Not found")

    def editPriority(self):
        found = False
        p = input("What task you wanna edit? ")

        for task in self.tasks:
            if task.title == p:
                newPriority = input("Enter new priority: ")
                task.priority = newPriority
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
        manager.deletTask()

    elif choice == "7":
        manager.done()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")