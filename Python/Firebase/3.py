import os
import firebase_admin 
from firebase_admin import firestore
from firebase_admin import db
from firebase_admin import credentials

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv() 
p1=os.getenv('private_key_id')
p2=os.getenv('private_key')
p3=os.getenv('client_id')
u1=os.getenv('client_x509_cert_url')
u2=os.getenv('databaseURL')

# Creating credentials certificate for Authorization
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "learning-290101",
    "private_key_id": p1,
    "private_key": p2,
    "client_email": "firebase-adminsdk-x0tar@learning-290101.iam.gserviceaccount.com",
    "client_id": p3,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": u1
})

# Initializing the app with the certificate and access URL
firebase_admin.initialize_app(cred)
db = firestore.client()

# CRUD Operations on DB                               --> Create, Read, Update, Delete

# Create                                              --> .add() or .set() command
C = {'name': 'Allen', 'age': 20}
db.collection('1').add(C)                             # Data added to a randomly generated ID in Collection 1
db.collection('2').document().set(C)                  # Data added to a randomly generated ID in Colection 2
db.collection('2').document('ID').set(C)              # Data added to a user defined ID in Collection 2
C = {'Address': 'Bangalore'}
db.collection('2').document('ID').set(C, merge=True)  # Data added to an existing document in Collection 2

# Read                                                --> .get() command
R = db.collection('2').document('ID').get()
print(R.to_dict())

'''                                                   --> Cloud Firestore rules in Firebase
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
'''