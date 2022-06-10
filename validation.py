
# number validation
def check_number(number):
    if len(number) != 11 or number.strip().isdigit() == False:
        print("\n{num} is not a valid number" .format(num=number))
    else:
        return True

# name validation


def check_name(name):
    if len(name) < 3 or name.strip().isalpha() == False:
        print("\n{name} is an unaccepted response".format(name=name))
    else:
        return True

# email validation


def email_validation(email):
    if email.count('@') != 1 or email.count('.') != 1:
        print("\n{email} is an unaccepted response".format(email=email))
    if email.count('@') == 1 and email.count('.') == 1:
        return True

# address validation


def address_validation(address):
    if len(address) < 3 or address.strip().isalpha() == False:
        print("\n{address} is an unaccepted response".format(address=address))
    else:
        return True


