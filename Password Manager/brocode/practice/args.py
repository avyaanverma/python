# *args = parameter tat will pack all arguments into a tuple
# useful so that a function that can accept a varying amount of arguments 

def add(*stuff):
    sum=0
    stuff=list(stuff)
    for i in stuff:
        sum+=i
    return 0
print(add(1,2,3)) #This becomes unuseful


