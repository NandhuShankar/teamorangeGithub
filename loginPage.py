"""
Epic 3
Developer 1: Mihir Karnani
Developer 2: Abylkhair Zholdybay
"""

# import regex for password checking
import re
from typing import Union, List, TypedDict
import importantLinks

# User dictionary
database = {}
#User class
class User:
    def __init__(self, username, password, first_name, last_name, major, university):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.university = university


# authenticated user
AUTH = {}


# type hinting for a job posting
class Posting(TypedDict):
    title: str
    description: str
    employer: str
    location: str
    salary: str
    posted_by: str


# array of postings
JOB_POSTINGS: List[Posting] = []


# log_or_sign asks the user of they want to log in or sign up, returns that decision
def log_or_sign() -> int:
    print("Welcome to InCollege's login page!\n")
    while True:
        print("1. Log in")
        print("2. Sign up")
        print("3. View success stories")
        print("4. View important links")
        print("5. View useful links")
        option = int(input("Please select one of the following options:"))
        match option:
            case 1:
                print("You are logging in.")
                return 1
            case 2:
                print("You are signing up.....")
                return 2
            case 3:
                print("You are viewing success stories.")
                return 3
            case 4:
                print("You are viewing important links.")
                return 4
            case 5:
                print("You are viewing useful links.")
                return 5
            case _:
                print("Invalid input, try again\n")


# Signup page
def signup(users_dict):
    # check if max users have been created
    if len(users_dict) == 10:
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
    major = input("Enter your major: ")
    university = input("Enter your university: ")
    # create new user
    users_dict[username] = User(username, password, first_name, last_name, major, university)
    print("User created successfully.")
    return True


# login function returning a user_dict or 0
def login(user_dict: dict) -> Union[dict, int]:
    username = input("Enter username:")
    password = input("Enter password:")
    if username in user_dict and user_dict[username].password == password:
        print(f"You have successfully logged in! Welcome, {user_dict[username].first_name}!")
        return user_dict
    else:
        print("Incorrect login, try again.")
        return 0


def viewSuccessStory():
    print("After graduating from college with a business degree, I was eager to start my career but struggling to "
          "land interviews. I heard about InCollege from a friend - it's an online platform that matches college "
          "students and grads with great companies and jobs. I created my profile and instantly had access to "
          "thousands of job openings at awesome companies. InCollege's matching technology suggested roles that "
          "aligned perfectly with my degree, skills, and interests.")
    option = input("Play video or Return to main page? (Type P or R:) ")
    if option.lower() == "p":
        print("Video is now playing")
    elif option.lower() == "r":
        print("Returning to main page...")
    else:
        print("Invalid input, returning to login page...")
        return


# login page
def loginPage():
    while True:
        user_desi = log_or_sign()
        # Decision tree
        match user_desi:
            case 1:
                auth = login(database)
                if auth != 0:
                    return auth
            case 2:
                signup(database)
            case 3:
                viewSuccessStory()
            case 4: 
                viewImportantLinks()
            case 5:
                viewUsefulLinks()
            case _:
                print("You shouldn't see this")


def homePage():
    while True:
        print("INCOLLEGE HOME PAGE")
        print("1. Search for a job/internship")
        print("2. Find someone you know")
        print("3. Learn a new skill")
        print("4. InCollege Important Links")
        print("5. InCollege Useful Links")
        option = int(input("Select an option :"))
        if (option < 1) or (option > 5):
            print("Invalid option try again")
        else:
            return option


def jobSearch():
    while True:
        print("SEARCH FOR A JOB/INTERNSHIP PAGE")
        print("1. Post a Job")
        print("2. View Job Postings")
        print("3. Return to Main Page")
        option = int(input("Select an option: "))
        match option:
            case 1:
                if len(JOB_POSTINGS) < 5:
                    postJob()
                else:
                    print("A maximum of 5 jobs have been posted in the system. Please choose another option.")
            case 2:
                # if not empty
                viewJob()
            case 3:
                break
            case _:
                print("Not an option")


def viewJob():
    while True:
        if len(JOB_POSTINGS) == 0:
            print("No job postings available\n")
            break
        if len(JOB_POSTINGS) != 0:
            # print every job posting
            print("Job Postings:")
            for i, job_posting in enumerate(JOB_POSTINGS):
                job_title = job_posting["title"]
                print(f"{i + 1}. View \"{job_title}\"")

            # return option depends on how many job postings
            return_option_val = len(JOB_POSTINGS) + 1
            print(f"{return_option_val}. Return to home page")
            option = int(input("Choose an option: "))

            if option == return_option_val:
                print("\n")
                break
            elif option < 1 or option > return_option_val:
                print("That is not an option")
                print("\n")
            else:
                curr_job_title = JOB_POSTINGS[option-1]
                print(f"Entering {curr_job_title.get('title')} job posting..")

    # if broke while True
    homePageOptions()


"""
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
"""


def personSearch():
    print("FIND SOMEONE YOU KNOW PAGE")

    search_option = int(input("Search by:\n1. Last Name\n2. University\n3. Major\nEnter option (1, 2, or 3): "))

    if search_option == 1:
        search_last_name = input("Enter the last name of the person you're looking for: ")
        search_results = search_students_by_last_name(search_last_name)
    elif search_option == 2:
        search_university = input("Enter the university of the person you're looking for: ")
        search_results = search_students_by_university(search_university)
    elif search_option == 3:
        search_major = input("Enter the major of the person you're looking for: ")
        search_results = search_students_by_major(search_major)
    else:
        print("Invalid option. Returning to the main page.")
        return

    if search_results:
        print("Search results:")
        for result in search_results:
            print(f"{result.first_name} {result.last_name} - {result.major} at {result.university}")
    else:
        print("No matching results found.")


def search_students_by_last_name(last_name):
    found_students = []
    for user in database.values():
        if user.last_name.lower() == last_name.lower():
            found_students.append(user)
    return found_students


def search_students_by_university(university):
    found_students = []
    for user in database.values():
        if hasattr(user, 'university') and user.university.lower() == university.lower():
            found_students.append(user)
    return found_students


def search_students_by_major(major):
    found_students = []
    for user in database.values():
        if hasattr(user, 'major') and user.major.lower() == major.lower():
            found_students.append(user)
    return found_students


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
        if option == 6:
            break
        elif (option < 1) or (option > 5):
            print("Invalid option try again")
        else:
            match option:
                case 1:
                    print("Under construction")
                    break
                case 2:
                    print("Under construction")
                    break
                case 3:
                    print("Under construction")
                    break
                case 4:
                    print("Under construction")
                    break
                case 5:
                    print("Under construction")
                    break


def postJob():
    title = input("Job Title: ")
    description = input("Job Description: ")
    employer = input("Employer: ")
    location = input("Location: ")
    salary = input("Salary: $")

    new_job_posting = {
        "title": title,
        "description": description,
        "employer": employer,
        "location": location,
        "salary": salary
    }

    for username, _ in AUTH.items():
        new_job_posting["posted_by"] = username

    JOB_POSTINGS.append(new_job_posting)
    print("The job has successfully posted\n")


def viewUsefulLinks(): 
    while True: 
        print("INCOLLEGE USEFUL LINKS")
        print("1. General")
        print("2. Browse InCollege")
        print("3. Business Solutions")
        print("4. Directories")
        print("5. Return to previous page")
        option = int(input("Select an option: "))
        match option:
            case 1:
                viewGeneralLinks()
            case 2:
                print("Under construction")
            case 3:
                print("Under construction")
            case 4:
                print("Under construction")
            case 5:
                return
            case _:
                print("Not an option")

def viewGeneralLinks():
    while True:
        print("GENERAL LINKS")
        print("1. Sign Up")
        print("2. Help Center")
        print("3. About")
        print("4. Press")
        print("5. Blog")
        print("6. Careers")
        print("7. Developers")
        print("8. Return to previous page")
        option = int(input("Choose an option: "))
        match option:
            case 1:
                signup(database)
            case 2:
                print("We're here to help")
            case 3:
                print("In College: Welcome to In College, the world's largest college student"
                      "network with many users in many countries and territories worldwide")
            case 4:
                print("In College Pressroom: Stay on top of the latest news, updates, and reports")
            case 5:
                print("Under construction")
            case 6:
                print("Under construction")
            case 7:
                print("Under construction")
            case 8:
                return

            case _:
                print("Not an option")

def viewImportantLinks():
    while True:
        print("INCOLLEGE IMPORTANT LINKS")
        print("1. Copyright Notice")
        print("2. About")
        print("3. Accessibility")
        print("4. User Agreement")
        print("5. Privacy Policy")
        print("6. Cookie Policy")
        print("7. Brand Policy")
        print("8. Guest Controls")
        print("9. Languages")
        print("10. Return to Home Page")
        option = int(input("Select an option: "))
        match option:
            case 1:
                importantLinks.printCopyrightNotice()
            case 2:
                importantLinks.printAbout()
            case 3:
                importantLinks.printAccessibility()
            case 4:
                importantLinks.printUserAgreement()
            case 5:
                importantLinks.printPrivacyPolicy()
            case 6:
                importantLinks.printCookiePolicy()
            case 7:
                importantLinks.printBrandPolicy()
            case 8:
                importantLinks.viewGuestControls()
            case 9:
                importantLinks.switchLanguages()
            case 10:
                print("Returning to Home Page")
                return

            case _:
                print("Not an option")
                continue
def homePageOptions():
    option = homePage()
    match option:
        case 1:
            jobSearch()
        case 2:
            personSearch()
        case 3:
            skillSearch()
        case 4:
            viewImportantLinks()
        case 5:
            viewUsefulLinks()


# Main function
AUTH = loginPage()

# if auth does not fail, then go to home page
while AUTH != 0:
    homePageOptions()
