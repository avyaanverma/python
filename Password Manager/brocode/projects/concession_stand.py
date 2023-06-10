# concession stand program
menu = {
    "pizza"   : 3.00,
    "nachos"  : 4.50,
    "chips"   : 1.00,
    "pretzel" : 3.50
}
cart=[]
total=0

for key,value in menu.items():
    print(f"{key:^30}:${value:.^2f}")
for x in range(50): print("-", end="")
print()
b="Select an item (q to quit)"
while True:
    food=input(f"{b:^50}").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
a="--------YOUR ORDER--------"
print(f"{a:^50}")
for food in cart:
    total += menu.get(food)
    print(f"{food:^5}", end=" ")
print()
x="Total is : "
print(f"{x:^50} ${total:.2f}")

