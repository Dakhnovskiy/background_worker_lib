# -*- coding: utf-8 -*-
import pickle


class Job:

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs

    @property
    def func(self):
        return self.__func

    @property
    def args_dump(self):
        return pickle.dumps(self.args)

    @property
    def kwargs_dump(self):
        return pickle.dumps(self.kwargs)

    @property
    def func_dump(self):
        return pickle.dumps(self.func)

    def __init__(self, func, *args, **kwargs):
        """
        :param func: функция для выполнения в фоновом режиме
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def execute(self):
        self.__func(*self.__args, **self.kwargs)
