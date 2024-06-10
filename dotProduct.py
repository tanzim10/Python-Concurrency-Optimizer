import numpy as np
import time
import matplotlib.pyplot as plt

matrix_size = 10000
chunk_size = 100  # Define chunk size to collect time data

# Generate two large random matrices
A = np.random.rand(matrix_size, matrix_size)
B = np.random.rand(matrix_size, matrix_size)

# Initialize variables to store timing data
times = []
dot_products = []
num_dot_products = 0

# Start timing the operation
start_time = time.time()

# Perform matrix multiplication in chunks
C = np.zeros((matrix_size, matrix_size))
for i in range(0, matrix_size, chunk_size):
    for j in range(0, matrix_size, chunk_size):
        for k in range(0, matrix_size, chunk_size):
            sub_start_time = time.time()
            C[i:i+chunk_size, j:j+chunk_size] += np.dot(A[i:i+chunk_size, k:k+chunk_size], B[k:k+chunk_size, j:j+chunk_size])
            sub_end_time = time.time()
            
            # Update the number of dot product calculations
            num_dot_products += chunk_size ** 3
            
            # Record the elapsed time and the number of dot product calculations
            times.append(sub_end_time - start_time)
            dot_products.append(num_dot_products)

# End timing the operation
end_time = time.time()

# Calculate the duration
total_duration = end_time - start_time

# Print the execution time
print(f"Total Execution Time: {total_duration:.2f} seconds")

# Plot the number of dot product calculations against time
plt.figure(figsize=(10, 6))
plt.plot(dot_products,times, marker='o')
plt.ylabel('Time (seconds)')
plt.xlabel('Number of Dot Product Calculations')
plt.title('Dot Product Calculations Over Time')
plt.grid(True)
plt.show()
