def first(x):
    x = x * 2
    return x


def first_metamorph(x):
    k = 20
    return x * 2 * k / k


def second(n):
    s = 0
    for i in range(n):
        s += i
    return s


def second_metamorph(n):
    k = 100
    s = k
    for i in range(n + k):
        s += i

    for j in range(n, n + k):
        s -= j

    return s - k


assert(first(245) == first_metamorph(245))
assert(second(245) == second_metamorph(245))