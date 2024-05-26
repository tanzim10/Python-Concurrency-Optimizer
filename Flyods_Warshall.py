import numpy as np

def floyd_warshall(weights, num_vertices):
    # Initialize the distance matrix with a copy of the weights matrix
    distance = weights.copy()
    
    # Apply Floyd-Warshall algorithm to calculate shortest paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

import time
import psutil

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

    return result



def main():
    num_vertices = 200  # Number of vertices in the graph
    INF = float('inf')  # Infinite cost representing no direct path

    # Generate random integer weights between 1 and 9, then convert to float
    weights = np.random.randint(1, 10, size=(num_vertices, num_vertices)).astype(float)

    # Randomly assign roughly 10% of the weights to be INF
    mask = np.random.rand(num_vertices, num_vertices) < 0.1  # 10% chance
    weights[mask] = INF

    # Ensure diagonal elements are 0 (no self-loop costs)
    np.fill_diagonal(weights, 0)

    # Optional: Print some weights to verify
    print("Sample weights matrix:")
    print(weights[:5, :5])  # Print a 5x5 submatrix for inspection

    # Measure the Floyd-Warshall algorithm's performance
    measure_execution_time_and_memory(floyd_warshall, weights, num_vertices)

if __name__ == "__main__":
    main()


