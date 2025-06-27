from menu_functions import add_new_contact, see_contacts, update_contacts
from verification_functions import choice_verification

contacts = []

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

def delete_contact(contacts):
    if not see_contacts(contacts):
        return
    else:
        choice = choice_verification(contacts,"Remove")
        corrected_index = choice - 1
        removed_contact = contacts.pop(corrected_index)

        print(f"The contact \"{removed_contact["name"]}\" was succesfully removed")

        return

    # previous method before improving it
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

    if choice == "5":
        see_favorites(contacts)

    if choice =="6":
        delete_contact(contacts)

    elif choice == "7":
        print("Programm terminated")
        break