import json # Saving all of the tasks to the json file
from task import Task # Creates a Task Object
from add_function import add_task # Gets user input for the title and priority level with exceptions built in
from del_function import delete_task # Gets user input for the index of the task the user wants to delete

class_file_list = []
dict_file_list = []
user_input = "Beginning of the Application String"

def take_from_json():
    with open("tasks.json") as file_object:     #This code pulls the tasks from the JSON file, then clears the dictionary array
        dict_file_list = json.load(file_object)
    for dict_task in dict_file_list:
        task = Task.from_dictionary(dict_task)
        class_file_list.append(task)
    dict_file_list.clear()

def send_to_json():
    for task in class_file_list:                    #This code puts the task into the JSON file, then clears out the arrays
        dict_file_list.append(task.__dict__)
    with open("tasks.json", "w") as file_object:
        json.dump(dict_file_list, file_object)
    dict_file_list.clear()

def add_a_task():
    key, value = add_task()
    task = Task(key, value)
    class_file_list.append(task)

def delete_a_task():
    if len(class_file_list) == 0:
        print("\nThere are no Tasks in your Task List!")
    else:
        for index in range(len(class_file_list)):
            print(f"{(index + 1)} - {class_file_list[index].title} - {class_file_list[index].priority}")
        while True:
            try:
                index_to_delete = del_task()
                del class_file_list[index_to_delete]
                break
            except IndexError:
                print("ERROR: Please enter a number from the list to delete.")
        print("Task Deleted Successfully!")

def back_to_menu():
    user_input = input("\nIf you would like to return to the menu press 'm'\nIf you would like to quit press 'q'\nIf you would like to change the list again press any key!\n")
    return user_input

def main_menu():
    user_input = input("\n_____________ MENU _____________\n  Press 1 to Add a Task\n  Press 2 to Delete a Task\n  Press 3 to View a Task List\n  Press 'q' to Quit the App\n") # Main Menu
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "q":
        print("ERROR: Please enter an option from the list!")
    return user_input

print("\nWelcome to the To-Do List Application!\n")

try:
    take_from_json()
except json.decoder.JSONDecodeError:
    print("\nTo begin your task list, let's start by adding a Task!\n")
    add_a_task()
    send_to_json()

while True: # Loops the Application for the user

    user_input = main_menu()

    if user_input == "1": # Adds a Task to the Task List
        while user_input != "m" and user_input != "q":
            add_a_task()
            send_to_json()
            print("\nTask Added Successfully!\n")
            user_input = back_to_menu()
        
    if user_input == "2": # Deletes a Task from the Task List
        while user_input != "m" and user_input != "q":
            cancel_input = input("\nAre you sure you would like to delete a task\nPress 'c' to cancel, or any other key to continue.\n")
            if cancel_input == "c":
                break
            delete_a_task()
            send_to_json()
            user_input = back_to_menu()

    if user_input == "3": # Views the Task List
        if len(class_file_list) == 0:
            print("\nThere are no Tasks in your Task List!\n")
        for index in range(len(class_file_list)):
            print(f"{(index + 1)} - {class_file_list[index].title} - {class_file_list[index].priority}")
        send_to_json()
        user_input = input("\nPress any key to return to the main menu, or press 'q' to quit: ")

    if user_input == "q": # Quits the Application
        print(" Awesome! keep getting things done!")
        print("   Remember Sanitize your hands!")
        print("    Staying home = Staying Safe")
        break