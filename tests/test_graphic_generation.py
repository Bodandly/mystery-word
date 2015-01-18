from mystery_word import graphic_list_mkr

word = "BOATS"

empty_list = []

partial_list = ["B", "T"]

full_list = ["B", "O", "A", "T", "S"]

empty_list_answer = ["_", "_", "_", "_", "_"]

partial_list_answer = ["B", "_", "_", "T", "_"]

full_list_answer = ["B", "O", "A", "T", "S"]


def test_does_this_work():
    assert graphic_list_mkr(word, empty_list) == empty_list_answer


def test_with_letters():
    assert graphic_list_mkr(word, partial_list) == partial_list_answer


def test_full_word():
    assert graphic_list_mkr(word, full_list) == full_list_answer
