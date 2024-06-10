#!/usr/bin/env python3
"""
    A module that measures the total execution time for wait_n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
        A function that measures the total execution time for wait_n
    """
    prev_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - prev_time) / n
