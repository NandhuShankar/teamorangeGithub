#Epic 1
#Developer 1: Aliana Palmer
#Developer 2: Nandhakumar Shankarkala

#import regex for password checking
import re
#User dictionary
database = {}

#log_or_sign asks the user of they want to log in or sign up, returns that decision
def log_or_sign():
    print("Welcome to InCollege's login page!\n")
    while True:
        desi = input("Would you like to log in or signup? (Type L or S:) ")
        if desi.lower() == "l":
            print("You are logging in.")
            return "l"
        elif desi.lower() == "s":
            print("You are signing up.....")
            return "s"
        else:
            print("Invalid input, try again\n")

#Signup page
def signup(users_dict):
    #check if max users have been created
    if len(users_dict)== 5:
        print("All permitted accounts have been created, please come back later")
        return False
    
    username = input("Enter a new username: ")
    # Check if the username is unique
    if username in users_dict:
        print("This username is already taken. Please try another.")
        return False

    password = input("Enter a new password: ")
    # Check if the password meets the criteria
    if not (8 <= len(password) <= 12 and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password) and
            re.search("[!@#$%^&*(),.?\":{}|<>]", password)):
        print("Password does not meet the criteria.")
        return False

    # If all checks pass, save the username and password
    users_dict[username] = password
    print("User created successfully.")
    return True

#login function
def login(user_dict):
    username = input("Enter username:")
    password = input("Enter password:")
    if username in user_dict:
        if user_dict[username] == password:
            print("You have successfully logged in! Taking to site....")
            return 1
    else:
        print("Incorrect login, try again.")
        return 0

#login page
def loginPage():
    while True:
        user_desi = log_or_sign()
        #Desision tree
        match user_desi:
            case "l":
                auth = login(database)
                if auth == 1:
                    return True
            case "s":
                signup(database)
            case _:
                print("You shouldnt see this")

def homePage():
    while True:
        print("INCOLLEGE HOME PAGE")
        print("1. Search for a job/internship")
        print("2. Find someone you know")
        print("3. Learn a new skill")
        option = int(input("Select an option :"))
        if (option <= 1) or (option >= 3):
            print("Invalid option try again")
            True
        else:
            return option

def jobSearch():
    print("SEARCH FOR A JOB/INTERNSHIP PAGE")
    print("Under construction")

def personSearch():
    print("FIND SOMEONE YOU KNOW PAGE")
    print("Under construction")

def skillSearch():
    while True:
        print("LEARN A NEW SKILL PAGE")
        print("Skill 1 - ")
        print("Skill 2 - ")
        print("Skill 3 - ")
        print("Skill 4 - ")
        print("Skill 5 - ")
        print("Enter 6 for Return to Main Page")
        option = int(input("Select a skill :"))
        if (option <= 1) or (option >= 5):
            print("Invalid option try again")
            True
        elif (option == 6):
            loginPage()
        else:
            match option:
                case 1:
                    print("Under construction")
                case 2:
                    print("Under construction")
                case 3:
                    print("Under construction")
                case 4:
                    print("Under construction")
                case 5:
                    print("Under construction")


#Main function
if loginPage():
    option = homePage()
    match option:
        case 1 : 
            jobSearch()
        case 2 : 
            personSearch()
        case 3 : 
            skillSearch()

    

            

