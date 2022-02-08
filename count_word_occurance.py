"""
Python coding: count the occurrence of a word in a list
"""


def count_occurance(word_list, word_to_count):
    count_dict = dict()
    if word_to_count not in word_list:
        return 0
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict[word_to_count]


print(count_occurance(['cat', 'cat', 'applepie'], "car"))
