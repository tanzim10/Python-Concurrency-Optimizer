import numpy as np
import time
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
from concurrent.futures import ProcessPoolExecutor

def matrix_multiply_chunk(A_chunk, B, start_row, end_row):
    """Multiplies a chunk of matrix A with matrix B and returns the result."""
    C_chunk = np.zeros((end_row - start_row, B.shape[1]))
    for i in range(end_row - start_row):
        C_chunk[i, :] = np.dot(A_chunk[i, :], B)
    return C_chunk

def parallel_matrix_multiplication(A, B, num_workers):
    """Divides the matrix multiplication task into chunks and processes them in parallel."""
    matrix_size = A.shape[0]
    chunk_size = matrix_size // num_workers

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i in range(num_workers):
            start_row = i * chunk_size
            end_row = (i + 1) * chunk_size if i != num_workers - 1 else matrix_size
            A_chunk = A[start_row:end_row, :]
            futures.append(executor.submit(matrix_multiply_chunk, A_chunk, B, start_row, end_row))

        results = []
        dot_products = []
        times = []
        num_dot_products = 0
        start_time = time.time()

        for future in futures:
            result = future.result()
            end_time = time.time()
            
            # Update the number of dot product calculations
            num_dot_products += result.shape[0] * B.shape[1]
            
            # Record the elapsed time and the number of dot product calculations
            times.append(end_time - start_time)
            dot_products.append(num_dot_products)
            
            results.append(result)

    # Combine the results
    C = np.vstack(results)
    return C, times, dot_products

if __name__ == "__main__":
    matrix_size = 1000  
    num_workers = 4  # Adjust the number of workers as needed

    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)

    start_time = time.time()
    mem_usage_before = memory_usage()[0]

    C, times, dot_products = parallel_matrix_multiplication(A, B, num_workers)

    mem_usage_after = memory_usage()[0]
    end_time = time.time()

    mem_usage = mem_usage_after - mem_usage_before
    execution_time = end_time - start_time  # Total execution time
    print(f"Memory Usage: {mem_usage:.2f} MiB")
    print(f"\n\nExecution Time: {execution_time:.4f} seconds")

    # Plot the number of dot product calculations against time
    plt.figure(figsize=(10, 6))
    plt.plot(dot_products,times, marker='o')
    plt.ylabel('Time (seconds)')
    plt.xlabel('Number of Dot Product Calculations')
    plt.title('Dot Product Calculations Over Time')
    plt.grid(True)
    plt.show()
