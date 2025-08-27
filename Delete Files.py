import os

test_dir = 'test_recovery'

# Delete the test files
for i in range(5):
    os.remove(os.path.join(test_dir, f'test_file_{i}.txt'))
