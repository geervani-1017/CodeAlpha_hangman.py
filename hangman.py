import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

print("=" * 40)
print("        WELCOME TO HANGMAN GAME")
print("=" * 40)

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the complete word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# If player uses all attempts
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")