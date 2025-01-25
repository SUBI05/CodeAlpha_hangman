import random

# List of words for the game
words = ['python', 'programming', 'hangman', 'developer', 'challenge', 'computer', 'science', 'algorithm']

# Function to start the Hangman game
def hangman():
    # Select a random word from the list
    word = random.choice(words)
    word_length = len(word)
    
    # Create a list to represent the blanks in the word
    guessed_word = ['_'] * word_length
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit on incorrect guesses

    print("Welcome to Hangman!")
    print("You have to guess the word.")
    print("Word to guess: " + " ".join(guessed_word))
    print(f"You have {max_incorrect_guesses} incorrect guesses remaining.")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()

        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            # Update the guessed word with the correctly guessed letter
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")
        
        # Display the current state of the guessed word
        print("Current word: " + " ".join(guessed_word))

        # Check if the player has guessed the whole word
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word correctly.")
            break
    
    # If the player runs out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game Over! The word was: {word}")

# Start the Hangman game
if __name__ == "__main__":
    hangman()