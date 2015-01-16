from mystery_word import graphic_generation


def test_does_this_work():
    word = "boats"
    assert graphic_generation(word) == '_____'

def test_with_letters():
    word = "BOATS"
    assert graphic_generation(word, guessed_list=['B','T']) == 'B__T_'
