import random


guessed_letters = []
guess_counter = 8


def word_get(file, mode="NONE"):
    with open(file) as working_file:
        word_string = working_file.read()
    word_list = word_string.split()
    word = random.choice(word_list)
    if mode == "EASY":
        while len(word) > 6 or len(word) < 4:
            word = random.choice(word_list)
    if mode == "MEDIUM":
        while len(word) > 10 or len(word) < 6:
            word = random.choice(word_list)
    if mode == "HARD":
        while len(word) < 11:
            word = random.choice(word_list)
    word = word.upper()
    return word


def introduction():
    """Just a way of giving the player an introduction to the games and it's
    rules."""
    with open('mystery_word_ascii.txt') as art_file:
        word_art = art_file.read().ljust(10)
        print(word_art)
    print("""
          Welcome to Mystery Word! In this game you will attempt to guess
          a mystery word (isn't that kind of obvious?). However, you will be
          guessing it one letter at a time. If you guess the wrong letter
          eight times you will lose the game, so choose wisely! Please guess
          only one letter at a time. Good luck!
          """)


def graphic_generation(word, guessed_list=[]):
    graphic_list = []
    for letter in word:
        if letter in guessed_list:
            graphic_list.append(letter)
        else:
            graphic_list.append("_")
    graphic = "".join(graphic_list)
    print(graphic)
    return graphic


def letter_input():
    unfinished_letter = input("Please provide a letter you'd like to guess: ")
    letter = unfinished_letter.upper()
    if letter in guessed_letters:
        print("You already guessed that letter, please try again.")
        letter_input()
    elif letter == "":
        print("You entered nothing, please try again.")
        letter_input()
    elif len(letter) > 1:
        print("You entered more than one letter, please try again.")
        letter_input()
    elif not letter.isalpha():
        print("You entered a number, please try again.")
        letter_input()
    else:
        print("You entered {}".format(letter))
        return letter

def lower_guess_counter():
    guess_counter -= 1
    return guess_counter
# graphic_generation('boots', guessed_letters = ['b','t'])

# graphic_generation("boats", guessed_list=["b", "t"])


# letter_input()
