
import random
import urllib.request

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()


wordToGuess = random.choice(words)
lettersGuessed = []
failureCount = 6

while failureCount > 0:
    guessed = input("Enter a letter: ")

    if guessed in wordToGuess:
        print("Correct!")
    else: 
        failureCount -= 1
        print("Incorrect.")

    lettersGuessed.append(guessed)
    wrongLetterCount = 0

    for letter in wordToGuess: 
        if letter in lettersGuessed:
            print(f"{letter} ", end="")
        else:
            print("__ ", end="")
            wrongLetterCount += 1
    print("")

    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {wordToGuess}. You won!")
        break
else: 
    print(f"You lose! The secret word was {wordToGuess}")