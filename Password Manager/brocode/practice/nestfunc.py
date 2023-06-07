#nested functions = function calls inside otherr function calls innermost functions calls are resolved first retruned value  is used as argument for the next outer function 

# num =input("Enter a whole positive no : ")
# num = float(num)
# num = abs(num)
# num =round(num)
# print(num)
print(round(abs(float(input("Enter the whole positive no : ")))))