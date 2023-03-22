import json, random, os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.json"), "r") as f:
    data = json.load(f)
    f.close()

def create_password():
    char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''
    for _ in range(25):
        random_char = random.choice(char_seq)
        password += random_char
    return password

def insert_password():
    site = input("Enter site for which you want password to be stored\n").lower()
    if site not in data.keys():
        data[site] = create_password()
        print("Success! Password for site", site, "created. Password is:", data[site])
    else:
        print("Site already found, no need for a new password!")
    json.dump(data, open("passwords.json",'w'))

def return_password():
    site = input("Enter site for which you want password for\n").lower()
    if site in data.keys():
        print("Password for", site, "is:", data[site])
    else:
        print("You do not have a password saved for this site!")

action = ''
while action != '-1':
    action = input("What do you want to do? (create/access)\nEnter -1 to exit\n").lower() # create -> new; access -> old
    if action == "create":
        insert_password()
    
    elif action == "access":
        return_password()
    
    elif action == '-1':
        print('quitting')
        quit()
    
    else:
        print("Invalid input")
   