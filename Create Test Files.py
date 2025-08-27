import os
# Create a test directory
test_dir = 'test_recovery'
os.makedirs(test_dir, exist_ok=True)
# Create test files
for i in range(5):
    with open(os.path.join(test_dir, f'test_file_{i}.txt'), 'w') as f:
        f.write(f'This is test file number {i}.')
