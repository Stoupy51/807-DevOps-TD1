
## Python script that provides functions to generate multiple matrices with different properties.
"""
4 tests d'acceptation :
1.
	- Given: dimensions = [3,3,3], min_value = 1, max_value = 2, divider = 2.0
	- When: appelle de fonction generate_matrix(dimensions, min_value, max_value, divider)
	- Then: la fonction devrait retourner une matrice 3x3x3 avec les éléments entre 0.5 et 1
2.
	- Given: dimensions = [2,2], min_value = 0, max_value = 1, divider = 1.0
	- When: appelle de fonction generate_matrix(dimensions, min_value, max_value, divider)
	- Then: la fonction devrait retourner une matrice 2x2 avec les éléments entre 0 et 1
3.
	- Given: user input "4x4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"
	- When: appelle de fonction userinput_matrix()
	- Then: la fonction devrait retourner une matrice 4x4 avec les éléments de 1 à 16
4.
	- Given: user input "3x3 1 2 3 4 5 6 7 8 9"
	- When: appelle de fonction userinput_matrix()
	- Then: la fonction devrait retourner une matrice 3x3 avec les éléments de 1 à 9
"""

# Imports
import random

# Methods
def generate_matrix(dimensions: list[int] = [2,2], min_value: int = 0, max_value: int = 1, divider: float = 1.0) -> list:
	""" Generates a matrix with the given dimensions and fills it with random values between min_value and max_value.
	Args:
		dimensions	(list[int]):	dimensions of the matrix to be generated. can be [3,3,3] for a 3x3x3 matrix.
		min_value	(int):			minimum value for the matrix elements.
		max_value	(int):			maximum value for the matrix elements.
		divider		(float):		divider to be used to scale the random values.
	Returns:
		list: generated matrix.
	"""
	matrix = []
	for i in range(dimensions[0]):
		if len(dimensions) > 1:
			matrix.append(generate_matrix(dimensions[1:], min_value, max_value, divider))
		else:
			matrix.append(random.randint(min_value, max_value) / divider)
	return matrix

def userinput_matrix(dim: list = None) -> list:
	""" Generates a matrix with the given dimensions and fills it with user input.
	Args:
		dim	(list):	optional because used for recursion.
	Returns:
		list: generated matrix.
	"""
	matrix = []
	if dim is None:
		dimensions = input("Enter the dimensions of the matrix (e.g. '3x3'): ").split("x")
	else:
		dimensions = dim
	for i in range(int(dimensions[0])):
		if len(dimensions) > 1:
			matrix.append(userinput_matrix(dimensions[1:]))
		else:
			matrix.append(float(input(f"Enter the value for the element at position {i}: ")))
	return matrix


# Unit test functions
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"
import traceback

def test_generate_matrix() -> bool:
	""" Unit test for the generate_matrix function.	"""
	try:
		# Try to generate a matrix of size 3*3*3 with values between 0.5 and 1
		sizes = [3,3,3]
		matrix = generate_matrix(sizes, 1, 2, 2.0)

		# Check if the matrix has the right size for first dimension
		assert len(matrix) == sizes[0], f"Matrix has wrong size for first dimension: {len(matrix)} instead of {sizes[0]}"

		# For each element in the first dimension
		for i in range(len(matrix)):
			
			# Check if the matrix has the right size for second dimension
			assert len(matrix[i]) == sizes[1], f"Matrix has wrong size for second dimension: {len(matrix[i])} instead of {sizes[1]}"

			# For each element in the second dimension
			for j in range(len(matrix[i])):

				# Check if the matrix has the right size for third dimension
				assert len(matrix[i][j]) == sizes[2], f"Matrix has wrong size for third dimension: {len(matrix[i][j])} instead of {sizes[2]}"

				# For each element in the third dimension
				for k in range(len(matrix[i][j])):
					
					# Check if the element is between 0.5 and 1
					assert 0.5 <= matrix[i][j][k] <= 1, f"Element at position {i},{j},{k} is not between 0.5 and 1: {matrix[i][j][k]}"

	except Exception:
		print(f"{COLOR_RED}Error in test_generate_matrix: ", traceback.format_exc(), f"{COLOR_RESET}\n")
		return False

	# Everythin's fine
	return True

def test_userinput_matrix() -> bool:
	""" Unit test for the userinput_matrix function.	"""
	try:
		# Disable stdout temporary
		import sys
		temporary_out = "test_output.temp"
		temporary_in = "test_input.temp"
		sys.stdout = open(temporary_out, "w")

		# Try to generate a matrix of size 4*4 with user input
		to_stdin = "4x4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16".replace(" ", "\n")
		sys.stdin = open(temporary_in, "w")
		sys.stdin.write(to_stdin)
		sys.stdin.close()
		sys.stdin = open(temporary_in, "r")
		matrix = userinput_matrix()
		sys.stdin.close()
		sys.stdin = sys.__stdin__

		# Check if the matrix has the right size for first dimension
		assert len(matrix) == 4, f"Matrix has wrong size for first dimension: {len(matrix)} instead of 4"

		# For each element in the first dimension
		for i in range(len(matrix)):
			
			# Check if the matrix has the right size for second dimension
			assert len(matrix[i]) == 4, f"Matrix has wrong size for second dimension: {len(matrix[i])} instead of 4"

			# For each element in the second dimension
			for j in range(len(matrix[i])):
					
				# Check if the element is the same as the input
				assert matrix[i][j] == (i*4+j+1), f"Element at position {i},{j} is not the same as the input: {matrix[i][j]}"

	except Exception:
		# Go back to stdout
		sys.stdout.close()
		sys.stdout = sys.__stdout__

		print(f"{COLOR_RED}Error in test_userinput_matrix: ", traceback.format_exc(), f"{COLOR_RESET}\n")
		return False
	finally:
		# Go back to stdout
		sys.stdout.close()
		sys.stdout = sys.__stdout__

		# Remove temporary files
		import os
		os.remove(temporary_out)
		os.remove(temporary_in)

 	# Everythin's fine
	return True



# Run if directly called (not imported): runs all the tests
if __name__ == "__main__":

	# Run all the tests and remember the results
	bools = []
	bools.append(test_generate_matrix())
	bools.append(test_userinput_matrix())

	# Summary
	print("Summary:")
	for i in range(len(bools)):
		if bools[i]:
			print(f"{COLOR_GREEN}Test {i} passed!{COLOR_RESET}")
		else:
			print(f"{COLOR_RED}Test {i} failed!{COLOR_RESET}")

