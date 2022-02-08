"""
Calculate the average word length.
"""


def avg_word_length(lst):

    len_lst = list()

    if type(lst) == list:
        word_lst = lst
    elif type(lst) == str:
        word_lst = lst.split(' ')

    word_lst = [i for i in word_lst if i]

    for word in word_lst:
        if len(word) > 0:
            len_lst.append(len(word.strip()))

    return int(sum(len_lst)/ len(word_lst)) if len(word_lst) > 0 else 0

print(avg_word_length(['Hi ', 'world', 'Amruta']))

print(avg_word_length('hello a  world'))

print(avg_word_length([]))