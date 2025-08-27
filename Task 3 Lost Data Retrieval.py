import os

# Define the test directory
test_dir = 'test_recovery'

# Create the test directory if it doesn't exist
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Create sample files
file_names = ['file1.txt', 'file2.txt', 'file3.txt']
for file_name in file_names:
    with open(os.path.join(test_dir, file_name), 'w') as f:
        f.write(f'This is the content of {file_name}.')

print("Sample files created.")

# Delete the files
for file_name in file_names:
    os.remove(os.path.join(test_dir, file_name))
    print(f"{file_name} deleted.")

print("Files deleted. Now you can use recovery tools to attempt retrieval.")
