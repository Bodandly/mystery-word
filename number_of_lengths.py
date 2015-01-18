# Program that creates a dictionary with the number of words of each
# wordlength. Inspired by Alan.


with open("/usr/share/dict/words") as working_file:
    word_string = working_file.read()
word_list = word_string.split()
word_len_dict = {}
for word in word_list:
    if len(word) not in word_len_dict:
        word_len_dict[len(word)] = 1
    else:
        word_len_dict[len(word)] += 1
print(word_len_dict)
