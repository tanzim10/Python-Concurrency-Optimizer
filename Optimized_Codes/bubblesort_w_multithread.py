import random
import time
import psutil
from concurrent.futures import ThreadPoolExecutor
import heapq

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Return the sorted array

def parallel_bubble_sort(arr, num_threads=4):
    chunk_size = len(arr) // num_threads
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        sorted_chunks = list(executor.map(bubble_sort, chunks))
    
    return merge_sorted_chunks(sorted_chunks)

def merge_sorted_chunks(chunks):
    # Simple merging process for sorted chunks
    return list(heapq.merge(*chunks))

def measure_execution_time_and_memory(func, *args, **kwargs):
    """
    Measures the execution time and memory usage of a passed function.
    """
    process = psutil.Process()
    start_time = time.time()
    start_memory = process.memory_info().rss  # Memory usage before execution
    
    print("Original Array")
    print(*args)
    sorted_arr = func(*args, **kwargs)  # Execute the function
    print("\nSorted array:")
    print(sorted_arr)
    end_memory = process.memory_info().rss  # Memory usage after execution
    end_time = time.time()
    
    execution_time = end_time - start_time  # Total execution time
    memory_usage = end_memory - start_memory  # Total memory used

    print(f"\n\nExecution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage} bytes, approximately {memory_usage / 1024 ** 2:.2f} MB")

if __name__ == "__main__":
    array1 = [random.uniform(0, 100) for _ in range(10000)]
    measure_execution_time_and_memory(parallel_bubble_sort, array1)
