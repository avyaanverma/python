#WAP to determine whether a number N is equal to the sum of its proper positive divisors (Excluding the no itself )
#Let us define proper divisors. A positive proper divisor is a positive divisor of a number, excluding itself. So, the proper divisors of a number which are even are the even proper divisors of the number.
# OUTPUT : print YES if N is equal to the sum of its proper postivvie divisors else print NO 
# 6 = 1+2+3
# TEST CASE : input a number of test case 
taran_tc=int(input("Test Case ")) # T : test case 
for i in range(0,taran_tc):#input loop
    taran_no=int(input("Number")) # N : no input taken
    i = 1 
    sum=0
    while(i<taran_no):
        if taran_no%i==0:
            sum+=i
        i+=1
    if sum==taran_no:
        print("YES")
    else: 
        print("NO")