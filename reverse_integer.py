"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0

        if x == 0:
            return rev

        elif x > 0:
            while x > 0:
                a = x % 10
                rev = rev * 10 + a
                x = x // 10

        else:
            x = int(str(x)[1:len(str(x))])
            while x > 0:
                a = x % 10
                rev = rev * 10 + a
                x = x // 10
            rev = -1 * rev

        return rev



sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
