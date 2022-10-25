# Closure
def first_func():
	print("Closures are great")


def details(first_func):
	name = 'Ian Morvin'
	age = 45

	def return_details(*args, **kwargs):
		print(f"{name} - {age}")
		return first_func(*args, **kwargs)

	return return_details

first_func = details(first_func)
first_func() # closure call


# Decorators (Functions taking other functions as an arg)
# When decoratrs are used the closure call is not neccessary


@details # It's equal to saying first_func = details(first_ func)
def first_func():
	print("Decorators are great")

first_func()

@details
def second_func(language, experience):
	print(language, experience)

second_func('Python', 4)


# Class Decorators
class details_class(object):
	def __init__(self, first_func):
		self.first_func = first_func

	def __call__(self, *args, **kwargs):
		return self.first_func(*args, **kwargs) 


@details_class
def first_func():
	print("Decorators are great")

first_func()

@details_class
def second_func(language, experience):
	print(language, experience)

second_func('Javascript', 4)


# Loggig with decorators

def logger_func(first_func):
	import logging
	logging.basicConfig(filename=f"{first_func.__name__}.logs", level=logging.INFO)

	def wrapper(*args,**kwargs):
		logging.info(f"The function ran with arguments:{args} and keywords:{kwargs}")
		return first_func(*args, **kwargs)

	return wrapper

@logger_func
def first_func(name, career):
	print("logging is best for tests")

first_func('Ian Morvin', 'Software Development')