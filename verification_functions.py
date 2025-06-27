def choice_verification (contacts, verb):
    while True:
        choice = input(f"\nWhich contact would you like to {verb}? ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(contacts):
                print("Type a valid contact index number")
            else:
                return choice
        except ValueError:
            print("Invalid index, please type an integer number")

    