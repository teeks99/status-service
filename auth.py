import json

users = {}

def check_auth(user, apikey):
    if not user in users:
        return False
    
    if not apikey in users[user]:
        return False
    
    return True

def load_from_file(file="auth_list.json"):
    with open(file, "r") as f:
        global users
        users = json.load(f)["users"]


# Load on first import or if it is manually called
load_from_file()