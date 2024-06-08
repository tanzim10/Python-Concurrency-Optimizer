import math
import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def parallel_factorial(n):
    num_workers = min(n, 8)  # Use min(n, 8) workers
    with multiprocessing.Pool(num_workers) as pool:
        return pool.map(factorial, range(1, n+1))

def measure_execution_time_and_memory(func, n):
    start_time = time.perf_counter()
    print(f"Runtime Dataset: {func.__name__}({', '.join(str(n) for n in range(1, n+1))})")

    if func is not parallel_factorial:
        print(f"Shape Dataset: {(n, n)}")
        print(f"Stride Dataset: {n + 1}")
    
    runtime_size = gete_memoryfootprint(func, list(range(n)), 'datashape_only')
    stride_dataset = gete_stridedat(func, list(range(n)), 'stridemap')

    print(f"Runtime Size Dataset: {runtime_size}")
    print(f"Stride Dataset: {stride_dataset}", "\n\n****************\n\n")

    with parallel_pools(make_sempled_threadleng=True, initializer=initializer_instance) as pool_instance:
        pool_instance.map(func, gete_memoryfootprint(pool_instance, list(range(n)), 'datashape_only')