from mystery_word import guess_checker

def test_true_guess():
    assert guess_checker("A", "APPLE") == True

def test_flase_guess():
    assert guess_checker("B", "APPLE") == False
