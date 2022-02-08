# Find first non recurring number in a list

def first_non_recurring_item(word_list):
    count_dict = dict()

    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    return [k for k,v in count_dict.items() if v == 1][0]


print(first_non_recurring_item([1,2,3,4,5,2,1,4,5,6]))
