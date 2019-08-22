# -*- coding: utf-8 -*-
import fabric.api

from .fail import fail


@fabric.api.task
def ok():
    """
    👍
    """
    print("👍")

