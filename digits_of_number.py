# Return a list of digits given a number

def digits_of_number(num):
    digits = list()
    for n in str(num):
        try:
            digits.append(int(n))
        except:
            continue
    return digits

print(digits_of_number(123.4))
print(digits_of_number(-400))