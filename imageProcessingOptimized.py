import numpy as np
import time
import psutil
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Define the edge detection kernel
edge_detection_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Function to apply convolution
def apply_convolution(args):
    image, kernel = args
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Initialize the output image
    convolved_image = np.zeros_like(image)

    # Apply convolution without padding
    for i in range(pad_height, image_height - pad_height):
        for j in range(pad_width, image_width - pad_width):
            convolved_image[i, j] = np.sum(image[i-pad_height:i+pad_height+1, j-pad_width:j+pad_width+1] * kernel)

    return convolved_image

# Generate random images and measure performance
image_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
execution_times = []
memory_usages = []

process = psutil.Process()

def process_image(size):
    # Generate random image
    image = np.random.randint(0, 256, (size, size), dtype=np.uint8)
    
    # Measure execution time and memory usage
    start_time = time.time()
    initial_memory = process.memory_info().rss
    convolved_image = apply_convolution((image, edge_detection_kernel))
    final_memory = process.memory_info().rss
    end_time = time.time()
    
    exec_time = end_time - start_time
    mem_usage = (final_memory - initial_memory) / 1024 / 1024  # Convert to MB
    
    print(f"Size: {size}x{size} - Time: {exec_time:.4f}s - Memory: {mem_usage:.4f}MB")
    
    return exec_time, mem_usage

# Use parallel processing only for moderately large image sizes
if __name__ == '__main__':
    with Pool() as pool:
        for size in image_sizes:
            if size >= 700:  # Use parallel processing for moderately large image sizes
                results = pool.map(process_image, [size])
                execution_times.append(results[0][0])
                memory_usages.append(results[0][1])
            else:  # For smaller and very large image sizes, process sequentially
                result = process_image(size)
                execution_times.append(result[0])
                memory_usages.append(result[1])

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(image_sizes, execution_times, marker='o', label='Execution Time (s)')
plt.xlabel('Image Size (NxN)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs Image Size')
plt.legend()
plt.grid(True)
plt.show()
