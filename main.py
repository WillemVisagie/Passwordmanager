import json
import random
import os


passwords_file = "passwords.json"

if not os.path.isfile(passwords_file):
    with open(passwords_file, "w") as f:
        json.dump({}, f)

with open(passwords_file, "r") as f:
    data = json.load(f)


def create_password():
    char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''
    for _ in range(25):
        random_char = random.choice(char_seq)
        password += random_char
    return password


def insert_password():
    type_of_create = input(
        "Do you want to create a new password manually or automatically? (manual/auto)\n").lower()
    while type_of_create not in ["manual", "auto"]:
        print("Please enter a valid input\n")
        type_of_create = input(
            "Do you want to create a new password manually or automatically? (manual/auto)\n").lower()
    if type_of_create == "manual":
        site = input(
            "Enter site for which you want password to be stored\n").lower()
        if site not in data.keys():
            data[site] = input("Enter password for site\n")
            print("Success! Password for site", site,
                  "created. Password is:", data[site])
        else:
            print("Site already found, no need for a new password!")
    elif type_of_create == "auto":
        site = input(
            "Enter site for which you want password to be stored\n").lower()
        if site not in data.keys():
            data[site] = create_password()
            print("Success! Password for site", site,
                  "created. Password is:", data[site])
        else:
            print("Site already found, no need for a new password!")
    json.dump(data, open("passwords.json", 'w'))


def return_password():
    site = input("Enter site for which you want password for\n").lower()
    if site in data.keys():
        print("Password for", site, "is:", data[site])
    else:
        print("You do not have a password saved for this site!")


def update_password():
    site = input(
        "Enter site for which you want password to be updated\n").lower()
    if site not in data.keys():
        print(f"There is no password stored for {site}")
    else:
        type_of_update = input(
            "Do you want to update password manually or automatically? (manual/auto)\n").lower()
        while type_of_update not in ["manual", "auto"]:
            print("Please enter only manual or auto\n")
            type_of_update = input(
                "Do you want to update password manually or automatically? (manual/auto)\n").lower()
        if type_of_update == "manual":
            data[site] = input(f"Enter new password\n")
        else:
            data[site] = create_password()
        print(f"Succes, password for {site} updated to {data[site]}")
    json.dump(data, open("passwords.json", 'w'))


action = ' '
while action not in ['', "nothing"]:
    # create -> new; access -> old
    action = input(
        "What do you want to do? (create/access/update)\nEnter nothing to exit\n").lower()
    if action == "create":
        insert_password()

    elif action == "access":
        return_password()

    elif action == 'update':
        update_password()

    elif action in ['', "nothing"]:
        print('quitting')
        quit()

    else:
        print("Invalid input")
