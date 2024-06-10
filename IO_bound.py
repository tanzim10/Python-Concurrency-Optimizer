import os
import time


# Function to simulate reading files
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

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
        'file3.txt': 1,
        'file4.txt': 1,
        'file5.txt': 1,
        'file6.txt': 1,
        'file7.txt': 1,
        'file8.txt': 1,
        'file9.txt': 1,
        'file10.txt': 1   # 1 MB
    }
    
    # Define sample content to fill the files
    content = "This is a sample line of text.\n"
    
    start_time = time.time()

    # Create files with the specified sizes
    for file_name, size_mb in files.items():
        create_file(file_name, content, size_mb)
        print(f"Created {file_name} with size {size_mb} MB")

    print("Sample files created successfully.\n")

    # Example list of files to read
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt', 'file9.txt', 'file10.txt']
    
    for i in files:
        os.remove(i)
    print("all text files deleted")
    end_time = time.time()
    execution_time = end_time - start_time  # Total execution time
    print(f"\n\nExecution Time: {execution_time:.4f} seconds")
