import random

def play_game(score):
    print("\n🎮 Welcome to Hangman Game!")

    # Difficulty selection
    print("\nChoose Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        word_list = ["cat", "dog", "apple", "ball"]
        attempts = 8
        level = "Easy"
    elif choice == "2":
        word_list = ["python", "chair", "house", "plant"]
        attempts = 6
        level = "Medium"
    elif choice == "3":
        word_list = ["elephant", "computer", "programming"]
        attempts = 4
        level = "Hard"
    else:
        print("⚠️ Invalid choice. Defaulting to Medium.")
        word_list = ["python", "chair", "house", "plant"]
        attempts = 6
        level = "Medium"

    secret_word = random.choice(word_list)
    guessed_letters = []
    display_word = ["_"] * len(secret_word)

    print(f"\n🧠 Difficulty: {level}")
    print("Guess the word, one letter at a time.\n")

    # Game loop
    while attempts > 0 and "_" in display_word:
        print("Word:", " ".join(display_word))
        print("Attempts left:", attempts)
        print("Score:", score)
        print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1:
            print("⚠️ Enter only ONE letter.\n")
            continue
        if not guess.isalpha():
            print("⚠️ Letters only (a–z).\n")
            continue
        if guess in guessed_letters:
            print("⚠️ Already guessed.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong! (-2 points)\n")
            attempts -= 1
            score -= 2

    # Result
    if "_" not in display_word:
        print("🎉 You won! The word was:", secret_word)
        score += 10
        print("🏆 +10 points!")
    else:
        print("💀 Game Over! The word was:", secret_word)

    print("⭐ Current Score:", score)
    return score


# 🔁 Play again loop with score tracking
total_score = 0

while True:
    total_score = play_game(total_score)
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing!")
        print("🎯 Final Score:", total_score)
        break
