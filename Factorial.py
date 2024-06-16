import time
import sys
import os

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def get_memory_usage():
    """
    Returns the current memory usage of the process in MB.
    """
    try:
        with open('/proc/self/stat', 'r') as f:
            stats = f.read().split()
            vsize = int(stats[22])  # Virtual memory size in bytes
            return vsize / (1024 ** 2)  # Convert to MB
    except (IOError, IndexError):
        return 0.0  # Fallback to 0 if the memory usage cannot be determined

def measure_execution_time_and_memory(func, *args, **kwargs):
    """
    Measures the execution time and memory usage of a function.
    """
    start_time = time.time()
    start_memory = get_memory_usage()

    result = func(*args, **kwargs)

    end_time = time.time()
    end_memory = get_memory_usage()

    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory

    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage:.2f} MB")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    measure_execution_time_and_memory(factorial, n)