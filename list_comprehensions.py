if __name__ == '__main__':
    x = int(input()) # i can be 0 to x
    y = int(input()) # j can be 0 to y 
    z = int(input()) # k can be 0 to z 
    n = int(input()) #    
    # print a list of all possible coordinates 
    # condition : i + j + k != n 
    
    # use list comprehensions rather than multiple loops
    
    # newlist = [expression for item in iterable if condition == True]
    
    perm_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(perm_list)
