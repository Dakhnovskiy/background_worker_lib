# -*- coding: utf-8 -*-

import pickle as serialize_lib


def dumps(obj):
    return serialize_lib.dumps(obj)


def loads(obj):
    return serialize_lib.loads(obj)
