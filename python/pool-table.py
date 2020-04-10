def print_pool_table_title():
    print("                     ____        ")
    print("                 ,dP9CGG88@b,        ")
    print("               ,IP  _   Y888@@b,        ")
    print("              dIi  (_)   G8888@b        ")
    print("             dCII  (_)   G8888@@b        ")
    print("             GCCIi     ,GG8888@@@        ")
    print("             GGCCCCCCCGGG88888@@@        ")
    print("             GGGGCCCGGGG88888@@@@..............        ")
    print("             Y8GGGGGG8888888@@@@P................        ")
    print("              Y88888888888@@@@@P.................        ")
    print("               Y8888888@@@@@@@P.................        ")
    print("                 `@@@@@@@@@P`..................        ")
    print("                     ----...................        ")
    print("(__   ____________________________________________   __)")
    print("   | |                                            | |")
    print("   | |                                            | |")
    print("   | |               Digigtalcrafts               | |")
    print("   | |                 Pool Table                 | |")
    print("   | |                 Management                 | |")
    print("   | |                                            | |")
    print(" __| |By:Nathan NOSudo____________________________| |__")
    print("(__   ____________________________________________   __)")
    print("   | |                                            | |")

def pool_table_menu():
    print("Press [1] to View Pool Tables")
    print("Press [2] to Occupy Pool Table")
    print("Press [3] to Un-Occupy Pool Table")
    print("Press [q] to Quit")


print_pool_table_title()
user_input = ""

tables = []
while user_input != "q":

    pool_table_menu()
    user_input = input("What would you like to do? ")
    if user_input == "1":
        print("---------------------")
        print("---- Pool Tables ----")
        print("---------------------")
        for table in range(0, 13):
            print(f"Table {table+1}")
        print("---------------------")
    elif user_input == "2":
        occupy_input = input("Type in number of pool table you would like to occupy. ")
