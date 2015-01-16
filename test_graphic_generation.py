from mystery_word import graphic_gen



def test_does_this_work():
    word = "boats"
    assert graphic_gen(word) == '_____'

def test_with_letters():
    word = "BOATS"
    assert graphic_gen(word, guessed_list=["B","T"]) == "B__T_"

def test_full_word():
    word = "BOATS"
    assert graphic_gen(word, guessed_list=["B", "O", "A", "T", "S"]) == 'BOATS'
