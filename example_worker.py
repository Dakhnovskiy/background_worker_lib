# -*- coding: utf-8 -*-

from redis import Redis
from background_worker_lib import Worker


if __name__ == '__main__':
    redis_connect = Redis()
    worker = Worker(connect=redis_connect)
    worker.start()
