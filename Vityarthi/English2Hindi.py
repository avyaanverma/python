
x, y = map(int, input("Enter 2 number with space: ").split())
greater=max(x,y)
while(True):
  if(greater%x==0 and greater%y==0):
    break
  greater+=1
print(greater)