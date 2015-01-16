import random


def word_get(file, mode):
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
    introduction_text = """
          Welcome to Mystery Word! In this game you will attempt to guess
          a mystery word (isn't that kind of obvious?). However, you will be
          guessing it one letter at a time. If you guess the wrong letter
          eight times you will lose the game, so choose wisely! Please guess
          only one letter at a time. Good luck!
          """
    print(introduction_text)
    return(introduction_text)


def graphic_gen(word, guessed_list=[]):
    graphic_list = []
    for letter in word:
        if letter in guessed_list:
            graphic_list.append(letter)
        else:
            graphic_list.append("_")
    seen_graphic = " ".join(graphic_list)
    hidden_graphic = "".join(graphic_list)
    print(seen_graphic)
    return hidden_graphic


def get_difficulty():
    mode = input("Would you like to play [E]asy, [M]edium, or [H]ard? ")
    mode = mode.upper()
    wrong_input = "Please enter E, M, or H. Try again."
    if mode == "":
        print(wrong_input)
        get_difficulty()
    if len(mode) > 1:
        print(wrong_input)
        letter_input()
    if not mode.isalpha():
        print(wrong_input)
        letter_input()
    if mode == "E":
        mode = "Easy"
    if mode == "M":
        mode = "Medium"
    if mode == 'H':
        mode = "Hard"

    print("You picked {}.".format(mode))
    return mode


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


def change_guess_counter(guess_counter, guess_checker):
    if guess_checker == False:
        guess_counter -= 1
        return guess_counter
    else:
        return guess_counter


def win_loss_checker(game_word, guess_counter, current_graphic):
    if game_word == current_graphic:
        win_string = "You win! Congratulations!"
        return win_string
        print(win_string)
    if guess_counter == 0:
        loss_string = "You have run out of guesses, you lose."
        return loss_string
        print(loss_string)


def progress_teller():
        print("Here is your current progress: {}.".format(graphic_gen()))
        print("You have {} guesses left.".format(guess_counter))


def guess_checker(guessed_letter, game_word):
    return guessed_letter in game_word


# introduction()
#
# while True:
#     get_difficulty()
#     guess_counter = 8
#     guessed_list = []
#     difficulty = get_difficulty()
#     game_word = word_get('/usr/share/dict/words', mode=difficulty)
#     print("You word is {} characters long.".format(len(game_word)))
#
#     while True:
#         progress_teller()
#         guessed_list.append(letter_input())
#
#         win
#
#
#    print("Your word ")


# letter_input()
