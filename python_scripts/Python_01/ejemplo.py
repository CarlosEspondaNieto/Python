def ejemplo(param1, param2):
    print(param1)
    return param2


def ejemplo2(param1="Hola", param2=5):
	print(param1)
    return param2


def ejemplo3(*args):
	print(args)


def ejemplo4(**kwargs):
	print(kwargs)


class MyClass:
	
	def my_method(self):
		print("Something")
