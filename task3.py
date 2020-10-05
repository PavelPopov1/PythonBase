# 1

def div_full(divisive, divider):
    """
    Division function
    """
    try:
        return divisive / divider
    except ZeroDivisionError:
        print('Деление на 0!')
    except Exception as e:
        print('Ошибка', e)


print(div_full(11, 5))
print(div_full(5, 0))
print(div_full(5, 'str2'))


# 2


def user_data(**kwargs):
    """
    Writes to the screen user data
    :param kwargs: user dates
    """
    print(*kwargs.values(), sep=', ')


user_data(name='Pavel', sirname='Popov', year=1998, citie='Moscow', email='pp@', phone=7)


# 3


def my_func(num1, num2, num3):
    if num1 + num2 >= num2 + num3 and num1 + num2 >= num1 + num3:
        return num1 + num2
    elif num2 + num3 >= num1 + num2 and num2 + num3 >= num1 + num3:
        return num2 + num3
    else:
        return num1 + num3


print(my_func(8, 77, 7))


# 4


def exp_simple(num, exp):
    return num ** exp


def exp_hard(num, exp):
    res = 1
    for i in range(1, abs(exp) + 1):
        res *= num
    return res if exp >= 0 else 1/res


print(exp_simple(5.5555, -9))
print(exp_hard(5.5555, -9))


# 5


def sum_kla(end_sym='#'):
    print('Символ конца строки:', end_sym)
    sum_r = 0
    while True:
        str_u = input('Введите строку чисел через пробел: ')
        for elem in str_u.split():
            if elem == end_sym:
                print(sum_r)
                return sum_r
            try:
                sum_r += int(elem)
            except Exception as e:
                print('Ошибка:', e)
        print(sum_r)


sum_kla()


# 6

def int_func(word):
    return str(word).capitalize()


def cap_func(str_w, func=int_func):
    """
    Title function
    :param str_w: string
    :param func: capitalize
    :return: converted string
    """
    lis = str(str_w).split()
    res = ''
    for elem in lis:
        res += f'{func(elem)} '
    return res[:-1]


def cap_func1(str_w, func):
    """
    Title function one line
    """
    return func(str_w)


print(cap_func('я тут придумал одну идею'))
print(cap_func1('я тут придумал одну идею', lambda word: str(word).title()))
