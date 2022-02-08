"""
Validate an ip address, has 4 parts, each part is numeric, doesn't have leading zeroes and
numbers are between 0 and 255
"""


def validate(ip):
    sub_ip = ip.split('.')

    if len(sub_ip) != 4:
        return False

    for num in sub_ip:
        # print(type(num[0]))
        if (not num.isdigit()) or (num[0] == '0' and len(num) > 1):
            return False

        num = int(num)

        if num < 0 or num > 255:
            return False
    return True

print(validate('127.0.0.1'))

print(validate('027.0.0.1'))

print(validate('127.0.0.1.2'))

print(validate('127.p.0.1'))


