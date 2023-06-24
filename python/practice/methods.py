class Pessoa:
	def __init__(self, name=None, age=None):
		self.name = name
		self.age = age
		
	@classmethod
	def show_age(cls, birth_year, name):
		age = 2023 - birth_year
		return cls(name, age)
		
	@staticmethod
	def adult(age):
		return age >= 18
		
p = Pessoa(name='ana', age=10)
print(p.name, p.age)

p2 = Pessoa.show_age(2001, name='alfredo')
print(p2.name, p2.age)
