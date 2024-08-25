import random

def hangman():
    # List of possible words
    words = ["apple", "banana", "grape", "orange", "watermelon", "strawberry"]
    
    # Randomly choose a word from the list
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print("Guess the word:")
    
    while attempts > 0 and "_" in guessed_word:
        print("Word to guess: ", " ".join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Check if letter is already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1
        
        print("\n")
    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

# Start the game
hangman()
