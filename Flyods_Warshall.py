
import numpy as np
import time
import psutil
import matplotlib.pyplot as plt

def floyd_warshall(weights, num_vertices):
    distance = weights.copy()
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

def measure_execution_time_and_memory(func, *args, **kwargs):
    process = psutil.Process()
    start_time = time.time()
    start_memory = process.memory_info().rss
    result = func(*args, **kwargs)
    end_memory = process.memory_info().rss
    end_time = time.time()
    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory
    return execution_time, memory_usage

def plot_performance(vertex_range):
    times = []
    for num_vertices in vertex_range:
        weights = np.random.randint(1, 10, size=(num_vertices, num_vertices)).astype(float)
        mask = np.random.rand(num_vertices, num_vertices) < 0.1
        weights[mask] = float('inf')
        np.fill_diagonal(weights, 0)
        execution_time, _ = measure_execution_time_and_memory(floyd_warshall, weights, num_vertices)
        times.append(execution_time)
        print(f"Processed graph with {num_vertices} vertices in {execution_time:.4f} seconds.")

    plt.figure(figsize=(10, 5))
    plt.plot(vertex_range, times, marker='o', linestyle='-', color='b')
    plt.title('Execution Time for Floyd-Warshall Algorithm')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

def main():
    vertex_range = range(200, 1001, 100)  # Test from 200 to 1000 vertices
    plot_performance(vertex_range)

if __name__ == "__main__":
    main()


