# -*- coding: utf-8 -*-

import traceback

from redis import Redis
from ..queue import Queue


class Worker:

    def __init__(self, connect: Redis, name_queue=None, job_map=None):
        self.__job_map = job_map or {}
        self.queue = Queue(connect=connect, name=name_queue)

    def execute_job(self, job_name, args, kwargs):
        func = self.__job_map[job_name]
        return func(*args, **kwargs)

    def start(self):

        while True:
            job_id = self.queue.pop_job_id()
            try:
                job_info = self.queue.pop_job(job_id)
                self.execute_job(**job_info)
            except:
                # TODO: использовать logging
                traceback.print_exc()
