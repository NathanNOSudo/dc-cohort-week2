import json

data = [{"first name" : "", 
        "last name" : "",
        "age" : "" }]

while True:
    print("\n *** USER ID DATABASE *** \n")
    print("Please return '1' to view users")
    print("Please return '2' to add a new user")
    print("Please return 'q' to quit application \n")

    userinput = input("Please choose from a choice above and hit ENTER. : ")

    if userinput == "q":
        break

    if userinput == "1":

        with open("ids.json") as file:
            users = json.load(file)
            print(users)

        print(dict)

    if userinput == "2":

        firstname = input("please provide first name : ")
        lastname = input("please provide last name : ")
        age = input("please provide your age : ")
        data.append({"first name" : firstname, "last name" : lastname, "age" : age})

        with open("ids.json", "w") as file:
            json.dump(data, file)