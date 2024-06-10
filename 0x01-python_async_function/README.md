# Asynchronous Programming in Python

This repository contains Python code examples and exercises focusing on asynchronous programming using asyncio.

## Files Description

### 0-basic_async_syntax.py

**Description:** 
This file contains an asynchronous coroutine that generates random delays and returns them. It's designed to help understand the basics of asynchronous programming in Python.

---

### 1-concurrent_coroutines.py

**Description:** 
This file implements a coroutine called `wait_n` that executes multiple instances of the coroutine from file 0 concurrently. It returns a list of delays in ascending order.

---

### 2-measure_runtime.py

**Description:** 
In this file, a function named `measure_time` is created. It calculates the total execution time for running the coroutine multiple times and returns the average time taken per execution.

---

### 3-tasks.py

**Description:** 
Here, a regular function `task_wait_random` is defined, which takes an integer parameter and returns an asyncio.Task. This demonstrates how to wrap a regular function call in an asyncio.Task.

---

### 4-tasks.py

**Description:** 
This file alters the code from file 1 into a new function named `task_wait_n`, which uses asyncio.Tasks instead of directly calling coroutines. It demonstrates the use of Tasks for asynchronous execution.

---

These files are part of a project focused on learning asynchronous programming concepts in Python. Each file builds upon the previous one, gradually introducing more advanced topics and techniques.
