from refactor import *
from menus import add_person_menu, update_menu, main_menu, thanks

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
        input_name(name)
        # number validation
        phone = input("Please enter the phone number: ")
        input_number(phone)
        address = input("Please enter the address: ")
        # address validation
        input_address(address)
        email = input("Please enter the email: ")
        # email validation
        input_email(email)
        # add to phonebook
        #phoneBook.append([name, phone, address, email])
        print("\n{name} has been added to the phonebook".format(name=name))
        # with open('Contacts.txt', 'w') as file:
        #     # use `json.loads` to do the reverse
        #     file.write(json.dumps(phoneBook))
        Dict[name] = dict({"name": name, "phone": [phone, ],
                           "address": address, "email": email})
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
                add_values_in_dict(Dict[name], "phone", [phone2])
                print("\n{phone} has been added to the phonebook".format(
                    phone=phone))
                break

            elif add_more == 'n':
                Dict[name] = dict(
                    {"name": name, "phone": [phone], "address": address, "email": email})
                break
            else:
                print("Invalid response")
                add_person_menu()

        #print("The entry has been added")
    elif menu == '2':
        main_menu()
        user_choice()
    else:
        print("Invalid menu number")
        add_person_menu()

# function to add multiple values


def add_values_in_dict(dic, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in dic:
        dic[key] = list()
    dic[key].extend(list_of_values)
    return dic


# update contact
def update_contact():
    search_key = input("Please enter the name: ")
    for key, value in Dict.items():
        if search_key.lower() == key.lower():
            print("Name:", value["name"])
            print("Phone:", value["phone"])
            print("Address:", value["address"])
            print("Email:", value["email"])
            update_menu()
            menu = input("Please enter a menu number: ")
            if menu == '1':
                # update name
                new_name = input("Please enter the updated name: ")
                if input_name(new_name) == True:
                    Dict[key]["name"] = new_name
                    print("Name updated")
                else:
                    print("Name not updated")
            elif menu == '2':
                # update phone
                phone = input("Please enter the phone number: ")
                if input_number(phone) == True:
                    Dict[search_key]["name"] = phone
                    print("Phone updated")
                else:
                    print("Phone not updated")
            elif menu == '3':
                # update address
                address = input("Please enter the address: ")
                if input_address(address) == True:
                    Dict[search_key]["address"] = address
                    print("Address updated")
                else:
                    print("Address not updated")
            elif menu == '4':
                # update email
                email = input("Please enter the email: ")
                if input_email(email) == True:
                    Dict[search_key]["email"] = email
                    print("Email updated")
                else:
                    print("Email not updated")
            elif menu == '5':
                # update multiple numbers
                add_more_numbers()
            elif menu == '6':
                break
            else:
                print("Invalid menu number")
                update_menu()
                update_contact()
            # print("\n{new_name} has been updated in the phonebook".format(
            #     name=new_name))
        else:
            print("Name not found")


# search an existing contact
def search():
    name = input("Please enter the name: ")
    for key, value in Dict.items():
        if name.lower() == key.lower():
            print("Name:", key)
            print("Phone:", value["phone"])
            print("Address:", value["address"])
            print("Email:", value["email"])
            break
    else:
        print("Name not found")

# remove contact


def remove_contact():
    name = input("Please enter the name: ")
    for key, value in Dict.items():
        if name.lower() == key.lower():
            del Dict[key]
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

# Show all contacts


def show_all_contacts():
    count = 0
    for key, value in Dict.items():
        count += 1
        print(count)
        for key, value in value.items():
            print(key+": ", value)
# export to txt file


def export_to_file():
    with open('Contacts.txt', 'w') as f:
        count = 0
        for key, value in Dict.items():
            count += 1
            print(str(count)+".", file=f)
            for key, value in value.items():
                print(key+": ", value, file=f)
    print("Contacts exported")

# user main menu input


def user_choice():
    menu = input("Please enter a menu number: ")
    while menu != '8':
        if menu == '1':
            add_contact()
        elif menu == '2':
            if check_empty_dict(Dict) == True:
                update_contact()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        elif menu == '3':
            if check_empty_dict(Dict) == True:
                remove_contact()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        elif menu == '4':
            if check_empty_dict(Dict) == True:
                remove_all_contacts()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        elif menu == '5':
            if check_empty_dict(Dict) == True:
                search()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        elif menu == '6':
            if check_empty_dict(Dict) == True:
                show_all_contacts()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        elif menu == '7':
            if check_empty_dict(Dict) == True:
                export_to_file()
            else:
                print("Phonebook is empty")
                main_menu()
                user_choice()
        else:
            print("Invalid menu number")
    thanks()
