
from sre_constants import FAILURE


secret_word = "Hello"
lettersGuessed = ""

failureCount = 0

while failureCount < 6:

    guess = input("Enter Letter: ")

    if guess in secret_word:
        print(f"Correct! There is one or more {guess} in the secret word!")
    else: 
        failureCount += 1
        print(f"Incorrect! There is no {guess} in the secret word!")

    lettersGuessed = lettersGuessed + " " + guess
    wrongLetterCount = 0

    for letter in secret_word:
        if letter in lettersGuessed:
            print(f"{letter}", end ="")
        else:
            print("_", end ="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f"You won! The secret word was: {secret_word}")
        break
