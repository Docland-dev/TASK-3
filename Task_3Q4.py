import re

password = input("Enter your password ")

p = True

while p:
    if (len(password)<8):
        print("Password must be a least 8 Characters")
        break
    elif not re.search ("[a-z]", password):
        print("Password must contain at least on lower case letter from a-z")
        break
    elif not re.search("[0-9]", password):
        print("Password must contain at least one number from 0-9")
        break
    elif not re.search("[A-Z]", password):
        print("Password must contain an uppercase letter from A-Z")
        break
    elif not re.search("[$#@_*^%!?~]", password):
        print("Password must contain atleast one special character")
        break
    elif re.search("\s", password):
        print("Password should not contain spaces")
        break
    else:
        print("Valid Password", password)
        p = False

if p:
    print("Password not valid")