import sys
import functools as ft
from itertools import count, cycle
from math import factorial

# 1


def calc_pay(par):
    if len(par) == 3:
        return (int(par[0])*int(par[1]))+int(par[2])
    else:
        print('Нехватка параметров')


print(calc_pay(sys.argv[1:]))


# 2

list_start = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_filter = [list_start[i] for i in range(1, len(list_start)) if list_start[i] > list_start[i-1]]

print(list_filter)

# 3

list_res = [num for num in range(20, 241) if not(num % 20) or not(num % 21)]

print(list_res)

# 4

lis_s = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lis_r = [num for num in lis_s if lis_s.count(num) == 1]

print(lis_r)

# 5

res = [i for i in range(100, 1001) if not i % 2]
res_sum = ft.reduce(lambda a, b: a*b, res)

print(res_sum)

# 6

lis_rs = [1, 2, 3, 9, 'A']


def count_range(start, stop):
    """
    Generates and print range with start and stop

    :param start: start pos iteration
    :param stop: end pos iteration
    """
    result = []
    for i in count(start):
        print(i, end=' ')
        result.append(i)
        if i == stop:
            print()
            break
    return result


def cycle_range(lis, cnt):
    """
    Generates and print a cyclic list of repetitions cnt

    :param lis: cycle list
    :param cnt: count cycle
    """
    result = []
    for i, num in enumerate(cycle(lis)):
        print(num, end=' ')
        result.append(num)
        if not (i+1) % len(lis):
            ind = (i+1) // len(lis)
            if ind == cnt:
                print()
                break
            print()
    return result


print(count_range(5, 10))
print(cycle_range(lis_rs, 4))


# 7

def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


def print_fact(n, gen):
    for i, num in enumerate(gen(n)):
        print(f'{i+1}! = {num}')


print_fact(5, fact)






