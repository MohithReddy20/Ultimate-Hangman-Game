import time
import random

def display_hangman(turns_left):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[6 - turns_left]

def hangman_game():
    print("Welcome to Hangman!")
    time.sleep(1)
    name = input("Enter your name: ")
    print(f"Hello, {name}! Get ready to play Hangman!")
    time.sleep(1)
    print("Here's how it works: You have 6 attempts to guess the correct word.")
    time.sleep(1)

    word_list = [
        'expense', 'simultaneous', 'interceptor', 'gregarious', 
        'juxtaposed', 'ambivert', 'orifice', 'algebra', 
        'distortions', 'gynaecology', 'autonomous'
    ]
    word = random.choice(word_list)
    guesses = ''
    turns = 6

    print("\nLet's start guessing!\n")
    while turns > 0:
        failed = 0
        display_word = ''

        # Build display for the current word
        for char in word:
            if char in guesses:
                display_word += char
            else:
                display_word += '_'
                failed += 1

        # Display the current state of the game
        print(display_hangman(turns))
        print("Word:", ' '.join(display_word))

        if failed == 0:
            print(f"\nCongratulations, {name}! You've guessed the word correctly!")
            print("🎉 Here's your reward: 🏆 $1,000,000 🏆 🎉")
            break

        # Player guesses a letter
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guesses:
            print("You already guessed that letter. Try again!")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("\nWrong guess!")
            print(f"You have {turns} turns left.")
            if turns == 0:
                print(display_hangman(turns))
                print("You lose! The word was:", word)
                print("Better luck next time!")
                break
        else:
            print("\nGood guess!")

# Start the game
hangman_game()
