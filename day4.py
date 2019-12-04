def increasing_digits(number):
    div = 100000
    digit = number // div
    while True:
        number = number % (digit * div)
        div /= 10
        if div < 1:
            return True
        next_digit = number // div
        if next_digit < digit:
            return False

        digit = next_digit


def has_double(number):
    digits = []
    div = 100000
    digit = number // div
    while 1:
        digits.append(digit)
        number = number % (digit * div)
        div /= 10
        if div < 1:
            break
        digit = number // div

    for dig in digits:
        count = 0
        for i in range(len(digits)):
            if dig == digits[i]:
                count += 1

        if count == 2:
            return True


c = 0
for n in range(138307, 654504):
    if increasing_digits(n) and has_double(n):
        c += 1


print(c)