import verification as v
#logo display

#verification
invalid_login = True
while invalid_login:
    check_admin = input("Enter 1 for admin access, 2 for user access: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if check_admin == 1:
        if v.check(1, username, password):
            invalid_login = False
        #transfer access to admin file
        pass

    elif check_admin == 2:
        if v.check(2, username, password):
            invalid_login = False
        #transfer access to user file
        pass
    
    else:
        
