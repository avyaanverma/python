# exception = events detected during execution that interrupt the flow of a program
try :
    num = int(input("Enter a number to divide : "))
    den= int(input("Enter a number to  divide by : "))
    results = num/den
except ZeroDivisionError as e: # These are specific exceptions
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e :
    print(e)
    print("Please enter only numbers !!")
except  Exception as e: # it is not a good practice to handle all exceptions a single except block
    print(e)
    print("something went wrong :( ")
else:
    print(results," else statement")
finally:
    # if you open files you can close files here
    print("This will always execute at the end")
