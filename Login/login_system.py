print("Welcome to 1500 Harbor Login")

#login or sign up
def welcome():
    login_or_signup = input(print("Do you want to [L]ogin or [S]ign-up?")).lower()
    if login_or_signup == 'l':
        return login()
    elif login_or_signup == 's':
        return sign_up()

#initial signup function
def sign_up():
    print("Please enter username and password below")
    username = input(print("Input username here: "))
    password = input(print("Input password here: "))

    all_users = open("user_profiles.txt", "r")
    users_info = all_users.read()
    if username in users_info:
        print("Username already taken. Please try another name.")
    all_users.close()

    all_users = open("user_profiles.txt", "w")
    users_info = username + " " + password
    all_users.write(users_info)
    print("Welcome aboard " + username)

#login function
def login():
    print("Please enter username and password below")
    username = input(print("Input username here: "))
    password = input(print("Input password here: "))

    all_users = open("user_profiles.txt", "r")
    users_info = all_users.read()
    if username in users_info:
        index = users_info.index(username) + 1
        username_password = users_info[index]
        if username_password == password:
            print("Welcome Back! " + name)
        else:
            print("Password is incorrect.")
    else:
        print("Name not found. Please Sign Up")
    all_users.close()

welcome()



