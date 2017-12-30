# -*- coding: utf-8 -*-

import pytest
from redis import Redis


@pytest.fixture(scope='function')
def redis_instance():
    return Redis()


@pytest.fixture(
    scope='function',
    params=[
        {'job_name': 'hello_world', 'args': (), 'kwargs': {}, 'result': 'hello_world', },
        {'job_name': 'add', 'args': (0, -1), 'kwargs': {}, 'result': -1, },
        {'job_name': 'mult', 'args': (), 'kwargs': {'a': 1, 'b': 2}, 'result': 2, },
        {'job_name': 'mult', 'args': (3,), 'kwargs': {'b': 2}, 'result': 6, },
    ],
    ids=['without_arguments', 'with_args', 'with_kwargs', 'with_args_and_kwargs']
)
def test_params(request):
    return request.param


@pytest.fixture(scope='function')
def job_map():
    return {
        'hello_world': lambda: 'hello world',
        'add': lambda a, b: a + b,
        'mult': lambda a, b: a * b,
    }
