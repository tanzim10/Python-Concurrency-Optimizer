

import requests
import time
import matplotlib.pyplot as plt

def fetch_api_data(url):
    """Fetch data from a given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        return None

def fetch_data_sequentially(urls):
    """Fetch data sequentially from a list of URLs and record the time taken for each."""
    results = []
    times = []
    for url in urls:
        start_time = time.time()
        data = fetch_api_data(url)
        end_time = time.time()
        times.append(end_time - start_time)
        if data is not None:
            results.append(data)
            print(f"Data fetched from {url}")
        else:
            print(f"Failed to fetch data from {url}")
    return results, times

def time_function(func, *args, **kwargs):
    """Measure the total execution time of a function."""
    start_time = time.time()
    result, times = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, times, execution_time

def plot_performance(times):
    """Plot the execution time for each API call."""
    plt.figure(figsize=(10, 5))
    plt.plot(times, marker='o', linestyle='-')
    plt.title('API Request Execution Times')
    plt.xlabel('Request Index')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

# Example usage
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
results, times, total_time = time_function(fetch_data_sequentially, urls)
print("Fetched data from all endpoints.")
print(f"Total time taken: {total_time:.2f} seconds")
plot_performance(times)

