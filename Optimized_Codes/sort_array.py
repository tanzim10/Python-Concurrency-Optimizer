import urllib.request
import json
import time
import tracemalloc
import random
from concurrent.futures import ThreadPoolExecutor

# Function to perform Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function to fetch data from a public API using urllib
def fetch_api_data(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        return json.loads(data)

# Generate a random array of size 100
array = random.sample(range(0, 1000), 100)

# Public API URL for fetching sample data
api_url = "https://jsonplaceholder.typicode.com/posts"

# Measure compile time
compile_start_time = time.time()
compile_end_time = time.time()
compile_time = compile_end_time - compile_start_time

# Start measuring execution time and memory usage
start_time = time.time()
tracemalloc.start()

# Create a ThreadPoolExecutor to perform tasks concurrently
with ThreadPoolExecutor() as executor:
    # Schedule the tasks and get the future objects
    future_sort = executor.submit(merge_sort, array.copy())
    future_api = executor.submit(fetch_api_data, api_url)

    # Wait for the results
    sorted_array = future_sort.result()
    api_data = future_api.result()

# Stop measuring execution time and memory usage
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Calculate the execution time
execution_time = end_time - start_time

# Print the results
print("\nOriginal array:", array)
print("\n\nSorted array:", sorted_array)
print("\n\nAPI data:", api_data[:5])  # Print first 5 items from the API response for brevity
print(f"\n\nCompile time: {compile_time:.6f} seconds")
print(f"\n\nExecution time: {execution_time:.6f} seconds")
print(f"\n\nCurrent memory usage: {current / 10**6:.6f} MB")
print(f"\n\nPeak memory usage: {peak / 10**6:.6f} MB")
