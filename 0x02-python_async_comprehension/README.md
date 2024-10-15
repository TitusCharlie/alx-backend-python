# 0x02. Python Async Comprehension

## Project Overview
This project demonstrates the use of asynchronous comprehensions in Python.
It consists of three main tasks:

1. **Task 0: async_generator.py**
   - This coroutine generates 10 random numbers between 0 and 10 asynchronously,
     yielding one number per second.

2. **Task 1: async_comprehension.py**
   - This coroutine collects 10 random numbers from the `async_generator` using
     an async comprehension.

3. **Task 2: measure_runtime.py**
   - This coroutine measures the runtime of running `async_comprehension` four times
     in parallel.

## Requirements
- Python 3.7 on Ubuntu 18.04 LTS.
- Code follows pycodestyle guidelines (version 2.5.x).
- All functions and coroutines are type-annotated.
- All modules and functions have proper documentation.

## How to Run
- To run the async generator:
  ```bash
  python3 async_generator.py
