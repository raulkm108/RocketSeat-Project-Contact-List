def add_new_contact(contacts):
    name = input("Type the person's name: ")
    number = input("Type it's phone number: ")
    email = input("Type it's Email: ")
    while True:
        favorite_choice = input("Do you want it to be in your favorite list? [y / n]: ").lower()
        if favorite_choice == "y":
            favorite = True
            break
        elif favorite_choice == "n":
            favorite = False
            break
        else:
            print("Invalid input. Please type 'y' for yes and 'n' for no")
    contact = {"name": name, "number": number, "email": email, "favorite": favorite}
    
    contacts.append(contact)

    print(f"\n{contact["name"]}'s contact was added successfully")

    return