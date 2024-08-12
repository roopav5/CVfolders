import json

class ContactManager:
    def __init__(self):
        self.contacts = {}  
        self.file_name = "contacts.json"  
        self.load_contacts_from_file()

    def add_contact(self, name, mobile_number):
        if mobile_number not in self.contacts:
            self.contacts[mobile_number] = name
            self.save_contacts_to_file()
            print("Contact added successfully.")
        else:
            print("Contact with this mobile number already exists.")

    def remove_contact(self, mobile_number):
        if mobile_number in self.contacts:
            del self.contacts[mobile_number]
            self.save_contacts_to_file()
            print("Contact removed successfully.")
        else:
            print("No such mobile number exists.")

    def save_contacts_to_file(self):
        with open(self.file_name, mode='w') as file:
            json.dump(self.contacts, file)

    def load_contacts_from_file(self):
        try:
            with open(self.file_name, mode='r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

def main():
    contact_manager = ContactManager()
    while True:
        print("\nMenu:")
        print("1. Add New Contact")
        print("2. Remove Existing Contact")
        print("3. Exit from the contacts menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            mobile_number = input("Enter the mobile number: ")
            contact_manager.add_contact(name, mobile_number)
        elif choice == "2":
            mobile_number = input("Enter the mobile number to remove: ")
            contact_manager.remove_contact(mobile_number)
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please check again")

# Start the program
main()
