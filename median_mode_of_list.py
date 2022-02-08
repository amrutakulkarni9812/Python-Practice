# Find out median of the list

def median(x):
    if len(x) % 2 != 0:
        return x[len(x) // 2]
    elif len(x) == 0:
        return None
    else:
        return (x[len(x) // 2] + x[len(x) // 2 + 1]) / 2


print(median([1, 2, 3, 4]))

print(max([1, 2, 3, 4]))


def find_mode(x):
    frequency_dict = dict()

    if len(x) == 0:
        return 0
    else:
        for i in x:
            if i in frequency_dict:
                frequency_dict[i] += 1
            else:
                frequency_dict[i] = 1

        sorted_frequency = [k for k,v in (sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True))]

    print(sorted_frequency[0])


find_mode([1, 2, 3, 4, 2, 3, 4, 4, 6, 8,8,8,8,8,8,8,8,8,8,8])



