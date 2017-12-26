# -*- coding: utf-8 -*-

import traceback

from redis import Redis
from ..queue import Queue


class Worker:

    def __init__(self, connect: Redis, name_queue=None):
        self.queue = Queue(connect=connect, name=name_queue)

    def start(self):

        while True:
            job_id = self.queue.pop_job_id()
            try:
                job = self.queue.pop_job(job_id)
                job.execute()
            except:
                # TODO: использовать logging
                traceback.print_exc()
