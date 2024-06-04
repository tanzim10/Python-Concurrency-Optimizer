import numpy as np
import time
import psutil
from concurrent.futures import ProcessPoolExecutor, as_completed


def matrix_chain_order(p, i, j):
    if i == j:
        return 0
    min_cost = float('inf')
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k) +
                 matrix_chain_order(p, k + 1, j) +
                 p[i-1] * p[k] * p[j])
        if count < min_cost:
            min_cost = count
    return min_cost


def matrix_chain_order_parallel(p, i, j):
    if i == j:
        return 0
    
    min_cost = float('inf')
    
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(matrix_chain_order_task, p, i, k, j)
            for k in range(i, j)
        ]
        
        for future in as_completed(futures):
            count = future.result()
            if count < min_cost:
                min_cost = count
                
    return min_cost

def matrix_chain_order_task(p, i, k, j):
    return (matrix_chain_order(p, i, k) +
            matrix_chain_order(p, k + 1, j) +
            p[i-1] * p[k] * p[j])

def measure_execution_time_and_memory(func, *args, **kwargs):
    """
    Measures the execution time and memory usage of a passed function.
    """
    process = psutil.Process()
    start_time = time.time()
    start_memory = process.memory_info().rss  # Memory usage before execution
    
    result = func(*args, **kwargs)  # Execute the function
    
    end_memory = process.memory_info().rss  # Memory usage after execution
    end_time = time.time()
    
    execution_time = end_time - start_time  # Total execution time
    memory_usage = end_memory - start_memory  # Total memory used
    
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage} bytes, approximately {memory_usage / 1024 ** 2:.2f} MB")

def main():
    # Generate random integers for matrix dimensions (more appropriate than floating-point)
    arr = np.random.randint(2, 100, size=20)
    n = len(arr)
    
    # Measuring the matrix chain multiplication function with parallel execution
    measure_execution_time_and_memory(matrix_chain_order_parallel, arr, 1, n-1)

if __name__ == "__main__":
    main()
