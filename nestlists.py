def inde(nam, scor):

    minscore = min(scor) # first min score
    minscore2 = minscore
    person = nam[scor.index(minscore)]
    print(minscore)
    a = person

    # removed the first one 
    nam.remove(person)
    scor.remove(minscore)
    
    minscore = min(scor) # second min score 

    a= nam[scor.index(minscore)] # second min score name 
    print("hello??")
    print(minscore, minscore2)
    nam.remove(a)
    scor.remove(minscore)
    minscore2 = min(scor)
    if minscore == minscore2:
        b= nam[scor.index(minscore)] # second min score if equal a = b
        print(a+"\n"+b)
    else :
        print(a)
if __name__ == '__main__':
    name= []
    score=[]
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    nam=name.copy()
    scor=score.copy()
    
    inde(nam,scor)   
    