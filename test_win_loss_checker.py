from mystery_word import win_loss_checker

win_string = "You win! Congratulations!"
loss_string = "You have run out of guesses, you lose."

def test_win():
    assert win_loss_checker("BLOB", 8, "BLOB") == win_string

def test_loss():
    assert win_loss_checker("BLOB", 0, "BL_B") == loss_string

def test_win_with_new_word():
    assert win_loss_checker("BILLIONS", 8, "BILLIONS") == win_string

def test_win_with_less_counters():
    assert win_loss_checker("BUFFALO", 4, "BUFFALO") == win_string

def test_not_loss():
    assert win_loss_checker("BUFFALO", 2, "BUFF___") != loss_string
