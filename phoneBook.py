from menus import *
import json
from add_contact import add_contact

import pickle
phoneBook = []
# lookup


def lookup():
    name = input("Please enter the name: ")
    for entry in phoneBook:
        if name == entry[0]:
            print("Name:", entry[0])
            print("Phone:", entry[1])
            print("Address:", entry[2])
            print("Email:", entry[3])
            break
    else:
        print("Name not found")


def main():
    main_menu()
    menu = input("Please enter a menu number: ")
    while menu != '3':
        if menu == '1':
            lookup()
        elif menu == '2':
            add_contact()
        else:
            print("Invalid menu number")
        menu = input("Please enter a menu number: ")
    print("Goodbye")
    #exDict = {'exDict': 'exDict'}


main()
