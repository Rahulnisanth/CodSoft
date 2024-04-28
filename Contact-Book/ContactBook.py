class Contact:
    def __init__(self, name, phone, email, location) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location

class ContactBook:
    def __init__(self) -> None:
        self.contacts = []

    # Adding contact :
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    # Viewing contacts :
    def view_contacts(self):
        if not self.contacts:
            print("Message: Your contact book is empty.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}    Phone: {contact.phone}")

    # Searching contacts :
    def search_contact(self, keyword):
        found = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone or keyword in contact.email or keyword.lower() in contact.location.lower():
                found.append(contact)
        if not found:
            print("Message: No matching contacts found.")
        else:
            print(f"Matching contacts for \'{keyword.capitalize()}\' :")
            for item in found:
                print(f'Name: {item.name}    Phone: {item.phone}')
    
    # Updating the contacts :
    def update_contact(self, name, new_number):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_number
                print('Message: Contact updated successfully.')
                return
        print("Message: Contact not found.")
    
    # Deleting contact :
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print('Message: Contact deleted successfully.')
                return
        print("Message: Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            location = input("Enter contact location: ")
            contact = Contact(name, phone_number, email, location)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter search keyword (name or location)/(phone or email): ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            contact_book.update_contact(name, new_phone_number)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book...!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()