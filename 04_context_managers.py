with open('sample.txt', 'w') as text:
	text.write("Software Development")

# class

class Context():
	def __init__(self, file, mode):
		self.file = file
		self.mode = mode

	def __enter__(self):
		self.file = open(self.file, self.mode)
		return self.file

	def __exit__(self, exec_type, exec_value, traceback):
		self.file.close()


with Context('class.txt', 'w') as text:
	text.write('Class Based')	


