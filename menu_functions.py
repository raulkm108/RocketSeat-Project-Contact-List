from verification_functions import choice_verification

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
    

def update_contacts(contacts):
    if not see_contacts(contacts):
        return
    else:     
        choice = choice_verification(contacts,"Update")
        
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
    if not see_contacts(contacts):
        return
    else:
        choice = choice_verification(contacts,"Favorite")
        corrected_index = choice - 1
        chosen_contact = contacts[corrected_index]

        if chosen_contact["favorite"]:
            print("\nThis contact is already in the favorite list")
        else:
            contacts[corrected_index]["favorite"] = True
            print(f"\nThe contact \"{chosen_contact["name"]}\" is now in the favorite list!")
        
        return
    

def see_favorites(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        counter = 1
        print("\nFavorites list:")
        for contact in contacts:
            if contact["favorite"] == True:
                print(f"\n{counter}. {contact["name"]}\nPhone number: {contact["number"]}\nEmail: {contact["email"]}")
                counter += 1
        if counter == 1:
            print("No favorite contacts available")
    return
