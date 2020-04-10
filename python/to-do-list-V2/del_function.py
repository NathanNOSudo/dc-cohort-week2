def delete_task():
    while True:
        delete_input = input("NO GOING BACK AFTER THIS! Select the task you'd like to remove from the list: ")
        try:
            delete_index = int(delete_input)
            delete_index -= 1
            return delete_index
        except ValueError:
            print("ERROR: Enter a number from the list to delete.")