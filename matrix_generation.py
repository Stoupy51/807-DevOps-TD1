
## Python script that provides functions to generate multiple matrices with different properties.
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
			matrix.append(userinput_matrix())
		else:
			matrix.append(float(input(f"Enter the value for the element at position {i}: ")))
	return matrix

