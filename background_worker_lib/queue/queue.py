# -*- coding: utf-8 -*-

from .helpers_serialize import loads, dumps
from redis import Redis


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
            
    def __get_job_field_name(self, job_id, field_name):
        return self.job_prefix.format(job_id, field_name)

    def __lpop(self, key):
        return self.__connect.lpop(key)

    def __rpush(self, key, value):
        return self.__connect.rpush(key, value)

    def add(self, job_name, *args, **kwargs):
        """
        Добавить "задачу" в очередь
        :param job_name: название джоба на стороне воркера
        :param args: позиционные аргументы функции
        :param kwargs: именованные аргументы функции
        """

        self.__connect.sadd(self.__queues_key, self.__key)

        job_id = self.next_job_id

        self.__rpush(self.__get_job_field_name(job_id, 'args'), dumps(args))
        self.__rpush(self.__get_job_field_name(job_id, 'kwargs'), dumps(kwargs))
        self.__rpush(self.__get_job_field_name(job_id, 'job_name'), dumps(job_name))
        self.__rpush(self.jobs_key, job_id)

    def pop_job_id(self):
        job_id = self.__connect.blpop(self.jobs_key)
        return int(job_id[1].decode('utf-8'))

    def pop_job(self, job_id):
        raw_args = self.__lpop(self.__get_job_field_name(job_id, 'args'))
        raw_kwargs = self.__lpop(self.__get_job_field_name(job_id, 'kwargs'))
        raw_job_name = self.__lpop(self.__get_job_field_name(job_id, 'job_name'))

        args = loads(raw_args)
        kwargs = loads(raw_kwargs)
        job_name = loads(raw_job_name)

        return {
            'job_name': job_name,
            'args': args,
            'kwargs': kwargs
        }
