Num=[]
while True:
    input_values=int(input('Enter the numbers:'))
    Num.append(input_values)
    choice=input("Do you want to add more (y/n):")
    if choice=="n":
        break
print("The list genrated=",Num)
maximum_number=max(Num)
Num.remove(max(Num))
print("List after removing the maximum number:",Num)
second_largest=max(Num)
print("The second largest number in the list is:",second_largest)