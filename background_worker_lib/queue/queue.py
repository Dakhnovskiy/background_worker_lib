# -*- coding: utf-8 -*-
from redis import Redis


class Queue:

    def __init__(self, connect: Redis):

        self.__connect = connect

    def add(self, func: function, *args, **kwargs):
        """
        Добавить "задачу" в очередь
        :param func: функция для выполнения в фоновом режиме
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        pass
