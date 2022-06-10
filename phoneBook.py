from menus import *
import json
from add_contact import add_contact
from functions import *


def main():
    main_menu()
    menu = input("Please enter a menu number: ")
    while menu != '7':
        if menu == '1':
            add_contact()
        elif menu == '2':
            remove_contact()
        elif menu == '3':
            remove_all_contacts()
        elif menu == '4':
            search()
        elif menu == '5':
            show_all_contacts()
        elif menu == '6':
            export_to_file()
        else:
            print("Invalid menu number")
        menu = input("Please enter a menu number: ")
    thanks()
    #exDict = {'exDict': 'exDict'}


main()
