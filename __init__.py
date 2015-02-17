# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2014-2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from .async import Async, task    # noqa


def register():
    Pool.register(
        Async,
        module='async', type_='model'
    )
