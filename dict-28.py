# Create a dictionary containing names and phone numbers.
#
# Implement:
# - Add contact
# - Search contact
# - Update contact
# - Delete contact
# - Display all contacts

contacts = {"Ritesh": "9876543210", "Aditi": "9123456780"}


def add_contact(name, number):
    contacts[name] = number


def search_contact(name):
    return contacts.get(name, "Contact not found")


def update_contact(name, number):
    if name in contacts:
        contacts[name] = number
        return True
    return False


def delete_contact(name):
    return contacts.pop(name, None) is not None


def display_all_contacts():
    return contacts


if __name__ == "__main__":
    add_contact("Sahil", "9988776655")
    update_contact("Aditi", "9111222333")

    print(f"All contacts: {display_all_contacts()}")
    print(f"Search 'Ritesh': {search_contact('Ritesh')}")

    delete_contact("Sahil")
    print(f"After deleting Sahil: {display_all_contacts()}")
