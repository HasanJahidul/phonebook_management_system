from menus import *
from functions import  *
def start():
    main_menu()
    menu = input("Please enter a menu number: ")
    while menu != '8':
        if menu == '1':
            add_contact()
        elif menu == '2':
            update_contact()
        elif menu == '3':
            remove_contact()
        elif menu == '4':
            remove_all_contacts()
        elif menu == '5':
            search()
        elif menu == '6':
            show_all_contacts()
        elif menu == '7':
            export_to_file()
        else:
            print("Invalid menu number")
        menu = input("Please enter a menu number: ")
    thanks()
start()