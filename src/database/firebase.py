import firebase_admin
from firebase_admin import credentials, firestore

#Initialize Firebase with your service account credentials
cred = credentials.Certificate('ServiceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


#Function to store user data
def store_user_data(user_id, user_data):
    try:
        db.collection('users').document(user_id).set(user_data)
        print(f"User {user_id} added successfully")

    except Exception as e:
        print(f"A error occurred: {e}")

#Function to modify user data
def modify_user_data(user_id, user_data):
    try:
        db.collection('users').document(user_id).update(user_data)
        print(f"User {user_id} updated successfully")
    
    except Exception as e:
        print(f"A error occurred: {e}")

#Function to delete user data
def delete_user_data(user_id):
    try:
        db.collection('users').document(user_id).delete()
        print(f"User {user_id} deleted successfully")
    
    except Exception as e:
        print(f"A error occurred: {e}")

#Function to read user data
def read_user_data(user_id):
    try:
        user = db.collection('users').document(user_id).get()
        if user.exists:
            print(f"User data: {user.to_dict()}")
        else:
            print(f"User {user_id} does not exist")
    
    except Exception as e:
        print(f"A error occurred: {e}")



delete_user_data("123")