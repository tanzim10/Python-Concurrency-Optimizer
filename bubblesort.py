import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

import time
import psutil

def measure_execution_time_and_memory(func, *args, **kwargs):
    """
    Measures the execution time and memory usage of a passed function.
    """
    process = psutil.Process()
    start_time = time.time()
    start_memory = process.memory_info().rss  # Memory usage before execution
    
    print("Original Array")
    print(*args)
    func(*args, **kwargs)  # Execute the function
    print("\nSorted array:")
    print(*args)
    end_memory = process.memory_info().rss  # Memory usage after execution
    end_time = time.time()
    
    execution_time = end_time - start_time  # Total execution time
    memory_usage = end_memory - start_memory  # Total memory used

    print(f"\n\nExecution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage} bytes, approximately {memory_usage / 1024 ** 2:.2f} MB")



if __name__ == "__main__":
    array1 = [random.uniform(0, 100) for _ in range(100)]
    measure_execution_time_and_memory(bubble_sort,array1)
