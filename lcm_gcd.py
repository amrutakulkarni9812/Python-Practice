# Formula: number_1 * number_2 = lcm * gcd

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


print(gcd(5, 24))


def lcm(a, b):
    lcm = (a*b) // gcd(a, b)

    return lcm

print(lcm(5,24))

