ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

in_usr, in_pass = input("Username: "), input("Password: ")
if in_usr == ADMIN_USERNAME and in_pass == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")