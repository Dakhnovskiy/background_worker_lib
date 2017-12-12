# -*- coding: utf-8 -*-
import json


class Job:

    @property
    def args(self):
        return self.__args_dump

    @property
    def kwargs(self):
        return self.__kwargs_dump

    def __init__(self, func, *args, **kwargs):
        """
        :param func: функция для выполнения в фоновом режиме
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        self.__func = func
        self.__args_dump = json.dumps(args)
        self.__kwargs_dump = json.dumps(kwargs)
