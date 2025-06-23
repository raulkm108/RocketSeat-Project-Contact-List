import functions

contacts = []

while True:
    print("Contact List.")

    print("1. Add a new contact")
    print("2. See contacts")
    print("3. Update contact")
    print("4. Favorite a contact")
    print("5. See favorites")
    print("6. Erase a contact")
    print("7. Leave")

    choice = input("Choose an action: ")
    if choice == "7":
        break