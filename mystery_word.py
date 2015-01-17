import random
from pyfiglet import Figlet
import os
import time


f = Figlet(font='epic')


def change_guess_counter(guess_counter, guessed_letter, game_word):
    """Uses guess_check (Will be True, or False) to either subtract one from
    the guess counter, if guess_check is False. Or """
    if guessed_letter in game_word:
        return guess_counter
    else:
        guess_counter -= 1
        return guess_counter


def get_difficulty():
    """Asks the user for a difficulty, then assigns it to a variable mode."""
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
    if mode not in ok_inputs:
        print(wrong_input)
        return get_difficulty()
    if mode == "E":
        print("You picked easy.")
    elif mode == "M":
        print("You picked medium.")
    else:
        print("You picked hard.")
    return mode


def graphic_list_mkr(game_word, guessed_letters):
    """Generates a list of the characters needed to make the outline of the
    blank word or word filled in with guesses made so far."""
    graphic_list = []
    for letter in game_word:
        if letter in guessed_letters:
            graphic_list.append(letter)
        else:
            graphic_list.append("_")
    return graphic_list


def hidden_graphic_mkr(graphic_list):
    """Creates graphic used to check win condition in win_loss_checker."""
    hidden_graphic = "".join(graphic_list)
    return hidden_graphic


def introduction():
    """Just a way of giving the player an introduction to the games and it's
    rules."""
    print(f.renderText("Mystery Word"))
    introduction_text = """
          Welcome to Mystery Word! In this game you will attempt to guess
          a mystery word (isn't that kind of obvious?). However, you will be
          guessing it one letter at a time. If you guess the wrong letter
          eight times you will lose the game, so choose wisely! Please guess
          only one letter at a time. Good luck!
          """
    print(introduction_text)
    return(introduction_text)


def letter_input():
    """Asks the user to give a letter they would like to guess. If it is not
    a letter, number, more than one letter, or a letter they have already
    guessed it will force them to input until they do give an acceptable
    letter."""
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


def play_again():
    """Asks the player if they would like to play again or not. It will
    only accept the letters y or n. If they do not pick y or n it will return
    the function untill they do."""
    print(f.renderText("Try Again?"))
    choice = input("[Y]es, [N]o?")
    choice = choice.upper()
    pick_again = "Please pick again."
    if len(choice) > 1:
        print(pick_again)
        return play_again()
    elif choice != "Y" and choice != "N":
        print(pick_again)
        return play_again()
    elif choice.isnumeric():
        print(pick_again)
        return play_again()
    elif choice == "Y" or choice == "N":
        return choice


def progress_teller(seen_graphic, guess_counter, guessed_letters):
    """Prints out the list of guessed letters, number of guesses left,
    and the state of word filled in with their correct guesses."""
    print("""List of guessed letters: {}
    Guesses left: {}""".format(
              sorted(guessed_letters), guess_counter))
    print(f.renderText(seen_graphic))
    return """Here is your current progress: {}
               List of guessed letters: {}
               Guesses left: {}""".format(seen_graphic,
                                          guessed_letters, guess_counter)


def seen_graphic_mkr(graphic_list):
    """Creates the randomly generated word filled in with the correctly guessed
     letters with spaces inbetween each letter or underscore. This is the
     version the user will see, thus the name."""
    seen_graphic = " ".join(graphic_list)
    return seen_graphic


def win_loss_checker(random_word, guesses_left, created_word):
    """Checks to see if the player has fulfilled the win conditions or
    has guessed too many times and lost. Then returns a word that will be
    checked inside the loop to see if the loop needs to be broken."""
    if random_word == created_word:
        win_string = "win"
        print("You win! Congratulations!")
        return win_string
    elif guesses_left == 0:
        loss_string = "loss"
        print("You have run out of guesses, you lose.")
        return loss_string


def word_get(file, mode):
    """"Opens a file that should just be made of words with no puncuation
    or special characters. Then based off of the mode, the difficulty the user
    gave, picks a word randomly from the dictionary. If the user picks easy the
    word will be between four and six characters long. If they picked medium
    the word will be between six and ten characters long, and if they picked
    hard the word will be more than eleven characters long."""
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


os.system("clear")
introduction()
while True:
    guess_counter = 8
    guessed_letters = []
    mode = get_difficulty()
    game_word = word_get("/usr/share/dict/words", mode)
    print("You word is {} characters long.".format(len(game_word)))
    while True:
        guessed_letter = letter_input()
        guessed_letters.append(guessed_letter)
        graphic_list = graphic_list_mkr(game_word, guessed_letters)
        hidden_graphic = hidden_graphic_mkr(graphic_list)
        seen_graphic = seen_graphic_mkr(graphic_list)
        guess_counter = change_guess_counter(guess_counter, guessed_letter,
                                             game_word)
        os.system("clear")
        progress_teller(seen_graphic, guess_counter, guessed_letters)
        condition = win_loss_checker(game_word, guess_counter, hidden_graphic)
        if condition == "win":
            print(f.renderText("You win!"))
            break
        elif condition == "loss":
            print("Your word was:")
            print(f.renderText(game_word))
            print(f.renderText("You lose."))
            break
    time.sleep(5)
    os.system("clear")
    choice = play_again()
    if choice == "Y":
        continue
    elif choice == "N":
        break
