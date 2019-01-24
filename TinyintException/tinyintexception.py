class TinyIntError(Exception):
	def __init__(self):
		self.message = 'El numero entregado NO es un dato tipo TinyInt'

	def __str__(self):
		return self.message 
