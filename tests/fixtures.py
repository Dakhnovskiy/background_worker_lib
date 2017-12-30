# -*- coding: utf-8 -*-

import pytest
from redis import Redis


@pytest.fixture(scope='function')
def redis_instance():
    return Redis()


@pytest.fixture(
    scope='function',
    params=[
        {'job_name': 'add', 'args': (), 'kwargs': {}},
        {'job_name': 'add', 'args': (1, 2), 'kwargs': {}},
        {'job_name': 'foo', 'args': (), 'kwargs': {'a': 1, 'b': 2}},
        {'job_name': 'foo', 'args': (1, 2, 3), 'kwargs': {'a': 1, 'b': 2, 'c': 3}},
    ],
    ids=['without_arguments', 'with_args', 'with_kwargs', 'with_args_and_kwargs']
)
def add_test_params(request):
    return request.param