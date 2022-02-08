def find_max_emement(arr):

    sorted_arr = sorted(arr, reverse= True)

    return sorted_arr[0]


print(find_max_emement([4]))