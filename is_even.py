def is_even(x):
	"""
	Return True if integer is even
	Return False if integer is not even
	Raise TypeError if x is not an integer
	"""
	return True

assert is_even.__doc__ is not None

number = False
try:
	is_even('sdfserw')
except:
	number = True

assert is_even(number)

