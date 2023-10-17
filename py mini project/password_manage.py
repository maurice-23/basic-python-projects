from cryptography.fernet import Fernet

master_password = input("Enter a master password: ")
def view():
    with open('password.txt', 'r') as f: 
        for x in f.readlines():
            # print(x.rstrip())
            user, pswd = x.split("|")
            print("Username: ", user, "\n Password: ", pswd)
def add():
    username = input("Enter your name: ")
    psw = input("Enter password to use: ")
    with open('password.txt', 'a') as f:
        f.write(username + " | " + psw + "\n")
while True:
    
    mode = input("would like to add new password or want to view the current password (view, add)? to exit type (q)  ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option")
        continue