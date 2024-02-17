
## Python script that runs every.py file in the current directory (not itself)
# Imports
import os
import sys
import subprocess

# Get all the .py paths
py_files = [f for f in os.listdir() if f.endswith('.py') and f != '_RUN_ALL_TESTS.py']

# Run each .py file
for py_file in py_files:
	print(f"Running {py_file}...")
	subprocess.run(['python', py_file])
	print(f"{py_file} complete.\n")
print("All tests complete.")

