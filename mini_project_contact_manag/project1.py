print("Міні-проєкт №1 — Менеджер контактів")
print("Створи набір функцій: ")
print("------*------*------*-------*-------*-------")

contacts = ["Ivo Bobul", "Stepan Hiha", "Sofia Rotaru"]

def add_contact():
    contact = input("Please enter new contact: ")
    contacts.append(contact)

def show_contact():
    for i in contacts:
        print(i)
    input("Press any key to continue.")
def find_contact():
    contact = input("Please enter your contact: ")
    if contact in contacts:
        index = contacts.index(contact)
        print(f"Your index contact: {index} ")
    else:
        print(f"Your contact: {contact} is not here") 

def delete_contact():
    delete_index = int(input("Write index of contact to delete: "))
    deleted = contacts.pop(delete_index)
    print(f"Contact:  {deleted} is deleted.")

def menu():
    while True:

        print("1. Add contact")
        print("2. Show contacts")
        print("3. Find contact")
        print("4. Delete contact")
        print("0. Exit")
        choice = input("Select your option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":   
            show_contact()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "0":
            break
        else: 
            print("Invalid input!")        
menu()
