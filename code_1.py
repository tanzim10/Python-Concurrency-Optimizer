import time
from memory_profiler import memory_usage

def sample_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

# Measure memory usage before and after running the function
def mem_and_exec_test():
    
    mem_usage_before = memory_usage()[0]
    start_time = time.time()

    # Run the function
    sample_function()


    # Record the end time
    end_time = time.time()
    mem_usage_after = memory_usage()[0]

    mem_usage = mem_usage_after - mem_usage_before
    # Calculate the elapsed time
    execution_time = end_time - start_time

    print(f"Execution Time: {execution_time} seconds")
    print(f"Memory Usage: {mem_usage} MiB")

if __name__ == "__main__":
    mem_and_exec_test()
