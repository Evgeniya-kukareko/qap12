import time
import sys

sys.setrecursionlimit(2000)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = 1000

start_time = time.time()
factorial(n)
print("Factorial time:", time.time() - start_time, "seconds")

start_time = time.time()
for f in factorial_generator(n):
    pass
print("Generator time:", time.time() - start_time, "seconds")

start_time = time.time()
factorial_recursive(n)
print("Recursive time:", time.time() - start_time, "seconds")


def lexicographic_asc(*args):
    for arg in args:
        if arg > 19:
            return "Element {} is bigger than 19".format(arg)
        elif arg < 0:
            return "Element {} is less than 0".format(arg)

    number_names = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    sorted_numbers = sorted(args, key=lambda x: number_names[x])
    return sorted_numbers
