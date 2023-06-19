def swap_case(s): 
    low="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    newstring=""
    for letter in s :
        if letter in low: newstring  += letter.upper()
        elif letter in upper: newstring += letter.lower()
        else: newstring+= letter
    print(newstring)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    # print(result)