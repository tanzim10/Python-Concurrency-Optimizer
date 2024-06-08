import numpy as np
import time
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

        results = [future.result() for future in futures]

    # Combine the results
    C = np.vstack(results)
    return C

if __name__ == "__main__":
    matrix_size = 1000  
    num_workers = 4  # Adjust the number of workers as needed

    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)

    start_time = time.time()
    mem_usage_before = memory_usage()[0]

    C = parallel_matrix_multiplication(A, B, num_workers)

    end_time = time.time()
    mem_usage_after = memory_usage()[0]

    duration = end_time - start_time
    mem_usage = mem_usage_after - mem_usage_before

    print(f"Execution Time: {duration:.2f} seconds")
    print(f"Memory Usage: {mem_usage:.2f} MiB")
