import os
import pyrebase
import requests
import firebase_admin 
from firebase_admin import db
from firebase_admin import credentials

# Load variables from .env
from dotenv import load_dotenv
load_dotenv() 
a1=os.getenv('apikey')
a2=os.getenv('appid')
u1=os.getenv('databaseURL')

# Configure app and database
cred = {
    'apiKey': a1,
    'authDomain': "learning-290101.firebaseapp.com",
    'databaseURL': u1,
    'projectId': "learning-290101",
    'storageBucket': "learning-290101.appspot.com",
    'messagingSenderId': "468456439571",
    'appId': a2,
    'measurementId': "G-LVMDKBV43W"
};

firebase = pyrebase.initialize_app(cred)            # Initialize app with config file
auth = firebase.auth()                              # Authenticate the program     
storage = firebase.storage()                        # Connect to Storage
db = firebase.database()                            # Connect to Database

def login():                                        # Authenticate existing user
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        # User input verified from Firebase
        a = auth.sign_in_with_email_and_password(email, password)
        print("Valid Login")
    except: print("Invalid Login")
    print("ID:",auth.get_account_info(a['idToken'])['users'][0]['localId'])

def signup():                                       # Register new user 
    email = input("Enter your email: ")
    password1 = input("Enter your password: ")
    password2 = input("Confirm password: ")
    if(password1==password2):                       # Check if passwords match
        try:
            # User input added to Firebase
            a = auth.create_user_with_email_and_password(email, password1)
            print("Signup complete")
            print("ID:",auth.get_account_info(a['idToken'])['users'][0]['localId'])
        except Exception as e: print(e)             # Error handling
    else: print("Passwords don't match")

def main():                                         # Menu driven approach
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if(choice=='1'): login()
    elif(choice=='2'): signup()
    elif(choice=='3'): exit()
    else: print("Invalid choice")
    main()                                          # Recursive loop

if __name__ == "__main__": main()