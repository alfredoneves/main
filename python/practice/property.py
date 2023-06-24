class Foo:
	def __init__(self, x=None):
		self._x = x
	
	@property	# decorator (executes first when the class is initialized)
	def x(self):
		return self._x or 0
	
	@x.setter	# setter is the way you use to atribute a value to your variable
	def x(self, value):
		self._x = value	# check this latter
	
	@x.deleter	# used if you want to remove the value, but not remove the variable from the memory
	def x(self):
		self._x = 0
		
foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

