import random as rd
from threading import Timer
import os
from abc import ABC
from time import sleep


class LotoCards:
    def __init__(self, name=None, hard_level=100):
        self.change_card()

    def __getitem__(self, item):
        i, j = item
        return self.card[i][j]

    @property
    def card(self):
         return self.__card

    @card.setter
    def card(self, num):
        self.__card = num

    def change_card(self):
        """
        Refresh card

        :return: new card
        """
        buf_mas, buf_mas_res = [], []
        buf_pos, buf_pos_res = [], []
        buf_flaten = []
        while sum(map(buf_flaten.count, buf_flaten)) != 27:
            buf_mas_res, buf_pos_res = [], []
            for i in range(3):
                while sum(map(buf_mas.count, buf_mas)) != 9 or sum(map(buf_pos.count, buf_pos)) != 5:
                    buf_pos = sorted([rd.randint(0, 8) for _ in range(5)])
                    buf_mas = sorted([rd.randint(1, 99) for _ in range(9)])
                buf_mas_res.append(buf_mas)
                buf_pos_res.append(buf_pos)
                buf_mas, buf_pos = [], []
            buf_flaten = [buf_mas_res[j][i] for j in range(3) for i in range(9) if buf_mas_res[j][i] != '  ']
        self.card = [[buf_mas_res[j][i] if i in buf_pos_res[j] else '  ' for i in range(9)] for j in range(3)]

    def __str__(self):
        return '\n'.join(['  '.join(map(lambda x: ' '+x if len(x) < 2 and x != '  ' else x, map(str, self.card[i]))) for i in range(len(self.card))])


class LotoSession:

    def __init__(self, time=5, user_name=None, error_prob=0, file_stat='stat.txt'):
        self.time_round = time
        self.user_name = user_name
        self.__user_cross = 0
        self.__comp_cross = 0
        self.__error_prob = error_prob
        self.__file_stat = file_stat

    @property
    def error_prob(self):
        return self.__error_prob

    @error_prob.setter
    def error_prob(self, error_prob):
        if error_prob < 0 or error_prob > 100:
            raise Exception('Неправильный уровень сложности')
        else:
            self.__error_prob = error_prob

    @property
    def time_round(self):
        return self.__time_round

    @time_round.setter
    def time_round(self, time):
        self.__time_round = time

    @staticmethod
    def __input(x, t):
        """
        Input method

        :param x: type answer
        :param t: timeout
        :return: user input
        """
        return input(f'Введите {x} за {t} секунд: ').lower()

    def start_game(self):
        """
        Start game method

        """
        self.__user = LotoCards(self.user_name)
        self.__comp = LotoCards('Computer')
        self.__continue_game()

    @staticmethod
    def __gen_boch():
        while True:
            yield rd.randint(1, 99)

    def __continue_game(self):
        """
        Main game method

        """
        for boch in self.__gen_boch():
            t = Timer(self.__time_round, os._exit, [0])
            t.start()
            print(f'Карта {self.user_name}:')
            print(self.__user)
            print('Карта компьютера:')
            print(self.__comp)
            print(f'Бочонок {boch}')
            try:
                answer = self.__input('ответ(y/n)', self.__time_round)
            finally:
                t.cancel()
                del t
            answer_comp = self.__comp_check(self.__comp, boch, self.error_prob)
            print(f'Ответ компьютера {answer_comp}')
            buf_u = self.__check_answ(self.__user, boch, answer, self.user_name)
            buf_c = self.__check_answ(self.__comp, boch, answer_comp, 'computer')
            if buf_u == -1 and buf_c != -1 or self.__comp_cross == 15:
                print(f'{self.user_name} проиграл! Количество зачеркиваний: {self.__user_cross}')
                self.__write_statistic('проиграл')
                break
            elif self.__user_cross == 15 and self.__comp_cross != 15 or buf_c == -1 and buf_u != -1:
                print(f'{self.user_name} выиграл! Количество зачеркиваний: {self.__user_cross}')
                self.__write_statistic('победил')
                break
            elif self.__user_cross == 15 and self.__comp_cross == 15 or buf_u == -1 and buf_c == -1:
                print(f'Ничья! Количество зачеркиваний: {self.__user_cross}')
                self.__write_statistic('сыграл в нечью')
                break

    def __write_statistic(self, win):
        """
        This method write statistic in file

        :param win: fail or win
        """
        try:
            ln = self.count_lines(self.__file_stat)+1
        except FileNotFoundError:
            ln = 1
        with open(self.__file_stat, 'a+', encoding='utf-8') as f:
            f.write(f'\n{ln}.{self.user_name} {win}! Количество зачеркиваний: {self.__user_cross}, таймаут на ответ: {self.time_round}, вероятность ошибки компьютера {self.error_prob}%')

    @staticmethod
    def count_lines(filename, chunk_size=1 << 13):
        """
        Calculate count lines in file

        :param filename: file name
        :return: count lines
        """
        with open(filename) as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))


    @staticmethod
    def __request_y(def_us, number):
        """
        Define true or false user answer, when user answer = y

        :param def_us: user card
        :param number: boch number
        :return: user win or fail
        """
        flatten = [def_us[j, i] for j in range(3) for i in range(9)]
        if number not in flatten:
            return -1
        else:
            return [[def_us[j, i] if number != def_us[j, i] else '-' for i in range(9)] for j in range(3)]

    @staticmethod
    def __request_n(def_us, number):
        """
            Define true or false user answer, when user answer = n

            :param def_us: user card
            :param number: boch number
            :return: user win or fail
        """
        flatten = [def_us[j, i] for j in range(3) for i in range(9)]
        if number in flatten:
            return 0
        else:
            return 1

    @staticmethod
    def __comp_check(comp, boch, hard_level):
        """
        Computer logic method

        :param comp: computer card
        :param boch: boch number
        :param hard_level: error probability
        :return: computer answer
        """
        flatten = [comp[j, i] for j in range(3) for i in range(9)]
        error_probab = rd.random()
        if boch in flatten:
            if error_probab < hard_level / 100:
                return 'n'
            else:
                return 'y'
        else:
            if error_probab < hard_level / 100:
                return 'y'
            else:
                return 'n'

    def __check_answ(self, user, boch, answer, user_name):
        """
        Check answer on true or false

        :param user: user card
        :param boch: boch number
        :param answer: user answer
        :param user_name: user name
        :return: fail or win
        """
        if answer == 'y':
            buf = self.__request_y(user, boch)
            if buf == -1:
                return -1
            else:
                user.card = buf
                self.__user_cross += 1
        elif answer == 'n':
            if self.__request_n(user, boch) == 0:
                return -1
        else:
            raise Exception('Неправильно введен ответ')


class InitGame(ABC):
    @staticmethod
    def init_game():
        print('/------------------------------/')
        user_name = input('Введите имя пользователя: ')
        timeout = int(input('Введите таймаут на ответ: '))
        error_prob = int(input('Введите вероятность ошибки компьютера в процентах: '))
        session = LotoSession(timeout, user_name, error_prob)
        print('Игра начинается...')
        sleep(2)
        print('/------------------------------/')
        session.start_game()


InitGame.init_game()
















