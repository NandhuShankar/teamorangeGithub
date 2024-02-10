#Epic 1
#Developer 1: Aliana Palmer
#Developer 2: Nandhakumar Shankarkala

#import regex for password checking
import re
from typing import Union, List, TypedDict

#User dictionary
database = {}

# array of dictionaries
class Posting(TypedDict):
    title: str
    description: str
    employer: str
    location: str
    salary: str
    posted_by: str

job_postings: List[Posting] = []

#log_or_sign asks the user of they want to log in or sign up, returns that decision
def log_or_sign():
    print("After graduating from college with a business degree, I was eager to start my career but struggling to "
          "land interviews. I heard about InCollege from a friend - it's an online platform that matches college "
          "students and grads with great companies and jobs. I created my profile and instantly had access to "
          "thousands of job openings at awesome companies. InCollege's matching technology suggested roles that "
          "aligned perfectly with my degree, skills, and interests.")

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

#login function returning a user_dict
def login(user_dict: dict) -> Union[dict, int]:
    username = input("Enter username:")
    password = input("Enter password:")
    if username in user_dict:
        if user_dict[username] == password:
            print("You have successfully logged in! Taking to site....")
            return user_dict
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
                if auth != 0:
                    return auth
            case "s":
                signup(database)
            case _:
                print("You shouldn't see this")


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


def jobSearch(authenticated_user: dict):
    while True:
        print("SEARCH FOR A JOB/INTERNSHIP PAGE")
        print("1. Post a Job");
        print("2. View Job Postings")
        print("3. Return to Main Page")
        option = int(input("Select an option: "))
        match option:
            case 1:
                if len(job_postings) < 5:
                    postJob(authenticated_user)
                else:
                    print("A maximum of 5 jobs have been posted in the system. Please choose another option.")
            case 2:
                # if not empty
                viewJob()
            case 3:
                homePageOptions(authenticated_user)
                break
            case _:
                print("Not an option")


def viewJob(authenticated_user):
    if len(job_postings) != 0:
        # print every job posting
        for i, job_posting in enumerate(job_postings):
            job_title = job_posting["title"]
            print(f"{i+1}. View \"{job_title}\"")

        return_option_val = len(job_postings) + 1;
        print(f"{return_option_val}. Return to home page")
        option = int(input("Choose which job posting to view: "))
        if option+1 == return_option_val:
            homePageOptions(authenticated_user)
            return

        curr_job_title = job_postings[option]
        print(f"Entering {curr_job_title}")

def personSearch():
    print("FIND SOMEONE YOU KNOW PAGE")
    print("Under construction")

def skillSearch(authenticated_user):
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
            homePageOptions(authenticated_user)
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

def postJob(authenticated_user: dict):
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

    for username, _ in authenticated_user.items():
        new_job_posting["posted_by"] = username

    job_postings.append(new_job_posting)
    print("The job has successfully posted\n")


def homePageOptions(authenticated_user: dict):
    option = homePage()
    match option:
        case 1:
            jobSearch(authenticated_user)
        case 2:
            personSearch()
        case 3:
            skillSearch(authenticated_user)

#Main function
auth = loginPage()

# if auth does not fail, then go to home page
if auth != 0:
    homePageOptions(auth)





