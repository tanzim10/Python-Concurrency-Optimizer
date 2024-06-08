import numpy as np
import time
from memory_profiler import memory_usage

matrix_size = 10000

# Generate two large random matrices
A = np.random.rand(matrix_size, matrix_size)
B = np.random.rand(matrix_size, matrix_size)

# Start timing the operation
start_time = time.time()
mem_usage_before = memory_usage()[0]

# Perform matrix multiplication
C = np.dot(A, B)

# End timing the operation
end_time = time.time()
mem_usage_after = memory_usage()[0]

# Calculate the duration
duration = end_time - start_time
mem_usage = mem_usage_after - mem_usage_before

print(f"Execution Time: {duration:.2f} seconds")
print(f"Memory Usage: {mem_usage:.2f} MiB")
