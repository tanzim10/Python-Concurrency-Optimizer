import time
import psutil
import numpy as np

def knapsack(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

def measure_execution_time_and_memory(func, *args, **kwargs):
    process = psutil.Process()
    start_time = time.time()
    start_memory = process.memory_info().rss
    
    result = func(*args, **kwargs)
    
    end_memory = process.memory_info().rss
    end_time = time.time()
    
    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory
    
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(f"Memory Usage: {memory_usage} bytes, approximately {memory_usage / 1024 ** 2:.2f} MB")

def main():
    np.random.seed(42)
    n = 500  # Increase the size of the problem
    W = 1000  # Increase the capacity of the knapsack
    val = np.random.randint(1, 100, size=n)
    wt = np.random.randint(1, 50, size=n)
    
    measure_execution_time_and_memory(knapsack, W, wt, val, n)

if __name__ == "__main__":
    main()
