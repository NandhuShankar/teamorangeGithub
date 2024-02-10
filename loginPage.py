#Epic 1
#Developer 1: Aliana Palmer
#Developer 2: Nandhakumar Shankarkala

#import regex for password checking
import re
#User class
class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

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

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    #create new user
    users_dict[username] = User(username, password, first_name, last_name)
    print("User created successfully.")
    return True

#login function
def login(user_dict):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_dict and user_dict[username].password == password:
        print(f"You have successfully logged in! Welcome, {user_dict[username].first_name}!")
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
        if (option < 1) or (option > 3):
            print("Invalid option try again")
            True
        else:
            return option

def jobSearch():
    print("SEARCH FOR A JOB/INTERNSHIP PAGE")
    print("Under construction")

def personSearch():
    print("FIND SOMEONE YOU KNOW PAGE")
    
    # Prompt for the first name and last name
    search_first_name = input("Enter the first name of the person you're looking for: ")
    search_last_name = input("Enter the last name of the person you're looking for: ")
    
    # Search through the database
    found = False  # Flag to keep track if user is found
    for user in database.values():
        if user.first_name == search_first_name and user.last_name == search_last_name:
            found = True
            break

    if found:
        print("They are a part of the InCollege system.")
    else:
        print("They are not yet a part of the InCollege system yet.")
    homePageOptions()

def skillSearch():
    while True:
        print("LEARN A NEW SKILL PAGE")
        print("Skill 1 - Learn 3D Printing")
        print("Skill 2 - Learn Data Structures")
        print("Skill 3 - Learn Analysis of Algoritms")
        print("Skill 4 - Learn Databas Design")
        print("Skill 5 - Learn Architecture")
        print("Enter 6 for Return to Main Page")
        option = int(input("Select a skill :"))
        if (option == 6):
            homePageOptions()
        elif (option < 1) or (option > 5):
            print("Invalid option try again")
            True
        else:
            match option:
                case 1:
                    print("Under construction")
                    break;
                case 2:
                    print("Under construction")
                    break;
                case 3:
                    print("Under construction")
                    break;
                case 4:
                    print("Under construction")
                    break;
                case 5:
                    print("Under construction")
                    break;

def homePageOptions():
    option = homePage()
    match option:
        case 1 : 
            jobSearch()
        case 2 : 
            personSearch()
        case 3 : 
            skillSearch()
            
#Main function
if loginPage():
    homePageOptions()

    

            

