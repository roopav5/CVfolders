import json
contacts = {}  # Dictionary 

def add_contact(mobile_number):
    if len(mobile_number)!= 10 or not mobile_number.isdigit():
       print("Invalid mobile number , mob number has to be 10 digit")
       return 
    if mobile_number not in contacts:
        name = input("Enter name: ")
        contacts[mobile_number] = name
        print("Contact added successfully!")
    else:
        print("Mobile number already exists in contacts.")

def remove_contact(mobile_number):
    if mobile_number in contacts:
        del contacts[mobile_number]
        print("Contact removed successfully!")
    else:
        print("No such mobile number exists in contacts.")

def edit_name(mobile_number): 
    if mobile_number not in contacts:
       print("No such mobile number exists") #correct it 
    if mobile_number in contacts:
        new_name = input("Enter new name: ")
        contacts[mobile_number] = new_name
        print("Name updated successfully!")
    #else:
        #print("No such mobile number exists in contacts.")

def display_all_contacts():
    #if mobile_number not in contacts:
      #s print("Enter mobile numbers to display")
    sorted_contacts = sorted(contacts.items(), key=lambda x: x[1])  # Sort contacts by name
    print("Contacts:")
    for mobile_number, name in sorted_contacts:
        print(f"{name}: {mobile_number}")
    result = json.dumps(contacts)
    print('watch ')
    print(result)
    

def display_contact_details():
    query = input("Enter name or mobile number : ")
    found = False
    for mobile_number, name in contacts.items():
        if query.lower() in name.lower() or query == mobile_number:
            print(name, "-", mobile_number)
            found = True
    if not found:
        print("No such contact exists.")

while True:
    print("\nContact Details Management System\n")
    print("1. Add a Mobile Number")
    print("2. Remove a Mobile Number")
    print("3. Edit Name Based on Mobile Number")
    print("4. Display All Contacts")
    print("5. Display Contact Details Based on Mobile Number or Name")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mobile_number = input("Enter mobile number: ")
        
        add_contact(mobile_number)
    elif choice == "2":
        mobile_number = input("Enter mobile number to remove: ")
        remove_contact(mobile_number)
    elif choice == "3":
        mobile_number = input("Enter mobile number to edit name: ")
        #new_name = input("Enter new name: ")
        edit_name(mobile_number)
    elif choice == "4":
        display_all_contacts()
    elif choice == "5":
        #query = input("Enter mobile number or name to search: ")
        display_contact_details()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
