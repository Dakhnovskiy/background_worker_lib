# -*- coding: utf-8 -*-

from redis import Redis
from background_worker_lib import Queue


def foo(a, b):
    return a + b


if __name__ == '__main__':
    r = Redis()
    q = Queue(connect=r)
    q.add(foo, 1, 2)

    q2 = Queue(connect=r, name='q2')
    q2.add(foo, 1, 2)
