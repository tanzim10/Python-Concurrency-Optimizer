# import requests
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed

# def fetch_api_data(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()  # Return the JSON data
#     else:
#         return None


# def fetch_data_concurrently(urls):
#     results = []
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         # Create a dictionary to hold the future objects
#         future_to_url = {executor.submit(fetch_api_data, url): url for url in urls}
#         for future in as_completed(future_to_url):
#             url = future_to_url[future]
#             try:
#                 data = future.result()
#                 if data is not None:
#                     results.append(data)
#                     print(f"Data fetched from {url}")
#                 else:
#                     print(f"Failed to fetch data from {url}")
#             except Exception as e:
#                 print(f"Error fetching data from {url}: {e}")
#     return results


# def time_function(func, *args, **kwargs):
   
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()
#     execution_time = end_time - start_time
#     return result, execution_time


# urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
# results, total_time = time_function(fetch_data_concurrently, urls)
# print("Fetched data from all endpoints.")
# print(f"Total time taken: {total_time:.2f} seconds")

import requests
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_api_data(url):
    """Fetch data from a given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        return None

def fetch_data_concurrently(urls):
    """Fetch data concurrently from a list of URLs and record the time taken for each."""
    results = []
    times = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(fetch_api_data, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            start_time = time.time()
            try:
                data = future.result()
                if data is not None:
                    results.append(data)
                    print(f"Data fetched from {url}")
                else:
                    print(f"Failed to fetch data from {url}")
            except Exception as e:
                print(f"Error fetching data from {url}: {e}")
            end_time = time.time()
            times.append(end_time - start_time)
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
    plt.plot(times, marker='o', linestyle='-', color='b')
    plt.title('API Request Execution Times')
    plt.xlabel('Request Index')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

# Example usage
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
results, times, total_time = time_function(fetch_data_concurrently, urls)
print("Fetched data from all endpoints.")
print(f"Total time taken: {total_time:.2f} seconds")
plot_performance(times)