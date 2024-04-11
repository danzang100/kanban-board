import json

with open("userData.json", "r") as userDataFile:
    userData = json.load(userDataFile)

admin_max_id = max(admin['id'] for admin in userData['admins'])
user_max_id = max(user['id'] for user in userData['users'])

def verify(access, username, password):
    if access == 1:
        for admin in userData["admins"]:
            if admin['username'] == username and admin['password'] == password:
                return admin['id']
        
        return -1
    
    else:
        for user in userData['users']:
            if user['username'] == username and user['password'] == password:
                return user['id']
            
        return -1
    
def create(access, username, password):
    if access == 1:
        for admin in userData["admins"]:
            if admin['username'] == username and admin['password'] == password:
                return -1
        
        userData["admins"].append({
            "id":str(admin_max_id+1),
            "username":username,
            "password":password
        })
        with open("userData.json", "w") as file:
            json.dump(userData, file)
        return admin_max_id+1
    
    if access == 2:
        for admin in userData["users"]:
            if admin['username'] == username and admin['password'] == password:
                return -1
        
        userData["users"].append({
            "id":admin_max_id+1,
            "username":username,
            "password":password
        })
        with open("userData.json", "w") as file:
            json.dump(userData, file)
        return admin_max_id+1
