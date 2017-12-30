# -*- coding: utf-8 -*-
import pytest

from fixtures import redis_instance, add_test_params

from background_worker_lib import Queue


def test_create_queue(redis_instance):
    queue = Queue(connect=redis_instance)


def test_queue_has_method_add():
    assert hasattr(Queue, 'add')


def test_add(redis_instance, add_test_params):
    queue = Queue(connect=redis_instance)
    queue.add(
        add_test_params['job_name'],
        *add_test_params['args'],
        **add_test_params['kwargs']
    )


def test_queue_has_method_pop_job_id():
    assert hasattr(Queue, 'pop_job_id')


@pytest.mark.skip(reason="Пока отсутствует настройка окружения")
def test_method_pop_job_id(redis_instance):
    queue = Queue(connect=redis_instance)
    assert isinstance(queue.pop_job_id(), int)


def test_queue_has_method_pop_job():
    assert hasattr(Queue, 'pop_job')


@pytest.mark.skip(reason="Пока отсутствует настройка окружения")
def test_queue_pop_job(redis_instance):
    queue = Queue(connect=redis_instance)
    job_info = queue.pop_job(job_id)
    assert isinstance(job_info, dict)
    assert 'job_name' in job_info
    assert 'args' in job_info
    assert 'kwargs' in job_info
