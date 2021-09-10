# Authentication in Firebase

import os
import pyrebase
import firebase_admin 
from firebase_admin import db
from firebase_admin import credentials

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv() 
a1=os.getenv('apikey')
a2=os.getenv('appid')
u1=os.getenv('databaseURL')

# Creating credentials certificate for Authorization
cred = firebaseConfig = {
  'apiKey': a1,
  'authDomain': "learning-290101.firebaseapp.com",
  'databaseURL': u1,
  'projectId': "learning-290101",
  'storageBucket': "learning-290101.appspot.com",
  'messagingSenderId': "468456439571",
  'appId': a2,
  'measurementId': "G-LVMDKBV43W"
};


# Initializing the app with the certificate 
firebase = pyrebase.initialize_app(cred)
auth = firebase.auth()

# Connect to Resources
storage = firebase.storage()
db = firebase.database()

# Authenticating the user
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Valid Login")
    except: print("Invalid Login")
    exit()

# New user registration
def signup():
    email = input("Enter your email: ")
    password1 = input("Enter your password: ")
    #password2 = input("Confirm password: ")
    if(password1):#==password2):
        try:
            auth.create_user_with_email_and_password(email, password1)
            print("Valid Login")
        except Exception as e: print(e.values())
    else: print("Passwords don't match")

def main():
    print("\n1. Login")
    print("2. Signup")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1): login()
    elif(choice==2): signup()
    elif(choice==3): exit()
    else: print("Invalid choice")
    main()

if __name__ == "__main__": main()