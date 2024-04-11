import verification as v
import user as u
import admin as a
import logo as l

#logo display
print(l.logo)

#verification
invalid_login = True
while invalid_login:
    check_admin = input("Enter 1 for admin access, 2 for user access, 3 for creating new admin, 4 for creating new user: ")
    if check_admin == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        admin_id = v.verify(1, username, password)
        if admin_id != -1:
            invalid_login = False
            curr_admin = a.Admin(admin_id)
            curr_admin.run()

    elif check_admin == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = v.verify(2, username, password)
        if user_id != -1:
            invalid_login = False
            curr_user = u.User(user_id)
            curr_user.run()

    elif check_admin == '3' or check_admin == '4':
        root_verify = input("Enter root password to continue: ")
        if root_verify == "toor":
            if check_admin == '3':
                new_username = input("Enter new admin username: ")
                new_password = input("Enter new admin password: ")
                if v.create(1, new_username, new_password) != -1:
                    print("Created new admin successfully!")
                
                else:
                    print("Admin already exists.")

            elif check_admin == '4':
                new_username = input("Enter new user username: ")
                new_password = input("Enter new user password: ")
                if v.create(2, new_username, new_password) != -1:
                    print("Created new user successfully!")

                else:
                    print("User already exists.")
        
        else:
            print("Wrong password entered. Please retry.")

    else:
        print("Invalid login. Please try again.")
