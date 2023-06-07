# 1 inch = 2.54 cm 
# 1 m = 100 cm 
# 2.54 cm = 0.0254 m 
# 
# 0.394 inch = 1 cm 
# making program to convert units inch / cm / m / mm 
# author : @avyaanver
no =""
unit=""
unit2=""
def taking_input():
    no, unit = map(str, input("Enter the no and unit inch / cm / m / mm: "))
    no - int(no)
    unit2= int(input("You want to convert to ? inch / cm / m / mm : "))

taking_input()
if unit is unit2 : 
    print("The program can not run for same units \n Please enter units again. ")
    taking_input()
elif unit is "inch":
    no *= 0.0254 
elif unit is "cm":
    no *= 0.394
elif unit is "mm":
    no *= 0.0254 
elif unit is "m":
    no *= 0.0254 
else: 
    print("You have entered wrong input! \n Please check all of it again!")


