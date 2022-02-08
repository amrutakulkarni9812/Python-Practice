# Calculate dot product of three vectors
import numpy as np
def dot_product(list1, list2, list3):

    # print(tuple(zip(list1, list2, list3)))
    return sum([i * j * k for (i, j, k) in zip(list1, list2, list3)])


print(dot_product([1,2,3], [4,5,6], [7,8,9]))
