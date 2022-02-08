"""
# Find position of s in Missisipi
"""


def find_s(x):
    count = dict()
    for i in range(len(x)):
        count[i] = x[i]
    return [k for k, v in count.items() if v == 's']


print(find_s('missisipi'))

"""
word="missisipi"
for k,v in enumerate(word):
    if v == "s":
        print(k)
"""
