"""
python question: given a two dimensional list for example [ [2,3],[3,4],[5]]
person 2 is friends with 3 etc. find how many friends does each person has.
note one person has no friends.
"""


def friend_count(nested_list):
    friend_count = dict()

    for lst in nested_list:

        if len(lst) > 1:
            if lst[0] in friend_count:
                friend_count[lst[0]] += 1
            else:
                friend_count[lst[0]] = 1
        else:
            friend_count[lst[0]] = 0

    return friend_count


print(
    friend_count(
        [[2, 3], [3, 4], [5]
         ]
    )
)


