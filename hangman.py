import random

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

word_list = ['girrafe', 'cat', 'rabbit', 'monkey', 'pig']

word_to_guess = random.choice(word_list).lower()

lives = 6
word_to_display = ''

for letter in word_to_guess:
    word_to_display += '_'

def replace_letter_in_display_word(word_to_display, word_to_guess, guess_letter):
    new_word_to_display = ''

    for i in range(len(word_to_guess)):
        if word_to_guess[i] == guess_letter:
            new_word_to_display += guess_letter
        else:
            new_word_to_display += word_to_display[i]

    return new_word_to_display

while lives > 0:

    if(word_to_display == word_to_guess):
        print('You win! The word was: ' + word_to_guess)
        break

    print(f'Word to guess: {word_to_display}')
    guess_letter = input('Guess a letter: ').lower()

    if guess_letter in word_to_guess:
        if guess_letter in word_to_display:
            print(f"You've already guessess {guess_letter}")
        else:
            word_to_display = replace_letter_in_display_word(word_to_display, word_to_guess, guess_letter)
    else:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")

        if(lives == 0):
            print("***********************IT WAS nightclub! YOU LOSE**********************")

    print(HANGMAN_PICS[6-lives])
    print(f'** ** ** ** ** ** ** ** ** ** ** ** ** ** {lives} / 6 LIVES LEFT ** ** ** ** ** ** ** ** ** ** ** ** ** **')




