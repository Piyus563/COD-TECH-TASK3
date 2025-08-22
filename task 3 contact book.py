class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add a new contact
    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("\n✅ Contact added successfully!")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("\n📂 No contacts found!")
            return
        print("\n📞 Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    # Search contact by name or phone
    def search_contact(self, keyword):
        found = [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone]
        if not found:
            print("\n❌ No contact found!")
        else:
            print("\n🔍 Search Results:")
            for contact in found:
                print(contact)

    # Update contact
    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\n✏️ Updating Contact...")
                contact.name = input("Enter new name: ") or contact.name
                contact.phone = input("Enter new phone: ") or contact.phone
                contact.email = input("Enter new email: ") or contact.email
                contact.address = input("Enter new address: ") or contact.address
                print("\n✅ Contact updated successfully!")
                return
        print("\n❌ Contact not found!")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("\n🗑️ Contact deleted successfully!")
                return
        print("\n❌ Contact not found!")


# User Interface (Menu-driven)
def main():
    cb = ContactBook()

    while True:
        print("\n===== 📒 CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            cb.add_contact(name, phone, email, address)

        elif choice == "2":
            cb.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            cb.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            cb.update_contact(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            cb.delete_contact(name)

        elif choice == "6":
            print("\n👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
