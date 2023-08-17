#Task 4: Contactbook

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("Contacts:")
        for name, phone_number in self.contacts.items():
            print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact: {name}\nPhone Number: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")
#Menu for interaction
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            contact_book.add_contact(name, phone_number)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#This code is used to run code inside the if statement while running.
if __name__ == "__main__":
    main()
