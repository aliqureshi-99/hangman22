# Step 1: Import the random module
import random

# Step 2: Create a list containing the names of your 5 favorite fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 3: Assign this list to a variable called word_list
word_list = fruits

# Step 4: Use random.choice to select a random word from word_list
word = random.choice(word_list)

# Step 5: Print out the randomly selected word
print(word)

# Task 3: Taking User Input
# Step 1: Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Task 4: Validate User Input
# Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Step 2: Print a message that says "Good guess!"
    print("Good guess!")
else:
    # Step 3: Print "Oops! That is not a valid input." if the preceding conditions are not met
    print("Oops! That is not a valid input.")
