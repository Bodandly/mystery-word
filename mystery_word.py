import random


def word_get(file, mode):
    with open(file) as working_file:
        word_string = working_file.read()
    word_list = word_string.split()
    word = random.choice(word_list)
    if mode == "E":
        while len(word) > 6 or len(word) < 4:
            word = random.choice(word_list)
    if mode == "M":
        while len(word) > 10 or len(word) < 6:
            word = random.choice(word_list)
    if mode == "H":
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


def graphic_list_mkr(game_word, guessed_letters):
    graphic_list = []
    for letter in game_word:
        if letter in guessed_letters:
            graphic_list.append(letter)
        else:
            graphic_list.append("_")
    return graphic_list


def hidden_graphic_mkr(graphic_list):
    hidden_graphic = "".join(graphic_list)
    return hidden_graphic


def seen_graphic_mkr(graphic_list):
    seen_graphic = " ".join(graphic_list)
    return seen_graphic


#def check_word(seen_graphic):


def get_difficulty():
    mode = input("Would you like to play [E]asy, [M]edium, or [H]ard? ")
    mode = mode.upper()
    ok_inputs = ["E", "M", "H"]
    wrong_input = "Please enter E, M, or H. Try again."
    if mode == "":
        print(wrong_input)
        return get_difficulty()
    if len(mode) > 1:
        print(wrong_input)
        return get_difficulty()
    if not mode.isalpha():
        print(wrong_input)
        return get_difficulty()
    if not mode in ok_inputs:
        print(wrong_input)
        return get_difficulty()
    if mode == "E":
        print("You picked easy.")
    elif mode == "M":
        print("You picked medium.")
    else:
        print("You picked hard.")
    return mode


def letter_input():
    unfinished_letter = input("Please provide a letter you'd like to guess: ")
    letter = unfinished_letter.upper()
    if letter in guessed_letters:
        print("You already guessed that letter, please try again.")
        return letter_input()
    elif letter == "":
        print("You entered nothing, please try again.")
        return letter_input()
    elif len(letter) > 1:
        print("You entered more than one letter, please try again.")
        return letter_input()
    elif not letter.isalpha():
        print("You entered a number, please try again.")
        return letter_input()
    else:
        print("You entered {}".format(letter))
        return letter


def change_guess_counter(guess_counter, guess_check):
    if guess_check == False:
        guess_counter -= 1
        return guess_counter
    else:
        return guess_counter


def win_loss_checker(random_word, guesses_left, created_word):
    if random_word == created_word:
        win_string = "win"
        print("You win! Congratulations!")
        return win_string
    elif guesses_left == 0:
        loss_string = "lose"
        print("You have run out of guesses, you lose.")
        return loss_string
    else:
        carry_on = "continue"
        return carry_on




def progress_teller(seen_graphic, guess_counter, guessed_letters):
        print("""Here is your current progress: {}
                 List of guessed letters: {}
                 Guesses left: {}""".format(seen_graphic,
                 guessed_letters, guess_counter))
        return """Here is your current progress: {}
                  List of guessed letters: {}
                  Guesses left: {}""".format(seen_graphic,
                  guessed_letters, guess_counter)


def guess_checker(guessed_letter, game_word):
    return guessed_letter in game_word

def play_again():
    choice = input("Play again: [Y]es, [N]o?")
    choice = choice.upper()
    if len(choice) > 1:
        print("Please pick again.")
        return play_again()
    elif choice != "Y" or choice != "N":
        print("Please pick again.")
        return play_again()
    elif choice.isnumeric():
        print("Pleae pick again.")
        return play_again()
    elif choice == "Y" or choice == "N":
        return choice


progress_teller("Derp", 8, ["B", "C"])

introduction()

while True:
    guess_counter = 8
    guessed_letters = []
    mode = get_difficulty()
    game_word = word_get('/usr/share/dict/words', mode)
    print("You word is {} characters long.".format(len(game_word)))
    while True:
        guessed_letter = letter_input()
        guessed_letters.append(guessed_letter)
        graphic_list = graphic_list_mkr(game_word, guessed_letters)
        hidden_graphic = hidden_graphic_mkr(graphic_list)
        seen_graphic = seen_graphic_mkr(graphic_list)
        guess_check = guess_checker(guessed_letter, game_word)
        guess_counter = change_guess_counter(guess_counter, guess_check)
        progress_teller(seen_graphic, guess_counter, guessed_letters)
        condition = win_loss_checker(game_word, guess_checker, guessed_letters)
        print(condition)
        if guess_counter == 0:
            print("You lose!")
            break
        elif hidden_graphic == game_word:
            print("You win!")
            break
    choice = play_again()
    if choice == "N":
        break
