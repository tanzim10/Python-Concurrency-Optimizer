import numpy as np
import time
import psutil
import matplotlib.pyplot as plt

# Define the edge detection kernel
edge_detection_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Function to apply convolution
def apply_convolution(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Pad the image with zeros on all sides
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Initialize the output image
    convolved_image = np.zeros_like(image)

    # Perform convolution
    for i in range(image_height):
        for j in range(image_width):
            convolved_image[i, j] = np.sum(padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)

    return convolved_image

# Generate random images and measure performance
image_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
execution_times = []
memory_usages = []

process = psutil.Process()

for size in image_sizes:
    # Generate random image
    image = np.random.randint(0, 256, (size, size), dtype=np.uint8)
    
    # Measure execution time and memory usage
    start_time = time.time()
    initial_memory = process.memory_info().rss
    convolved_image = apply_convolution(image, edge_detection_kernel)
    final_memory = process.memory_info().rss
    end_time = time.time()
    
    exec_time = end_time - start_time
    mem_usage = (final_memory - initial_memory) / 1024 / 1024  # Convert to MB
    
    execution_times.append(exec_time)
    memory_usages.append(mem_usage)
    
    print(f"Size: {size}x{size} - Time: {exec_time:.4f}s - Memory: {mem_usage:.4f}MB")

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(image_sizes, execution_times, marker='o', label='Execution Time (s)')
plt.xlabel('Image Size (NxN)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs Image Size')
plt.legend()
plt.grid(True)
plt.show()
