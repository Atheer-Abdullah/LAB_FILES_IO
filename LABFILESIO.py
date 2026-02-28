while True:
    user_input = input("Do you want to add a new To-Do item? (y/n) or type 'exit' to quit: ").strip().lower()
    
    if user_input == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break  
    
    elif user_input == "y":
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write("Weekend To-Do List\n")
            file.write("Pray Fajr on time\n")
            file.write("Morning Adhkar\n")
            file.write("Read a portion of the Quran\n")
            file.write("Be kind to parents (call or help them)\n")
            file.write("Study / Work with excellence\n")
            file.write("Pray Duha prayer\n")
            file.write("Give charity (even a small amount)\n")
            file.write("Evening Adhkar\n")
            file.write("Pray Witr\n")
            file.write("Make Istighfar before sleeping\n")
        print("To-Do list added successfully!\n")
    
    elif user_input == "n":
        list_input = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
        if list_input == "y":
            try:
                with open("to_do.txt", "r", encoding="utf-8") as file:
                    print("\nYour To-Do List:")
                    print(file.read())
            except FileNotFoundError:
                print("No To-Do list found yet. Please add items first.\n")
        elif list_input == "n":
            print("Returning to main menu...\n")
    
    else:
        print("Invalid input. Please type 'y', 'n', or 'exit'.\n")