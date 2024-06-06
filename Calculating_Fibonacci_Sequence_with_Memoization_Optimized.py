import time
import tracemalloc
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_fibonacci():
    n = 35  # Change this value to calculate a different Fibonacci number
    start_time = time.perf_counter()
    tracemalloc.start()
    
    result = fibonacci(n)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB
    
    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Execution Time: {execution_time * 1e6:.2f} μs")
    print(f"Memory Usage: {memory_usage:.6f} MB")

if __name__ == "__main__":
    calculate_fibonacci()