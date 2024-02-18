import settings
from loginPage import AUTH, loginPage, homePageOptions





def printCopyrightNotice():
    print("Copyright © InCollege, 2023. All rights reserved.")
    print("Contents of InCollege, including but not limited to, "
          "text content, logos, brand names, images, video, and "
          "other media are the property of InCollege and are protected by copyright.")


def printAbout():
    print("InCollege is a social media platform designed to help people network, "
          "learn new skills, and find job opportunities.")

def printAccessibility():
    print("InCollege is committed to making its website accessible to individuals with disabilities. "
          "We are continually working to comply with the Web Content Accessibility Guidelines. "
          "If you need assistance using our website or have concerns about accessibility, please contact us.")

def printUserAgreement():
    print("InCollege User Agreement")
    print("Last revised: Feb 16, 2023")
    print("This User Agreement and your conduct make sure to follow the guidelines.")
    print("1. You agree to only use the platform for legal purposes.")
    print("2. You agree to not use the platform to harm others.")
    print("3. You agree to not use the platform to spam.")

def printPrivacyPolicy():
    print("InCollege Privacy Policy")
    print("Last revised: Feb 16, 2023")
    print("This Privacy Policy describes how your information is collected, used, and shared when you use InCollege.")
    print("1. We only collect the information you choose to give us, and we process it with your consent, or on another legal basis.")
    print("2. We only require the minimum amount of personal information necessary to fulfill the purpose of your interaction with us.")

def printCookiePolicy():
    print("InCollege Cookie Policy")
    print("Last revised: Feb 16, 2023")
    print("This Cookie Policy describes how InCollege uses cookies and similar technologies to provide, improve, promote, and protect the InCollege Services.")
    print("1. We use cookies to help personalize your InCollege experience.")
    print("2. We use cookies to understand how you use InCollege.")

def printBrandPolicy():
    print("InCollege Brand Policy")
    print("Last revised: Feb 16, 2023")
    print("This Brand Policy describes how you can and cannot use InCollege’s brand assets.")
    print("1. You may use the InCollege brand assets when you are promoting your InCollege profile.")

def switchLanguages():
    while True:
        print("Language options")
        print(f"Current language: {settings.GLOBAL_LANGUAGE}")
        print("1. English")
        print("2. Spanish")
        match int(input("Select a language: ")):
            case 1:
                print("Language set to English")
                settings.GLOBAL_LANGUAGE = "English"
                break
            case 2:
                print("Language set to Spanish")
                settings.GLOBAL_LANGUAGE = "Spanish"
                break
            case _:
                print("Invalid input")
                continue


def viewGuestControls():
    while True:
        email = printToggle(settings.GUEST_CONTROLS['Email'])
        sms = printToggle(settings.GUEST_CONTROLS['SMS'])
        ads = printToggle(settings.GUEST_CONTROLS['Targeted Ads'])

        print("InCollege Guest Controls")
        print(f"1. {email} - Email")
        print(f"2. {sms} - sms")
        print(f"3. {ads} - targeted ads")
        print(f"4. Return to Important Links")
        try:
            option = int(input("Select an option to toggle on/off: "))
            match option:
                case 1:
                    settings.GUEST_CONTROLS['Email'] = not settings.GUEST_CONTROLS['Email']
                case 2:
                    settings.GUEST_CONTROLS['SMS'] = not settings.GUEST_CONTROLS['SMS']
                case 3:
                    settings.GUEST_CONTROLS['Targeted Ads'] = not settings.GUEST_CONTROLS['Targeted Ads']
                case 4:
                    viewImportantLinks()
                    break
                case _:
                    print("Not an option")
                    continue
        except ValueError:
            print("Invalid input")
            continue

def printToggle(guestControl: bool) -> str:
    if guestControl:
        return "ON"
    else:
        return "OFF"
