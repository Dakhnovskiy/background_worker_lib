# -*- coding: utf-8 -*-

from fixtures import redis_instance, add_test_params

from background_worker_lib import Queue


def test_create_queue(redis_instance):
    queue = Queue(connect=redis_instance)


def test_queue_has_method_add():
    assert (hasattr(Queue, 'add'))


def test_add(redis_instance, add_test_params):
    queue = Queue(connect=redis_instance)
    queue.add(
        add_test_params['function'],
        *add_test_params['args'],
        **add_test_params['kwargs']
    )
