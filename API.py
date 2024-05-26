import requests
import time
# Function to fetch data from a single API endpoint
import requests

def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        return None

def fetch_data_sequentially(urls):
    results = []
    for url in urls:
        data = fetch_api_data(url)
        if data is not None:
            results.append(data)
            print(f"Data fetched from {url}")
        else:
            print(f"Failed to fetch data from {url}")
    return results



def time_function(func, *args, **kwargs):
    """
    Measures the execution time of a function.
    
    Parameters:
        func (callable): The function to measure.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
        
    Returns:
        tuple: A tuple containing the result of the function and the time taken to execute.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time



# Example usage wrapped with the timing function
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
results, total_time = time_function(fetch_data_sequentially, urls)
print("Fetched data from all endpoints.")
print(f"Total time taken: {total_time:.2f} seconds")




