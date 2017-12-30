# -*- coding: utf-8 -*-

from redis import Redis
from background_worker_lib import Worker


job_map = {
    'add': lambda a, b: print(a+b),
    'mult': lambda a, b: print(a*b)
}

if __name__ == '__main__':
    redis_connect = Redis()
    worker = Worker(connect=redis_connect, name_queue='queue_add', job_map=job_map)
    worker.start()
