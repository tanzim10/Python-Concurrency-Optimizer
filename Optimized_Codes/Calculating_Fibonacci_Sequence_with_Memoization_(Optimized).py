import time
import tracemalloc
from functools import lru_cache
import matplotlib.pyplot as plt

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_fibonacci(n):
    start_time = time.perf_counter_ns()
    tracemalloc.start()
    
    result = fibonacci(n)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter_ns()
    
    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB
    
    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Execution Time: {execution_time / 1e3:.2f} μs")
    print(f"Memory Usage: {memory_usage:.6f} MB")
    
    return execution_time / 1e9  # Convert to seconds

if __name__ == "__main__":
    num_requests = 10
    execution_times = []
    fibonacci_values = range(20, 20 + num_requests)  # Fibonacci numbers to calculate
    
    for n in fibonacci_values:
        execution_time = calculate_fibonacci(n)
        execution_times.append(execution_time)
    
    # Plot the execution times
    plt.figure(figsize=(10, 6))
    plt.plot(fibonacci_values, execution_times, marker='o')
    plt.xlabel("Fibonacci Number Index")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time for Calculating Fibonacci Numbers")
    plt.grid(True)
    plt.show()
