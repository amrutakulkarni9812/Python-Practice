"""
Return uncommon words from two sentences, also if a word occurs twice in a sentence and never in second sentence, it should not be returned in answer
"""


def uncommon_words(s1, s2):
    count_dict = dict()
    for word in (s1 + " " + s2).split():
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return [k for (k, v) in count_dict.items() if v == 1]


print(uncommon_words("this apple is sour", ""))
print(uncommon_words("Firstly this is the first string", "Next is the second string"))

def uncommon_words_set(s1, s2):
    st_A = set(s1.split())
    st_B = set(s2.split())
    return list((st_A - st_B) | (st_B - st_A))

print(uncommon_words_set("this apple is sour", ""))
print(uncommon_words_set("Firstly this is the first string", "Next is the second string"))