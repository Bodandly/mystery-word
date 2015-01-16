from mystery_word import word_get

def get_list():
    assert word_get("empty_file.txt") == ""

def get_bigger_list():
    assert word_get("small_list.txt") == ["Hippo", "maddening", "Regular"]
