from mystery_word import change_guess_counter


game_word = "BOATS"


def test_guess_counter():
    assert change_guess_counter(8, "J", game_word) == 7


def test_guess_again_counter():
    assert change_guess_counter(4, "R", game_word) == 3


def test_guess_correct():
    assert change_guess_counter(3, "B", game_word) == 3


def test_guess_again_correct():
    assert change_guess_counter(8, "T", game_word) == 8
