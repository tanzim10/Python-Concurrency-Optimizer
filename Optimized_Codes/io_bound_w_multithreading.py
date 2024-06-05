import os
import time
import tracemalloc
import concurrent.futures

# Function to simulate reading files
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Measure execution time and memory usage
def measure_performance(file_paths):
    start_time = time.time()
    tracemalloc.start()

    # Read files using multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(read_file, file_paths)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()

    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB

    print(f"Execution Time: {execution_time:.2f} seconds")
    print(f"Memory Usage: {memory_usage:.2f} MB")

# Function to create a file with sample content
def create_file(file_path, content, size_mb):
    with open(file_path, 'w') as file:
        while file.tell() < size_mb * 1024 * 1024:
            file.write(content)

if __name__ == "__main__":
    # Define file names and their sizes in MB
    files = {
        'file1.txt': 1,  # 1 MB
        'file2.txt': 1,  # 1 MB
        'file3.txt': 1   # 1 MB
    }
    
    # Define sample content to fill the files
    content = "This is a sample line of text.\n"

    # Use ThreadPoolExecutor to create files in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(create_file, file_name, content, size_mb) for file_name, size_mb in files.items()]

        # Ensure all files are created
        concurrent.futures.wait(futures)

    print("Sample files created successfully.")

    # Example list of files to read
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    measure_performance(files)

    
