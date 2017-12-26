# -*- coding: utf-8 -*-

from redis import Redis
from ..queue import Queue


class Worker:

    def __init__(self, connect: Redis, name_queue=None):
        self.queue = Queue(connect=connect, name=name_queue)

    def start(self):
        queue_name = '%s%s' % (self.prefix, list(self.tasks.keys())[0])
        while True:
            raw_tasks_info = self.redis_client.blpop(queue_name)
