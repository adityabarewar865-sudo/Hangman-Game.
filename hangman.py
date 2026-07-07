import random
from hangman_words import wordlist
from hangman_art import stages, logo

lives = 6 
print(logo)


chosen_word = random.choice(wordlist)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"**********{lives}/6 Lives Left**********")
    guess = input("Guess a letter:").lower()
    if guess in correct_letters:
        print(f"You have already guessed this letter {guess}. Please try again.")
    display = ""



    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"**********The Correct Word Was: {chosen_word} You Loose!!**********")

    if "_" not in display:
        game_over = True

        print("**********YOU WIN!!**********")

    print(stages[lives])




