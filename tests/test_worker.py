# -*- coding: utf-8 -*-

from fixtures import redis_instance, test_params, job_map

from background_worker_lib import Worker
from background_worker_lib import Queue


def test_create_worker(redis_instance):
    worker = Worker(connect=redis_instance)


def test_worker_instance_has_attribute_queue(redis_instance):
    worker = Worker(connect=redis_instance)
    assert hasattr(worker, 'queue')
    assert isinstance(worker.queue, Queue)


def test_worker_has_start_method():
    assert hasattr(Worker, 'start')


def test_worker_has_execute_job_method():
    assert hasattr(Worker, 'execute_job')


def test_worker_execute_job(redis_instance, job_map, test_params):
    worker = Worker(connect=redis_instance, job_map=job_map)
    result = worker.execute_job(test_params['job_name'], test_params['args'], test_params['kwargs'])
    assert result, test_params['result']
