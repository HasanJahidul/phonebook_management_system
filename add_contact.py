from menus import *
from phoneBook import *
from validation import *
import pickle as pickle
import pandas as pd

import json

# Creating an empty Dictionary
Dict = {}
phoneBook = {}
# add person to phonebook


def add_contact():
    # printing menu from menus.py
    add_person_menu()
    menu = input("Please enter a menu number: ")
    if menu == '1':
        # name validation
        name = input("Please enter the name: ")
        while check_name(name) != True:
            try:
                name = input("Please enter name number again: ")
            except Exception:
                print("something went wrong")
        # number validation
        phone = input("Please enter the phone number: ")
        while check_number(phone) != True:
            try:
                phone = input("Please enter phone number again: ")
            except Exception:
                print("something went wrong")
        address = input("Please enter the address: ")
        # address validation
        while address_validation(address) != True:
            try:
                address = input("Please enter address again: ")
            except Exception:
                print("something went wrong")

        email = input("Please enter the email: ")
        # email validation
        while email_validation(email) != True:
            try:
                email = input("Please enter email again: ")
            except Exception:
                print("something went wrong")
        # add to phonebook
        #phoneBook.append([name, phone, address, email])
        print("\n{name} has been added to the phonebook".format(name=name))
        # with open('Contacts.txt', 'w') as file:
        #     # use `json.loads` to do the reverse
        #     file.write(json.dumps(phoneBook))
        Dict = dict({name: {"name": name, "phone": [phone, ""],
                    "address": address, "email": email}})
        # print(Dict)
        # f = open("Contacts.txt","w")
        # f.write( str(Dict) )
        # f.close()
        # with open('myfile.txt', 'w') as f:
        #     print(Dict, file=f)

        # add multiple numbers
        while True:
            add_more = input("Would you like to add another number? (y/n): ")
            if add_more == 'y':
                phone2 = input("Please enter the phone number: ")
                while check_number(phone2) != True:
                    try:
                        phone2 = input("Please enter phone number again: ")
                    except Exception:
                        print("something went wrong")
                #Dict["phone"] = phone2
                add_values_in_dict(Dict, "phone", [phone2, ""])
                print("\n{phone} has been added to the phonebook".format(
                    phone=phone))
                print(Dict)
                # df = pd.DataFrame(Dict).T
                # df.fillna(0, inplace=True)
                # print(df)
                # for key, value in Dict.items():
                #     print(key+" : "+value+"\n")

            elif add_more == 'n':

                Dict = dict({name: {"name": name, "phone": [
                            phone], "address": address, "email": email}})
                print(Dict)
                df = pd.DataFrame(Dict).T
                df.fillna(1, inplace=True)
                print(df)
                # for key, value in Dict.items():
                #     print(key+" : "+value+"\n")
                break
            else:
                print("Invalid response")
                add_contact()

        #print("The entry has been added")
    elif menu == '2':
        main()
    else:
        print("Invalid menu number")
        add_contact()
# function to add multiple values


def add_values_in_dict(dic, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in dic:
        dic[key] = list()
    dic[key].extend(list_of_values)
    return dic
