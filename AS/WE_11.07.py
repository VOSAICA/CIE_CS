import random
SecretNum = random.randint(0, 50)
GuessNum = 1
Guesses = int(input("Guess a number between 0 and 50: \n"))
while Guesses != SecretNum:
    if Guesses > SecretNum:
        print("Guess a smaller one")
    if Guesses < SecretNum:
        print("Guess a bigger one")
    Guesses = int(input())
    GuessNum += 1
print("bingo! You have guessed ", GuessNum, " times")
