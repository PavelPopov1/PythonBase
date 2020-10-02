import copy as cp

# 1

list1 = [12, 'Some str', complex(5, 5), [5, 6], {'key': 'value'}]

for i in range(len(list1)):
    print(type(list1[i]))

# 2

list2 = []
elem = None

while elem != '#':
    elem = input('Введите элемент списка. # - завершение ввода ')
    if elem != '#':
        list2.append(elem)

for i in range(0, len(list2) - 1, 2):  # go to pair
    buf = list2[i]
    del list2[i]  # delete elem
    list2.insert(i + 1, buf)  # insert elem to next pos

print(list2)

# 3


month_in = int(input('Введите месяц от 1 до 12: '))

if month_in in range(1, 3) or month_in == 12:
    print('Время года: зима')
elif month_in in range(3, 6):
    print('Время года: весна')
elif month_in in range(6, 9):
    print('Время года: лето')
else:
    print('Время года: осень')

month_dict = {'зима': (1, 2, 12),
              'весна': (3, 4, 5),
              'лето': (6, 7, 8),
              'осень': (9, 10, 11)}

for key, elem in month_dict.items():
    if month_in in elem:
        print(f'Время года: {key}')
        break

# 4

user_str = input('Введите строку: ')

split_str = user_str.split()

for i, elem in enumerate(split_str):
    if len(elem) > 10:
        print(f'Word {i+1}: {elem[:10]}')
    else:
        print(f'Word {i+1}: {elem}')

# 5

# not use sort method

my_list = [7, 5, 3, 3, 2]

let = None
while let != '#':
    let = input('Введите число. Если больше не хотите вводить - введите #: ')
    if let == '#':
        break
    let = int(let)
    index = 0
    if my_list:
        for i, elem in enumerate(my_list):
            if elem <= let:
                index = i
                break
        if min(my_list) > let:
            index = len(my_list)
        my_list.insert(index, let)
    else:
        my_list.append(let)

print(my_list)

# with sort method

my_list = [7, 5, 3, 3, 2]
let = None

while let != '#':
    let = input('Введите число. Если больше не хотите вводить - введите #: ')
    if let == '#':
        break
    let = int(let)
    my_list.append(let)

my_list.sort(reverse=True)

print(my_list)


# 6

result_start = []
i = 1
let = None
while let != '#':
    result_start.append((i, {'название': input('Введите название: '),
                             'цена': int(input('Введите цену: ')),
                             'количество': int(input('Введите количество: ')),
                             'ед': input('Введите еденицу: ')}))
    let = input('Если хотите завершить ввод - введите # ')
    i += 1

result_agr = {'название': [], 'цена': [], 'количество': [], 'ед': []}

for elem in sorted(cp.deepcopy(result_start)):
    result_agr['название'].append(elem[1]['название'])
    result_agr['цена'].append(elem[1]['цена'])
    result_agr['количество'].append(elem[1]['количество'])
    result_agr['ед'].append(elem[1]['ед'])


print('Не агрегированные данные: ', result_start)
print('Агрегированные данные: ', result_agr)