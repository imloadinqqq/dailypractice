import random

words = ["alex", "diaz", "hi", "hello"] 
guesses = 0
randomWord = random.choice(words)
hiddenWord = ["*" for _ in randomWord]


def hang():
    #letter = str(input("Please guess a letter: "))
    #if any(letter in word for word in words):
    #    print(f"Correct! The letter '{letter}' is in one of the words.")
    #else:
    #    print(f"Sorry, the letter '{letter}' is not in any of the words.")
    global guesses
    letter = input("Please guess a letter: ").lower()
    if letter in randomWord:
        print(f"Correct! The letter '{letter}' is in the word.")
        guesses += 1
        for i, char in enumerate(randomWord):
            if char == letter:
                hiddenWord[i] = letter
    else:
        print(f"Sorry, the letter '{letter}' is not in the word.")
        guesses += 1
    print(" ".join(hiddenWord))

def name():
    name = str(input("What is your name? "))
    print(f"Hello, {name}!")

def main():
    name()
    bestGuess = len(list(set(randomWord)))

    while "*" in hiddenWord:
        hang()
    print(f"Congratulations! You guessed the word: {randomWord} in {guesses} guesses")
    print(f"*Aim for {bestGuess} guesses*")

main()
