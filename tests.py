# -*- coding: utf-8 -*-

import pytest

from redis import Redis
from background_worker_lib import Queue


@pytest.fixture(scope='function')
def redis_instance():
    return Redis()


def foo(*args, **kwargs):
    pass


@pytest.fixture(
    scope='function',
    params=[
        {'function': foo, 'args': (), 'kwargs': {}},
        {'function': foo, 'args': (1, 2), 'kwargs': {}},
        {'function': foo, 'args': (), 'kwargs': {'a': 1, 'b': 2}},
        {'function': foo, 'args': (1, 2, 3), 'kwargs': {'a': 1, 'b': 2, 'c': 3}},
    ],
    ids=['without_arguments', 'with_args', 'with_kwargs', 'with_args_and_kwargs']
)
def add_test_params(request):
    return request.param


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
