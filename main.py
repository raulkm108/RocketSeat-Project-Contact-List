from menu_functions import add_new_contact, see_contacts, update_contacts, favorite_contact, see_favorites, delete_contact

contacts = []

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

    elif choice == "2":
        see_contacts(contacts)

    elif choice == "3":
        update_contacts(contacts)

    elif choice =="4":
        favorite_contact(contacts)

    elif choice == "5":
        see_favorites(contacts)

    elif choice =="6":
        delete_contact(contacts)

    elif choice == "7":
        print("Programm terminated")
        break