import random
import string

def generate_random_word(min_length=3, max_length=10):
    """Generates a random word with a random length."""
    length = random.randint(min_length, max_length)
    word = ''.join(random.choices(string.ascii_lowercase, k=length))
    return word

def display_hangman(turns_left, max_turns):
    """Displays the hangman based on remaining turns."""
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
    index = max(0, len(stages) - 1 - int((len(stages) - 1) * (turns_left / max_turns)))
    return stages[index]

def hangman_game():
    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's play a special version of Hangman!")
    
    # Generate a random word
    word = generate_random_word()
    max_turns = len(word) + 3  # Extra tries for longer words
    guesses = ''
    turns = max_turns

    print("\nGuess the random word!")
    print(f"The word has {len(word)} letters. You have {turns} tries.\n")

    while turns > 0:
        failed = 0
        display_word = ''

        # Build the current display of the word
        for char in word:
            if char in guesses:
                display_word += char
            else:
                display_word += '_'
                failed += 1

        print(display_hangman(turns, max_turns))
        print("Word:", ' '.join(display_word))

        if failed == 0:
            print(f"\n🎉 Congratulations, {name}! You guessed the word: {word}")
            print("Here's your virtual trophy 🏆!")
            break

        # Player makes a guess
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
            print(f"Remaining tries: {turns}")
            if turns == 0:
                print(display_hangman(turns, max_turns))
                print(f"You lose! The word was: {word}")
                break
        else:
            print("\nGood guess!")

# Start the game
hangman_game()
