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

def see_contacts(contacts):
    if not contacts:
        print("No contacts available!")
        return False
    else:
        print("\nContacts list:")
        counter = 1
        for contact in contacts:
            print(f"\n{counter}. {contact["name"]}\nPhone Number: {contact["number"]}\nEmail: {contact["email"]}")
            counter += 1
            if contact["favorite"]:
                print("Favorite: [✔]")
            else:
                print("Favorite: [ ]")
        return True