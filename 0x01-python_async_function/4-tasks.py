#!/usr/bin/env python3
"""
    A module that returns a list of asyncio.Task
"""
from typing import List
import asyncio
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
        A coroutine that takes in 2 arguments and returns a list of delays
    """
    var_list_1 = []
    var_list_2 = []
    for i in range(n):
        var_list_1.append(task_wait_random(max_delay))
    for t in asyncio.as_completed(var_list_1):
        var_list_2.append(await t)
    return var_list_2
