import sys
#add person menu
def add_person_menu():
    print("""
    1. Add a new person
    2. Return to main menu
    """)

def main_menu():
    print("""********************************************************************
    \t\t\tSMARTPHONE DIRECTORY\n********************************************************************
	You can now perform the following operations on this phonebook\n
	1. Add a new contact
	2. Remove an existing contact
	3. Delete all contacts
	4. Search for a contact
	5. Display all contacts
	6. Exit phonebook""")

def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
	print("********************************************************************")
	print("Thank you for using our Smartphone directory system.")
	print("Please visit again!")
	print("********************************************************************")
	sys.exit("Goodbye, have a nice day ahead!")