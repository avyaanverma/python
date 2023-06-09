# os. system('cls' if os.name == 'nt' else 'clear')
import time

counter_time=int(input("Enter the Countdown limit ( in seconds ): "))
# for loop for countdown
for x in reversed(range(0,counter_time+1)):
    time.sleep(1)
    print(x)
