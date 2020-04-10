def add_task():

    while True:
        task_title = input("Remember to sanitie your hands! Please enter a title for the task: ")
        if task_title == "":
            print("ERROR: You did not enter a title you need to enter a title.")
        else:
            break

    print("  1 - Defcon1   2 - Defcon2   3 - Defcon3  ")

    while True:
        task_priority = input("Please enter a priority level for the task: ")
        try:
            task_priority_int = int(task_priority)
            if task_priority_int > 3 or task_priority_int < 0:
                print("ERROR: You need to enter priority options that are given.")
            else:
                break
        except ValueError:
            print("ERROR: You need to enter priority options that are given.")
    if task_priority_int == 3:
        priority = "Defcon3"
    if task_priority_int == 2:
        priority = "Defcon2"
    if task_priority_int == 1:
        priority = "Defcon1"
    return task_title, priority