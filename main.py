import functions

contacts = []

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
    print("\nContacts list:")
    counter = 1
    for contact in contacts:
        print(f"\n{counter}. {contact["name"]}\nPhone Number: {contact["number"]}\nEmail: {contact["email"]}")
        counter += 1
        if contact["favorite"]:
            print("Favorite: [✔]")
        else:
            print("Favorite: [ ]")
    return

def update_contacts(contacts):
    if not contacts:
        print("\nNo contacts available to update!")
        return
    else:
        see_contacts(contacts)
    while True:
        choice = input("\nWhich contact would you like to update? ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(contacts):
                print("Type a valid contact index number")
            else:
                break
        except ValueError:
            print("Invalid index, please type an integer number")
    
    corrected_index = choice - 1

    print(f"\nYou chose the contact \"{contacts[corrected_index]["name"]}\"")

    current_contact = contacts[corrected_index]
    old_name = current_contact["name"]
    counter = 1
    for key, item in current_contact.items():
        if key == "favorite":
            continue
        print(f"{counter}. {key}: {item}")
        counter += 1

    mapped_dictionary = {
        "1": {"key": "name", "prompt": "Type a new name for this contact: "},
        "2": {"key": "number", "prompt": "Type a new number for this contact: "},
        "3": {"key": "email", "prompt": "Type a new email for this contact: "}
        }
    while True:
        choice = input(f"\nWhat would you like to change? ")

        if choice in mapped_dictionary:
            field_info = mapped_dictionary[choice]
            field_key = field_info["key"]
            current_prompt = field_info["prompt"]

            old_value = current_contact[field_key]
            new_value = input(current_prompt)
            contacts[corrected_index][field_key] = new_value

            print(f"\nThe {field_key} of the contact \"{old_name}\" was successfully updated from \"{old_value}\" to \"{new_value}\"")
            break
        
        else:
            print("Invalid choice. Please select a valid index")

def favorite_contact(contacts):
    if not contacts:
        print("\nNo contacts available to favorite!")
        return
    else:
        see_contacts(contacts)

    choice = input("\nWhich contact would you like to favorite? ")
    corrected_index = choice - 1
    chosen_contact = contacts[corrected_index]

    if chosen_contact["favorite"]:
        print("\nThis contact is already in the favorite list")
    else:
        contacts[corrected_index]["favorite"] == True
        print(f"\nThe contact \"{chosen_contact["name"]}\" is now in the favorite list!")
    
    return
    

    '''
    while True:
        choice = input(f"\nWhat would you like to change? ")
        try:
            choice = int(choice)
            if choice < 1 or choice > (len(current_contact) - 1):
                print("Type a valid index number")
            else:
                break
        except ValueError:
            print("Invalid index, please type an integer number")

    old_name = current_contact["name"]
    if choice == 1:
        new_name = input("Type a new name for this contact: ")
        contacts[corrected_index]["name"] = new_name
        print(f"\nName of the contact \"{old_name}\" was successfully updated to \"{new_name}\"")
    if choice == 2:
        new_number = input("Type a new number for this contact: ")
        contacts[corrected_index]["number"] = new_number
        print(f"\nNumber of the contact \"{current_contact["name"]}\" was successfully updated to \"{new_number}\"")
    if choice == 3:
        new_email = input("Type a new email for this contact: ")
        contacts[corrected_index]["email"] = new_email
        print(f"\nEmail of the contact \"{current_contact["name"]}\" was successfully updated to \"{new_email}\"")
    '''
    return


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

    if choice == "3":
        update_contacts(contacts)

    if choice =="4":
        favorite_contact(contacts)

    elif choice == "7":
        print("Programm terminated")
        break