user = []
adieu_line = "Adieu, adieu, to "
while True:
    try:
        user.append(input("Name: "))
    except EOFError:
        break

print(adieu_line+user[0])
for x in (1,len(user)-1):
    my_user = user[0:x]
    print(adieu_line, end="")
    for y in my_user:
        if my_user.index(y) > len(my_user)-2 :
            if my_user.index(y) == len(my_user)-1:
                print(y)
            else:
                print(y+" and ")




