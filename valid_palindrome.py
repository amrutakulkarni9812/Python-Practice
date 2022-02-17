'''
    Check if a string is palindrome or not
'''

import re
def check_palindrome(str):
    str = re.sub('[^A-Za-z0-9]+', '', str)
    str = str.lower()
    return str == str[::-1]



print(check_palindrome("A man, a plan, a canal: Panama"))

print(check_palindrome("race a car"))

print(check_palindrome("    "))