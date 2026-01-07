import random

def play_game():
    # List of words
    word_list = ["python", "apple", "chair", "house", "plant"]

    # Choose a random word
    secret_word = random.choice(word_list)

    guessed_letters = []
    attempts = 6
    display_word = ["_"] * len(secret_word)

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses.\n")

    # Game loop
    while attempts > 0 and "_" in display_word:
        print("Word:", " ".join(display_word))
        print("Attempts left:", attempts)
        print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1:
            print("⚠️ Please enter only ONE letter.\n")
            continue

        if not guess.isalpha():
            print("⚠️ Please enter a LETTER (a–z only).\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct guess!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    # Game result
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("💀 Game Over! The word was:", secret_word)


# 🔁 Play again loop
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("👋 Thanks for playing Hangman!")
        break
