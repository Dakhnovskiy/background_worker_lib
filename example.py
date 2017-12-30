# -*- coding: utf-8 -*-

from redis import Redis
from background_worker_lib import Queue


if __name__ == '__main__':
    redis_connect = Redis()
    q = Queue(connect=redis_connect, name='queue_add')
    q.add('add', 1, 2)
    q.add('add', 3, 4)
    q.add('mult', 5, 6)
