# -*- coding: utf-8 -*-
import fabric.api

@fabric.api.task
def fail():
    """
    💥
    """
    print("💥")
