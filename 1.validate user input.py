user = input("User_name:")

if len(user) > 12:
    print("username is not more the 12 char")
elif not user.find(" ") == -1:
    print("user name must not contain space")
elif not user.isalpha():
    print("username must not contain digit")
else:
    print("user name look ok")
