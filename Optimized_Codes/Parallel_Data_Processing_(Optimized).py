import csv
import time
import tracemalloc
import multiprocessing
from functools import partial

# Function to process a chunk of data
def process_chunk(data_chunk, result_queue):
    processed_data = [x**2 for x in data_chunk]  # Example: Square each element
    result_queue.put(processed_data)

def parallel_data_processing(data_file, num_processes):
    start_time = time.perf_counter_ns()
    tracemalloc.start()

    # Read the data from the file
    with open(data_file, 'r') as file:
        reader = csv.reader(file)
        data = [float(row[0]) for row in reader]

    # Create a queue to store the results
    result_queue = multiprocessing.Queue()

    # Divide the data into chunks for parallel processing
    chunk_size = len(data) // num_processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    # Create and start the processes
    processes = [
        multiprocessing.Process(target=process_chunk, args=(chunk, result_queue))
        for chunk in chunks
    ]
    for process in processes:
        process.start()

    # Collect the results from the processes
    results = []
    for _ in range(num_processes):
        results.extend(result_queue.get())

    # Wait for all processes to finish
    for process in processes:
        process.join()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter_ns()

    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB

    print(f"Data processing completed.")
    print(f"Execution Time: {execution_time / 1e6:.2f} ms")
    print(f"Memory Usage: {memory_usage:.6f} MB")
    print(f"Processed Data (first 10 elements): {results[:10]}")

if __name__ == "__main__":
    data_file = "/path/to/data.csv"
    num_processes = multiprocessing.cpu_count()  # Use all available CPU cores
    parallel_data_processing(data_file, num_processes)