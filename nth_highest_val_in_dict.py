"""
Given a dictionary, print the key for nth highest value present in the dict.
If there are more than 1 record present for nth highest value then sort the key
 and print the first one.
"""


def nth_highest_val_in_dict(d, n):
    # sorted_values = [d[k] for k in sorted(d, key=d.get, reverse=True)]
    sorted_values = [v for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True)]
    keys = [k for k in d if d[k] == sorted_values[n - 1]]
    print(sorted(keys)[0])


nth_highest_val_in_dict({'b': 2, 'c': 3, 'd': 4, 'a': 1, 'e': 5, 'f': 5}, 1)
