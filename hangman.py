import random

# List of 5 predefined words
words = ["python", "science", "gravity", "quantum", "physics"]

def display(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def hangman():
    word = random.choice(words)
    guessed = set()
    wrong = 0
    max_wrong = 6

    print("\n=== HANGMAN GAME ===")
    print(f"Guess the word! It has {len(word)} letters.")
    print("You have 6 chances for wrong guesses.\n")

    while wrong < max_wrong:
        print(f"Word:    {display(word, guessed)}")
        print(f"Wrong guesses left: {max_wrong - wrong}")
        if guessed:
            print(f"Letters tried: {', '.join(sorted(guessed))}")

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already tried that letter!")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"✓ '{guess}' is in the word!")
            if all(letter in guessed for letter in word):
                print(f"\n🎉 You won! The word was: {word}")
                return
        else:
            wrong += 1
            print(f"✗ '{guess}' is not in the word.")

    print(f"\n💀 Game over! The word was: {word}")

hangman()
