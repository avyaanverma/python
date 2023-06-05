# task is find out if the string S contains alphanumeric,digits,alphabet, lowercase, uppercase 
#My Method
while(True):
    S=input("single line containing S string ")
    if(0<len(S)<1000):
        break
alphanumeric="123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxy"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in S:
    for b in alphanumeric:
        if i==b:
            print(True)
            break
    else:
        continue
    break       
else:
        print(False)
    
for i in S:
    for b in alphabet:
        if i==b:
            print(True)
            break
        else:
            continue
    break    
else:
        print(False)

for x in S:
    for c in digits:
        if i==b:
            print(True)
            break
        else:
            continue
    break
else:
        print(False)

for i in S:
    for b in lowercase:
        if i==b:
            print(True)
            break
        else:
            continue
    break
else:
        print(False)
        
for x in S:
    for c in uppercase:
        if i==b:
            print(True)
            break
        else:
            continue
    break
else:
        print(False)

