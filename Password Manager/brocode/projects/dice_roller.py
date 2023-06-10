# Dice Roller Program
import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: (
"┌─────────┐",
"│         │",
"│    ●    │",
"│         │",
"└─────────┘",
    ),
    2: (
"┌─────────┐",
"│         │",
"│  ●   ●  │",
"│         │",
"└─────────┘",
    ),
    3: (
"┌─────────┐",
"│    ●    │",
"│         │",
"│  ●   ●  │",
"└─────────┘",
    ),
    4: (
"┌─────────┐",
"│ ●     ● │",
"│         │",
"│ ●     ● │",
"└─────────┘",
    ) ,
    5: (
"┌─────────┐",
"│ ●     ● │",
"│    ●    │",
"│ ●     ● │",
"└─────────┘",
    ) ,
    6: (
"┌─────────┐",
"│ ●    ●  │",
"│ ●    ●  │",
"│ ●    ●  │",
"└─────────┘",
    )
}
dice = []
total= 0
num_of_dice=int(input("How many dice number you want ? : "))

for die in range(1,num_of_dice+1):
    x=random.randint(1,6)
    dice.append(x)

# PRINTING THEM NORMALLY
for die in dice:
    for line in dice_art.get(die):
        print(line)
# PRINTING THE DICES  ON  A SINGLE LINE( HORIZONTALLY )
for x in range(0,5):
    for d in dice:
        print(dice_art[d][x], end="  ")
    print()

# dice_art[d][x]
# die_art [d2][x]
#
for die in dice :
    total+=die
print(f"total: {total}")