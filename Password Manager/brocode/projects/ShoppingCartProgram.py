# Shopping Cart Program

food = []
price = []
while True:
    food.append(input("Enter the food items( press x to stop ): "))
    if food.count('x') != 0:
        food.remove('x')
        break
    else:
        price.append(int(input('Enter the price( press x to stop ): Rs. ')))
price_sum=0
i=0

print("YOUR CART SHOWS".center(50,'-'))
for x in food:
    print(x)
    price_sum += price[i]

print(f"The price of food items are : {price_sum:,}")
