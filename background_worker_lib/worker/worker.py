# -*- coding: utf-8 -*-

from redis import Redis
from ..queue import Queue


class Worker:

    def __init__(self, connect: Redis, name_queue=None):
        self.queue = Queue(connect=connect, name=name_queue)

    def start(self):
        pass
