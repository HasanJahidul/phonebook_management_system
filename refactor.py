from pickle import TRUE
from validation import *


def input_name(name):
    while check_name(name) != True:
        try:
            name = input("Please enter name number again: ")
        except Exception:
            print("something went wrong")
    return True
def input_number(phone):
    while check_number(phone) != True:
        try:
            phone = input("Please enter phone number again: ")
        except Exception:
            print("something went wrong")

def input_address(address):
    while address_validation(address) != True:
        try:
            address = input("Please enter address again: ")
        except Exception:
            print("something went wrong")

def input_email(email):
    while email_validation(email) != True:
        try:
            email = input("Please enter email again: ")
        except Exception:
            print("something went wrong")
