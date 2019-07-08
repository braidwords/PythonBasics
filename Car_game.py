menu = "help"
user_value = input("Write help to get the menu:").lower()
if user_value == menu:
    print("""Choose among the options: 
    1: Start the car
    2: Stop the car
    3: Exit """)
    user_menuInput = int(input())
    if user_menuInput == 1:
        print("Car started.......")
    elif user_menuInput == 2:
        print("Car stopped....!")
    else:
        print("you are out of the system")
else:
    print("I don't understand this")
