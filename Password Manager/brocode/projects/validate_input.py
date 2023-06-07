# validate user input exercise 
# 1. username is no more than 12 characters. 
# 2. username must not contain spaces
# 3. username must not contain digits
username= input("Enter any string that is your username: ")
if len(username)>12:
    print("username should be no more than 12 characters. ")
elif username.find(" ") != -1:
    print("username must not contain spaces")
# elif not username.find(" ")== -1:
elif username.isalpha() is False: 
    print("username must not contain digits")
    # elif not username.isalpha(): 
else: 
    print("Thank you for registering with Bellxploit!")
