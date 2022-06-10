
import sys
# add person menu


def add_person_menu():
    print("""
    1. Add a new person
    2. Return to main menu
    """)


def main_menu():
    print("""********************************************************************
    \t\t\tPhonebook Application\n********************************************************************
	You can now perform the following operations on this phonebook\n
	1. Add a new contact
	2. Update an existing contact
	3. Remove an existing contact
	4. Delete all contacts
	5. Search for a contact
	6. Display all contacts
	7. Export all contacts
	8. Exit phonebook""")


def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Phonebook management system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


def update_menu():
    print("""
	1. Update name
	2. Update phone number
	3. Update email
	4. Update address
	5. Add another number
	6. Return to main menu
	""")


