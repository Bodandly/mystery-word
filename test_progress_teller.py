from mystery_word import progress_teller


word = "BOAT_"
word_list = ["B","O","A","T"]


def test_progress_teller():
    assert progress_teller(word, word_list, 8) == """Here is your current progress: BOAT_ List of guessed letters: ["B","O","A","T"] Guesses left: 8"""
