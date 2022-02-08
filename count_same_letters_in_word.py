"""
Python coding: count the same letters in a single word
"""

def count_same_letter(word):
    count_dict = dict()
    for letter in word:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return {k:v for (k,v) in count_dict.items() if v > 1}
print(count_same_letter("applepie"))


