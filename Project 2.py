# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.
"""
import random


class guessGame:
    def __init__(self, n, rn, i = 0):
        self.n = n
        self.rn = rn
        self.i = i

    def GuessCounter(self):
        self.i = self.i+1

    def equalCheck(self):
        return f"You got the number it is {self.rn}, guess : {self.i}"

    def HighLowCheck(self):
        if self.rn > self.n:
            return "higher number please"
        elif self.rn < self.n:
            return "lower number please"
        else:
            self.equalCheck()


val = random.randint(0,100)

while True:
    inp = int(input("Your Guess: "))
    game = guessGame(inp,val)
    game.GuessCounter()
    print(game.HighLowCheck())
game.equalCheck()
"""
"""
import random
val = int(random.randint(0,100))
i = 0

while True:
    inp = int(input("Your Guess: "))
    i = i+1
    if val > inp:
        print("higher number please")
    elif val < inp:
        print("lower number please")
    else:
        break

print(f"Correct, you got the number, it was {val}, it took you {i} guesses")
"""
