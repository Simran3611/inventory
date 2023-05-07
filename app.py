import pyrebase
# from firebase import firebase

#steps to install pyrebase 
#pip3 install --upgrade setuptools

# pip3 install --upgrade gcloud

# pip3 install pyrebase4
#  
firebaseConfig =  {
  "apiKey": "AIzaSyDlVlhetavbdVX4EBIzBPrHji0uT3fIBeA",
  "authDomain": "inventorydb-b0cee.firebaseapp.com",
  "projectId": "inventorydb-b0cee",
  "databaseURL": "https://inventorydb-b0cee-default-rtdb.firebaseio.com/",
  "storageBucket": "inventorydb-b0cee.appspot.com",
  "messagingSenderId": "155467399195",
  "appId": "1:155467399195:web:beae9ee6f69197d14bb8be",
  "measurementId": "G-VHXND08TDE"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()
# #connects to the firebase
# database = firebase.database()
# #configs the database

# data = {"Age": 21, "Name": "Jenna", "Employed": True}
# #-------------------------------------------------------------------------------
# # Creates data, go ahead and change the data to related data to inventory

# database.push(data)
# database.child("Users").child("FirstPerson").set(data)
# #pushes the data to the database
