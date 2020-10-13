import functools as ft
import json as js
import pickle as pic


# 1


def print_in_file(file_name, end_sym='q'):
    inp = None
    try:
        with open(file_name, 'w') as file1:
            while True:
                inp = input(f'Введите строку в файл. Для конца введите {end_sym}: ')
                if inp == end_sym:
                    break
                file1.write(f'{inp}\n')
    except IOError as e:
        print('Произошла ошибка', e)
    finally:
        print('Запись прошла успешно')


print_in_file('p1_file.txt')

# 2


def calculate_file(file_name):
    res = {}
    i = 0
    try:
        with open(file_name) as file2:
            for st in file2:
                i += 1
                res[i] = len(st.split())
        return {'count': i, 'count_word': res}
    except IOError as e:
        print('Ошибка', e)


print(calculate_file('p2_file.txt'))

# 3


def calc_salary(file_name):
    min_employed = []
    i = 0
    summa = 0
    try:
        with open(file_name) as file3:
            for st in file3:
                i += 1
                men = st.split(' - ')
                if int(men[1]) < 20000:
                    min_employed.append(men[0])
                summa += int(men[1])
    except IOError as e:
        print('Ошибка', e)
    else:
        print('Подсчет прошел успешно')
        return {'offended employees': min_employed, 'avg': summa/i}


print(calc_salary('p3_file.txt'))

# 4


def translate_file(file_in, file_out):
    dic = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    res = ''
    try:
        with open(file_in) as f4_i:
            for st in f4_i:
                res_i = st.split(' - ')
                res += f'{dic[int(res_i[1])]} - {res_i[1]}'
    except IOError as e:
        print('Ошибка открытия', e)
    else:
        print('Данные считаны. Запись...')
        try:
            with open(file_out, 'w') as f4_o:
                f4_o.write(res)
        except IOError as e:
            print('Ошибка записи', e)
        else:
            print('Запись успешно произведена')


translate_file('p4_file_in.txt', 'p4_file_out.txt')

# 5


def write_file(file_name, *args):
    try:
        with open(file_name, 'w') as file5:
            print(*args, file=file5)
    except IOError as e:
        print('Ошибка записи', e)
    else:
        print('Запись успешно произведена')


def calc_sum_file(file_name):
    try:
        with open(file_name) as file5:
            return ft.reduce(lambda a, b: int(a)+int(b), file5.readline().split())
    except IOError as e:
        print('Ошибка чтения', e)
    except TypeError:
        print('Проверьте содержимое файла!')


write_file('p5_file.txt', 1, 4, 5, 20)
print(calc_sum_file('p5_file.txt'))

# 6


def calc_hour_learn(file_name):
    res = {}
    try:
        with open(file_name) as file6:
            for st in file6:
                summa = 0
                inter = st.split()
                for num in inter[1:]:
                    if num == '-':      # skip if '-'
                        continue
                    summa += int(num[:num.index('(')])      # calc sum for one lesson
                res[inter[0][:-1]] = summa
    except IOError as e:
        print('Ошибка чтения', e)
    else:
        return res


print(calc_hour_learn('p6_file.txt'))

# 7


def calc_proceeds(file_in):
    """
    This function reads file and calculates result list

    :param file_in: input file name
    :return: result list
    """
    res_firm = {}
    res = []
    i, summa = 0, 0
    try:
        with open(file_in) as f_in:
            for st in f_in:
                spl = st.split()
                proceeds = int(spl[2]) - int(spl[3])
                res_firm[spl[0]] = proceeds
                if proceeds < 0:        # skip if proceeds<0
                    continue
                summa += proceeds
                i += 1
    except IOError as e:
        print('Ошибка чтения', e)
    else:
        res.append(res_firm)
        res.append({'average_profit': summa/i})
        return res


def write_json(obj, file_out, type_ser='json'):
    """
    This function dumps obj in file

    :param obj: object dump in file
    :param file_out: output file name
    :param type_ser: dump type (json or pickle)
    """
    try:
        if type_ser.lower() == 'json':
            with open(file_out, 'w') as f_jp:
                js.dump(obj, f_jp)
        elif type_ser.lower() == 'pickle':
            with open(file_out, 'wb') as f_jp:
                pic.dump(obj, f_jp)
        else:
            raise Exception('Invalid dump type')
    except IOError as e:
        print('Ошибка записи json', e)


def result_jon(file_in, file_out, func_read=calc_proceeds, func_write=write_json, type_ser='json'):
    obj = func_read(file_in)
    func_write(obj, file_out, type_ser=type_ser)
    print('Операция завершена!')


def load_file(file_in, type_ser='json'):
    """
    This function loads data from file

    :param file_in: input file name
    :param type_ser: load type (json or pickle)
    """
    try:
        if type_ser.lower() == 'json':
            with open(file_in) as f_jon:
                return js.load(f_jon)
        elif type_ser.lower() == 'pickle':
            with open(file_in, 'rb') as f_pic:
                return pic.load(f_pic)
        else:
            raise Exception('Invalid load type')
    except IOError as e:
        print('Ошибка чтения', e)


result_jon('p7_file_in.txt', 'p7_file_out.jon')
result_jon('p7_file_in.txt', 'p7_file_out.pic', type_ser='pickle')
print(load_file('p7_file_out.jon'))
print(load_file('p7_file_out.pic', 'pickle'))







