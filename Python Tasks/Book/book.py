#Task : Contactbook

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")


    def display_all_contacts(self):
        for name, phone_number in self.contacts.items():
            print(f"Name: {name}, Phone Number: {phone_number}")

def main():
    contact_book = ContactBook()
    
#Menu for interaction
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            contact_book.add_contact(name, phone_number)
            print("Contact added successfully!")

        elif choice == '2':
            name = input("\nEnter name to search: ")
            phone_number = contact_book.get_contact(name)
            print(f"\nPhone Number: {phone_number}")

        elif choice == '3':
            contact_book.display_all_contacts()
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
