"""
Given a nested list, [ [ 0, 1 ], [ [ 2 ] ], [ 3, 4 ] ], return straight list
Pop last element, If it is a list, extend nested list with the elements. In the next loops,
these individual elements will be added to the flat list
"""


def flatten_nested_list(nested_lst):
    flat_lst = list()

    while nested_lst:

        e = nested_lst.pop()

        if type(e) == list:
            nested_lst.extend(e)

        else:
            flat_lst.append(e)

    return sorted(flat_lst)


print(flatten_nested_list([[0, 1], [[2]], [3, 4]]))
