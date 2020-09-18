
i = 0
j = 7
k = j * 2

while i <= j:
    print(' '*k, end = '')
    for i in range(-i, i+1):
        print(abs(i), end=' ')
        i += 1
    k -= 2
    print('\n')
