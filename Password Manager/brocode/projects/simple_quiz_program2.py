# Python quiz game
questions =("Are you over your ex? ","Do You Love Yourself?","Are You Satisfied with your Life?","Are You taking care of your Life?","Why don't you quit this game and start working? ")
# There is no correct answer
options=(
    ('A: Probably Not','B: She will come back','C: He/She comes in my dream so they never left','D: Of,Course'),
    ('A: Haan Bhai karte hi hain','B: There is nothing to love about me','C: Is option D is the correct answer everytime you ask yourself this question?','D: I will from now onwards'),
    ('A: Probably Not','B: I will Die so no point','C: Sometimes','D: Quite the Opposite'),
    ('A: Probably Not','B: I will Die so no point','C: Sometimes','D: Quite the Opposite'),
    ('A: Probably Not', 'B: I will Die so no point', 'C: Sometimes', 'D: Quite the Opposite')
)
answers=('C','D','A','B','A')
guesses=[]
score=0
i=0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[i]:
        print(option)
    guesses.append(input("Enter your answer from (A,B,C,D): "))
    if guesses[i]==answers[i]:
        print("CORRECT ANSWER")
        score+=1
    else:
        print("INCORRECT!!")
    i+=1
a=round(score/len(questions)*100)
print(f"You have scored {a:.0f}% ")



