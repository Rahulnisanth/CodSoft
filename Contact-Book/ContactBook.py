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
    def view_contact(self):
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

