"""
User story class
"""

import datetime

class MyUserStory(object):
    name = None
    id = None
    state = 0  # 1 выбрал цвет, 2 выбрал ввести свой смысл, 3 смысл определён
    state_actions = [['Сделай выбор:', [('Красное', 'red'), ('Зелёное', 'green')]],
                     ['В чём смысл жизни?', [('42', '42'), ('Другой', 'user')]],
                     ['Напиши свой смысл: ', []],
                     ['Выбор сделан ', [('Заново', '0')]]]
    message = ''
    choise = None
    idea = None
    our_date = None
    celebrated = []

    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.our_date = datetime.datetime.now()

    def get_user_buttons(self):
        """
        отправляет набор кнопок для вывода пользователю в виде списка названий и кодов реакции
        :return: список
        """
        self.message = self.state_actions[self.state][0]
        if self.state == 3:
            self.message = self.message + self.idea
        return self.state_actions[self.state][1]

    def set_user_reaction(self, reaction):
        """
        получает реакцию пользователя, меняет состояние объекта пользователя
        :param reaction:
        :return: ничего
        """
        if self.state == 0:
            self.state = 1
            self.choise = reaction
        elif self.state == 1:
            if reaction == '42':
                self.state = 3
                self.idea = '42'
            else:
                self.state = 2
        elif self.state == 2:
            self.state = 3
            self.idea = reaction

        if reaction == '0':
            self.state = 0
