import os
import time
import tracemalloc
from concurrent.futures import ThreadPoolExecutor

def search_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def parallel_file_search(directories, filename):
    start_time = time.time()
    tracemalloc.start()
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_file, directory, filename) for directory in directories]
        results = [future.result() for future in futures]
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB
    
    print(f"File paths: {[path for path in results if path is not None]}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Memory Usage: {memory_usage:.6f} MB")

if __name__ == "__main__":
    directories = ["/path/to/dir1", "/path/to/dir2", "/path/to/dir3"]
    filename = "example.txt"
    parallel_file_search(directories, filename)