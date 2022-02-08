"""
Find the minimum absolute difference between the set of elements of an array.
"""

def findMinDiff(arr):
    # Initialize difference as infinite
    diff = 10 ** 20
    n = len(arr)
    # Find the min diff by comparing difference
    # of all possible pairs in given array
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])

    # Return min diff
    return diff

arr = [10, 15, -2, 188]
print("Minimum difference is " + str(findMinDiff(arr)))