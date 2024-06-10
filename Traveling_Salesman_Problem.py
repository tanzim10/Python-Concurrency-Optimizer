import time
import psutil
import numpy as np

def tsp(graph, mask, pos, dp):
    if mask == (1 << len(graph)) - 1:
        return graph[pos][0]
    if dp[mask][pos] != -1:
        return dp[mask][pos]
    
    min_cost = float('inf')
    for city in range(len(graph)):
        if mask & (1 << city) == 0:
            new_cost = graph[pos][city] + tsp(graph, mask | (1 << city), city, dp)
            min_cost = min(min_cost, new_cost)
    dp[mask][pos] = min_cost
    return min_cost

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
    num_cities = 10
    graph = np.random.randint(1, 100, size=(num_cities, num_cities))
    dp = [[-1] * num_cities for _ in range(1 << num_cities)]
    
    measure_execution_time_and_memory(tsp, graph, 1, 0, dp)

if __name__ == "__main__":
    main()
