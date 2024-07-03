import random

def choose_random_word(words):
    """
    Select a random word from the provided list.
    
    Args:
        words (list): A list of words to choose from.
    
    Returns:
        str: A randomly chosen word from the list.
    """
    return random.choice(words)

def prompt_user_for_letter():
    """
    Prompt the user to enter a single letter and ensure it's a valid input.
    
    Returns:
        str: The valid letter input from the user.
    """
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            return guess
        else:
            print("Oops! That is not a valid input. Please enter a single alphabetical character.")

def main():
    """
    The main function to run the Hangman game.
    """
    # List of favorite fruits
    favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Choose a random word from the list
    chosen_word = choose_random_word(favorite_fruits)
    
    # Print the chosen word (for demonstration purposes)
    print(chosen_word)
    
    # Prompt the user to guess a letter
    user_guess = prompt_user_for_letter()

if __name__ == "__main__":
    main()
