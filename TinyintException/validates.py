def tinyintvalidate(val):
	return val >= 0 and val <= 255

def intvalidate(val):
	try:
		return isinstance(int(val), int)
	except ValueError as error:
		return False 