import json


class Job:

    def __init__(self, func: function, *args, **kwargs):
        """
        :param func: функция для выполнения в фоновом режиме
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        self.__func = func
        self.__args_dump = json.dumps(args)
        self.__kwargs_dump = json.dumps(kwargs)
