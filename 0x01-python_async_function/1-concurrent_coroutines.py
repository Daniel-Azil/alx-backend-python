#!/usr/bin/env python3
"""
    A module that return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
        A coroutine that takes in 2 arguments and returns a list of delays
    """
    var_list_1 = []
    var_list_2 = []
    for i in range(n):
        var_list_1.append(wait_random(max_delay))
    for t in asyncio.as_completed(var_list_1):
        var_list_2.append(await t)
    return var_list_2
