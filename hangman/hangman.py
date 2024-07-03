import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with a list of words and number of lives.
        
        Args:
            word_list (list): A list of words to choose from.
            num_lives (int): The number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word.
        
        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts the user to enter a single letter and validates the input.
        """
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    Function to run the Hangman game.
    
    Args:
        word_list (list): List of words to choose from for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(f"The word to guess is: {' '.join(game.word_guessed)}")
        else:
            print("Congratulations! You won the game!")
            break

# Example usage
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    play_game(word_list)
