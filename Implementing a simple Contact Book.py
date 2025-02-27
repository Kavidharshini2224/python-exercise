import os
import sys

CONTACT_FILE="contacts.txt"

def load_contacts():
    if op.path.exists(CONTACT_FILE):
        with open(CONTACTS_FILE,"r")as file:
            return [line.strip() for line in file.readlines()]
        return[]
def save_contacts(contacts):
    with open(CONTACTS_FILE,"W")as file:
        file.writelines("\n".join(contacts))

def view_contacts():
    contacts=load_contacts()
    if not contacts:
        print("no contacts availabe.")
    else:
        print("\ncontact List:")
        for idx,contact in enumerate(contacts,start=1):
            print(f"{idx}.{contact}")

def delete_contact():
    view_contacts()
    contacts = load_contacts()

    if not contacts:
        return

    try:
        contact_number = int(input("Enter contact number to delete: ")) - 1
        if 0 <= contact_number < len(contacts):
            removed_contact = contacts.pop(contact_number)
            save_contacts(contacts)
            print(f"Deleted contact: {removed_contact}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")


while True:
    display_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice.please try again.")
