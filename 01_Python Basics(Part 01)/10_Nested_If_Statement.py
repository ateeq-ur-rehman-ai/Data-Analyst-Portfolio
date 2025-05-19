'''
A nested if statement is one in which an if statement is nested inside another if statement.This is used when a variable must be processed more than once.
'''

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
