#!/usr/bin/python3
class WrongType(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)

def list_division(my_list_1, my_list_2, list_length):
	my_list = []
	for i in range(0, list_length):
		try:
			if type(my_list_1[i]) not in (int, float):
				x = 0
				raise WrongType
			elif type(my_list_2[i]) not in (int, float):
				x = 0
				raise WrongType
			else:
				x = my_list_1[i] / my_list_2[i]
			
		except ZeroDivisionError:
			x = 0
			print("division by 0")
		except WrongType:
			x = 0
			print("wrong type")
		except IndexError:
			x = 0
			print("out of range")
		finally:
			my_list = my_list + [x]
		
	return(my_list)
