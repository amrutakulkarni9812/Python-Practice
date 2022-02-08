# Return cumulative sum of the elements in a list

def cumulative_sum(lst):

    new_lst = [0] * len(lst)
    for i in range(len(lst)):
        # print(new_lst)
        new_lst[i] = new_lst[i-1]+ lst[i]

    print(new_lst)


cumulative_sum([1,1,1])

cumulative_sum([1,-1,3])


