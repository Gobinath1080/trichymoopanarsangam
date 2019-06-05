import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import sys

cred = credentials.Certificate("C:\\Projects\\trichymoopanarsangam\\mysite\\database.json")

# Initialize the app with a None auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://trichymoopanar.firebaseio.com/',
})
root = db.reference()
# Add a new user under /users.
new_user = root.child('users').push({
    'name' : 'Mary Anning', 
    'since' : 1700
})

two = root.get('users')
three = two
