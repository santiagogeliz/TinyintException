from .validates import tinyintvalidate, intvalidate
from .tinyintexception import TinyIntError

def finalvalidate(val):
	try:
		if tinyintvalidate(val) and intvalidate(val):
			print('El numero ES un dato TinyInt')
			return True 
		else:
			raise TinyIntError()
	except TinyIntError as error:
		print(error)