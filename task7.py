from abc import ABC, abstractmethod


# 1

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    @property
    def matr(self):
        return self.__matr

    @matr.setter
    def matr(self, matr):
        leng = len(matr[0])
        if len([el for el in map(len, matr) if el == leng]) != len(matr):
            raise Exception('Неверный формат матрицы')
        self.__matr = matr

    def __str__(self):
        res = ''
        for el in self.matr:
            res = f'{res}\n{el}'
        return res[1:]

    def __add__(self, other):
        res = []
        if list(map(len, self.matr)) != list(map(len, other.matr)):
            raise Exception('Разные по структуре матрицы')
        for i in range(len(self.matr)):
            res.append([self[i, j] + other[i, j] for j in range(len(self.matr[0]))])
        return Matrix(res)

    def __getitem__(self, item1):
        i, j = item1
        return self.matr[i][j]


matr1 = Matrix([[1, 6, 7], [5, 2, 7]])
matr2 = Matrix([[1, 4, 5], [2, 3, 1]])
matr3 = matr1 + matr2
print(matr3)


# 2


class Clothes(ABC):
    @abstractmethod
    def calc_size_one(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        self.__v = v

    def calc_size_one(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    def calc_size_one(self):
        return 2 * self.h + 0.3


class Container:
    def __init__(self):
        self.__lst = []

    @property
    def lst(self):
        return self.__lst

    @lst.setter
    def lst(self, item):
        self.__lst = item

    def calc_total_size(self):
        return sum([el.calc_size_one() for el in self.lst])

    def __iadd__(self, other):
        self.lst.append(other)
        return self


su = Suit(6)
co = Coat(10)
cont = Container()
cont += su
cont += co
print(su.calc_size_one())
print(co.calc_size_one())
print(cont.calc_total_size())


# 3


class Cells(ABC):
    count = 0

    def __init__(self):
        Cells.count += 1

    @abstractmethod
    def make_order(self, cnt):
        pass


class Cell(Cells):
    def __init__(self, nucleus_count):
        super().__init__()
        self.nucleus_count = nucleus_count

    @property
    def nucleus_count(self):
        return self.__nucleus_count

    @nucleus_count.setter
    def nucleus_count(self, item):
        self.__nucleus_count = item

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError
        return Cell(self.nucleus_count + other.nucleus_count)

    def __sub__(self, other):
        if type(other) != type(self):
            raise TypeError
        if self.nucleus_count <= other.nucleus_count:
            raise Exception('Число ячеек клетки слева меньше числа ячеек клетки справа')
        else:
            return Cell(self.nucleus_count - other.nucleus_count)

    def __mul__(self, other):
        if type(other) != type(self):
            raise TypeError
        return Cell(self.nucleus_count * other.nucleus_count)

    def __truediv__(self, other):
        if type(other) != type(self):
            raise TypeError
        return Cell(self.nucleus_count // other.nucleus_count)

    def __del__(self):
        Cells.count -= 1

    def make_order(self, cnt):
        sep = '\n'
        res = sep.join(['*' * cnt for i in range(self.nucleus_count // cnt)])
        return f'{res}{sep if self.nucleus_count // cnt and self.nucleus_count % cnt else ""}{"*" * (self.nucleus_count % cnt)}'


celli1 = Cell(6)
celli2 = Cell(3)
celli_add = celli1 + celli2
celli_sub = celli1 - celli2
celli_mul = celli1 * celli2
celli_div = celli1 / celli2
print(celli_add.make_order(3), end='\n------------------------\n')
print(celli_sub.make_order(6), end='\n------------------------\n')
print(celli_mul.make_order(7), end='\n------------------------\n')
print(celli_div.make_order(1), end='\n------------------------\n')
print(Cells.count)





























