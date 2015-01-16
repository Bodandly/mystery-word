from mystery_word import change_guess_counter

def test_guess_counter():
    assert change_guess_counter(8, False) == 7

def test_guess_again_counter():
    assert change_guess_counter(4, False) == 3

def test_guess_correct():
    assert change_guess_counter(3, True) == 3

def test_guess_again_correct():
    assert change_guess_counter(8, True) == 8
