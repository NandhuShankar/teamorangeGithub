"""
Epic 1 - Sprint 2
Developer 1: Nandhakumar Shankarkala
Developer 2: James Yab
Date: Feb 2, 2024
"""

# import regex for password checking
import re
from typing import Union, List, TypedDict
from viewImportantLinks import viewImportantLinks
# user settings for language and guest controls
import settings



# User dictionary
database = {}
#User class
class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
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
            case _:
                print("Invalid input, try again\n")


# Signup page
def signup(users_dict):
    # check if max users have been created
    if len(users_dict) == 5:
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
    # create new user
    users_dict[username] = User(username, password, first_name, last_name)
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
            case _:
                print("You shouldn't see this")


def homePage():
    while True:
        print("INCOLLEGE HOME PAGE")
        print("1. Search for a job/internship")
        print("2. Find someone you know")
        print("3. Learn a new skill")
        print("4. InCollege Important Links")
        option = int(input("Select an option :"))
        if (option < 1) or (option > 4):
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
                homePageOptions()
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
        if option == 6:
            homePageOptions()
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


def homePageOptions():
    option = homePage()
    match option:
        case 1:
            jobSearch()
        case 2:
            personSearch()
        case 3:
            skillSearch()


# Main function
AUTH = loginPage()

# if auth does not fail, then go to home page
if AUTH != 0:
    homePageOptions()
