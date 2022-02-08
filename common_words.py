"""
Find common words in 2 sentences
"""

def common_words(s1, s2):
    s1_set = set(s1.split(" "))
    s2_set = set(s2.split(" "))

    return list(s1_set.intersection(s2_set)) if s1_set.intersection(s2_set) else None

print(common_words("I am here", "You are here"))
print(common_words("I am here", "You are there"))


