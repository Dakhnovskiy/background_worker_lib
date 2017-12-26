# -*- coding: utf-8 -*-

from redis import Redis
from background_worker_lib import Queue


def foo(a, b):
    print(a + b)


if __name__ == '__main__':
    redis_connect = Redis()
    q = Queue(connect=redis_connect)
    q.add(foo, 1, 2)

    q2 = Queue(connect=redis_connect, name='q2')
    q2.add(foo, 5, 6)
