import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Loading variables from .env
from dotenv import load_dotenv
load_dotenv()
p1=os.getenv('private_key_id')
p2=os.getenv('private_key')
p3=os.getenv('client_id')
u1=os.getenv('client_x509_cert_url')
u2=os.getenv('databaseURL')

# Creating a credentials object
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

# Initializing the app
firebase_admin.initialize_app(cred, {'databaseURL': u2})

ref = db.reference('py/')
users_ref = ref.child('users')
users_ref.set({
    'Allen': {
        'date_of_birth': 'September 26, 2000',
        'full_name': 'Allen Ben Philipose'
    },
    'Christi': {
        'date_of_birth': 'January 29, 2001',
        'full_name': 'Christiana John'
    },
    'Alvin': {
        'date_of_birth': 'January 16, 2004',
        'full_name': 'Alvin Ben',
        'nickname': 'Avin Boo'
    }
})

hopper_ref = users_ref.child('Christi')
hopper_ref.update({'nickname': 'Kishti Mol'})

handle = users_ref.child('py/users/Allen').get()
print(ref.get())