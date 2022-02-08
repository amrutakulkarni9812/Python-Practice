"""
Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.
"""


class Solution:
    def isMonotonic(self, A):
        return True if A == sorted(A, reverse=True) or A == sorted(A, reverse=False) else False


sol = Solution()

print(sol.isMonotonic([6, 5, 4, 10]))


