# Replace None values in a list with previous non null values
def replace_none_with_prev_value(x):
    for i in range(len(x)):
        if x[i] is None:
            x[i] = x[i - 1]
    print(x)


replace_none_with_prev_value([1, 4, None, None, 3])

replace_none_with_prev_value([None, 4, None, None, 3])
