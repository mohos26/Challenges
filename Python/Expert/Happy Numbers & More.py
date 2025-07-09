# https://edabit.com/challenge/5RN3TNyGMWRgynLLa
# 09.07.2025
# Expert

from math import sqrt, ceil, floor


def multiples(n):
    lst, var = [], []
    var2 = sqrt(abs(n))
    for i in range(1, ceil(var2)):
        if not n % i:
            lst.append(i)
            lst.append(n//i)
    if var2 == floor(var2):
        var = [floor(var2)]
    return lst[::2] + var + lst[::-2]


def is_happy(n):
    if not str(n).isdigit():
        return False
    count = 0
    while True:
        aid = 0
        for i in str(n):
            aid += int(i)**2
        if aid == 1:
            break
        if count > 100:
            return False
        count += 1
        n = aid
    return True


def is_prime(n):
    if n < 0:
        return False
    return len(multiples(n)) == 2


def is_perfect(n):
    if n < 0:
        return False
    return len(multiples(n)) > 2 and sum(multiples(n)[:-1]) == n


def is_triangular(n):
    if n < 0:
        return False
    return (sqrt(1 + 8 * n) - 1) / 2 == (sqrt(1 + 8 * n) - 1) // 2


def happy(n):
    res = ""
    res += f"{n} is "
    if is_happy(n):
        res += "a happy number.\n"
    else:
        res += "an unhappy number.\n"

    res += f"{n} is "
    if is_prime(n):
        res += "a prime number.\n"
    else:
        res += "not a prime number.\n"

    res += f"{n} is "
    if is_perfect(n):
        res += "a perfect number.\n"
    else:
        res += "not a perfect number.\n"

    res += f"{n} is "
    if is_triangular(n):
        res += "a triangular number.\n"
    else:
        res += "not a triangular number.\n"
    return res

# note: because the compiler of edabit are old, the code don't pass
# this is a same tester:


def run_tests():
    assert happy(-1) == (
        "-1 is an unhappy number.\n"
        "-1 is not a prime number.\n"
        "-1 is not a perfect number.\n"
        "-1 is not a triangular number.\n"
    )

    assert happy(0) == (
        "0 is an unhappy number.\n"
        "0 is not a prime number.\n"
        "0 is not a perfect number.\n"
        "0 is a triangular number.\n"
    )

    assert happy(1) == (
        "1 is a happy number.\n"
        "1 is not a prime number.\n"
        "1 is not a perfect number.\n"
        "1 is a triangular number.\n"
    )

    assert happy(2) == (
        "2 is an unhappy number.\n"
        "2 is a prime number.\n"
        "2 is not a perfect number.\n"
        "2 is not a triangular number.\n"
    )

    assert happy(3) == (
        "3 is an unhappy number.\n"
        "3 is a prime number.\n"
        "3 is not a perfect number.\n"
        "3 is a triangular number.\n"
    )

    assert happy(7) == (
        "7 is a happy number.\n"
        "7 is a prime number.\n"
        "7 is not a perfect number.\n"
        "7 is not a triangular number.\n"
    )

    assert happy(28) == (
        "28 is a happy number.\n"
        "28 is not a prime number.\n"
        "28 is a perfect number.\n"
        "28 is a triangular number.\n"
    )

    assert happy(496) == (
        "496 is a happy number.\n"
        "496 is not a prime number.\n"
        "496 is a perfect number.\n"
        "496 is a triangular number.\n"
    )

    assert happy(709) == (
        "709 is a happy number.\n"
        "709 is a prime number.\n"
        "709 is not a perfect number.\n"
        "709 is not a triangular number.\n"
    )

    assert happy(8128) == (
        "8128 is a happy number.\n"
        "8128 is not a prime number.\n"
        "8128 is a perfect number.\n"
        "8128 is a triangular number.\n"
    )

    assert happy(150193) == (
        "150193 is an unhappy number.\n"
        "150193 is a prime number.\n"
        "150193 is not a perfect number.\n"
        "150193 is not a triangular number.\n"
    )

    assert happy(497503) == (
        "497503 is an unhappy number.\n"
        "497503 is not a prime number.\n"
        "497503 is not a perfect number.\n"
        "497503 is a triangular number.\n"
    )

    print("✅ All tests passed!")


# Run the tests
run_tests()
