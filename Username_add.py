user_names = []
while True:
    print("""Choose your option from below
    1. Add a user
    2. Delete a user
    3. Show all users
    4. Exit""")
    user_choice = int(input())
    if user_choice == 1:
        print("Enter your user name: ")
        user_input = input()
        user_names.insert(len(user_names), user_input)
        print("User added!")
    elif user_choice == 2:
        print("Enter user name to be deleted: ")
        user_input = input()
        if user_input in user_names:
            user_names.remove(user_input)
            print("User removed")
        else:
            print("user not found in the list")
    elif user_choice == 3:
        print(user_names)
    elif user_choice == 4:
        print("Thank you :)")
        break
    else:
        print("Not a valid option")
