# Find the elements on odd positions of a zero based list

def odd_elements(lst):
    odd_lst = list()
    for i in range(len(lst)):
        if (i % 2) != 0:
            odd_lst.append(lst[i])

    return odd_lst

print(odd_elements([0,1,2,3,4,5]))
print(odd_elements([1,-1,2,-2]))

assert odd_elements([0,1,2,3,4,5]) == [1,3,5]
assert odd_elements([1,-1,2,-2]) == [-1,-2]