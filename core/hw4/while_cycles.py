def mult_sum(x):
    i = 1
    result = 1
    while i <= x:
        result *= i
        i += 1
    return result


def count_s(s1, s2):
    years = 0
    percent = s2 / 10
    while s1 < percent:
        s1 *= 2
        s2 *= 3
        years += 1
    return years


def sum_and_digits(n):
    count = 0
    total = 0
    while n > 0:
        count += 1
        total += n % 10
        n //= 10
    return count, total


def age_counter(m, n):
    years = 0
    while m != 2 * n:
        m += 1
        n += 1
        years += 1
    return years, m, n
