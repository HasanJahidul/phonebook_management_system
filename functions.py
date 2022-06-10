from add_contact import Dict, add_values_in_dict
from validation import *
import pandas as pd


def search():
    name = input("Please enter the name: ")
    for entry in Dict:
        if name == entry[0]:
            print("Name:", entry[0])
            print("Phone:", entry[1])
            print("Address:", entry[2])
            print("Email:", entry[3])
            break
    else:
        print("Name not found")

# remove contact


def remove_contact():
    name = input("Please enter the name: ")
    for entry in Dict:
        if name == entry[0]:
            Dict.remove(entry)
            print("Contact removed")
            break
    else:
        print("Name not found")


# remove all contacts
def remove_all_contacts():
    Dict.clear()
    print("All contacts removed")


# add multiple numbers
def add_more_numbers():
    name = input("Please enter the name: ")
    for entry in Dict:
        if name == entry[0]:
            phone2 = input("Please enter the phone number: ")
            while check_number(phone2) != True:
                try:
                    phone2 = input("Please enter phone number again: ")
                except Exception:
                    print("something went wrong")
            add_values_in_dict(Dict[name], "phone", [phone2])
            print("\n{phone} has been added to the phonebook".format(
                phone=phone2))
            print(Dict)
            break
    else:
        print("Name not found")

# display all contacts


def all_values(dict_obj):
    ''' This function generates all values of
        a nested dictionary. 
    '''
    # Iterate over all values of the dictionary
    for key, value in dict_obj.items():
        # If value is of dictionary type then yield all values
        # in that nested dictionary
        if isinstance(value, dict):
            for v in all_values(value):
                yield v
        else:
            yield value


# show all contacts from level to dictionary
def show_all_contacts():
    count = 0
    for key, value in Dict.items():
        count += 1
        print(count)
        for key, value in value.items():
            print(key+": ", value)
