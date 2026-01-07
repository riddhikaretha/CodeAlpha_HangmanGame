import random

# Step 1: List of words
word_list = ["python", "apple", "chair", "house", "plant"]

# Step 2: Choose a random word
secret_word = random.choice(word_list)

# Step 3: Game variables
guessed_letters = []
attempts = 6

# Create display word with underscores
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Step 4: Game loop
while attempts > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        attempts -= 1

# Step 5: Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
