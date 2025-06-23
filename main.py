import functions

contacts = []

def add_new_contact(contacts):
    name = input("Type the person's name: ")
    number = input("Type it's phone number: ")
    email = input("Type it's Email: ")
    while True:
        favorite_choice = input ("Do you want it to be in your favorite list? [y / n]: ")
        if favorite_choice == "y":
            favorite = True
            break
        elif favorite_choice == "n":
            favorite = False
            break
        else:
            print("Type y or n")
    contact = {"name": name, "number": number, "email": email, "favorite": favorite}
    
    contacts = contacts.append(contact)

    print(f"\n{contact["name"]}'s contact was added successfully")

def see_contacts(contacts):
    print("\n Contacts list:")
    for contact in contacts:
        print(f"\nName: {contact["name"]}\nPhone Number: {contact["number"]}\nEmail: {contact["email"]}")
        if contact["favorite"]:
            print("Favorite: Yes")
        else:
            print("Favorite: No")


while True:
    print("\nContact List.")

    print("1. Add a new contact")
    print("2. See contacts")
    print("3. Update contact")
    print("4. Set a contact to Favorite")
    print("5. See favorites")
    print("6. Erase a contact")
    print("7. Leave")

    choice = input("Choose an action: ")

    if choice == "1":
        add_new_contact(contacts)

    if choice == "2":
        see_contacts(contacts)

    elif choice == "7":
        print("Programm terminated")
        break