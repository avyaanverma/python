#scope = The region that a variable is recognized 
# A vairable is only available from inside the region it is created
# a global and locally scoped versions of a varaible can be created
# LEGB RULE = local enclosed gloabl built-in 
name = "Bell" #global scope (available inside & outside function)

def display_name():
    name = "xploit"
    print(name)

display_name()
print(name)
print(display_name())