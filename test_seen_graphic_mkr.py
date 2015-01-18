from mystery_word import seen_graphic_mkr

word = "BOATS"


empty_list = ["_", "_", "_", "_", "_"]

partial_list = ["B", "_", "_", "T", "_"]

full_list = ["B", "O", "A", "T", "S"]

empty_answer = "_ _ _ _ _"

partial_answer = "B _ _ T _"

full_answer = "B O A T S"


def test_seen_nothing():
    assert seen_graphic_mkr(empty_list) == empty_answer


def test_seen_some():
    assert seen_graphic_mkr(partial_list) == partial_answer


def test_seen_full():
    assert seen_graphic_mkr(full_list) == full_answer
