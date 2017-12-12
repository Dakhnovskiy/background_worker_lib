# -*- coding: utf-8 -*-
from redis import Redis
from .job import Job


class Queue:

    __queue_prefix = 'queue:'
    __queues_key = 'queues'
    __jobs_key = 'jobs'

    @property
    def job_id_key(self):
        return '{0}:job_id'.format(self.__key)

    @property
    def jobs_key(self):
        return '{0}:{1}'.format(self.__key, self.__jobs_key)

    @property
    def job_prefix(self):
        return '{0}:job:{{0}}:{{1}}'.format(self.__key)

    @property
    def next_job_id(self):
        return int(self.__connect.incr(self.job_id_key))

    def __init__(self, connect: Redis, name=None):
        if name is None:
            name = 'queue'

        self.__key = '{0}{1}'.format(self.__queue_prefix, name)
        self.__connect = connect

        self.__init_job_id()

    def __init_job_id(self):
        job_id = self.__connect.get(self.job_id_key)
        if job_id is None:
            self.__connect.set(self.job_id_key, 0)

    def add(self, func, *args, **kwargs):
        """
        Добавить "задачу" в очередь
        :param func: функция для выполнения в фоновом режиме
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        assert callable(func), 'func must be callable'

        self.__connect.sadd(self.__queues_key, self.__key)

        job = Job(func, *args, **kwargs)
        job_id = self.next_job_id

        self.__connect.rpush(self.jobs_key, job_id)
        self.__connect.rpush(self.job_prefix.format(job_id, 'args'), job.args)
        self.__connect.rpush(self.job_prefix.format(job_id, 'kwargs'), job.kwargs)
