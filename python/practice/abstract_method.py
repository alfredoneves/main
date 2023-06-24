from abc import ABC, abstractmethod, abstractproperty	# library to use abstract methods

class Controle_remoto(ABC):
	@abstractmethod	# you must implement, but you have to figure out how
	def ligar(self):	# interface
		pass
		
	@property
	@abstractproperty
	def brand(self):	# interface
		pass
		
class Controle_TV(Controle_remoto):
	def ligar(self):
		print('TV ligada.')
		
	@property	# you need to write that this is a property here too
	def brand(self):
		return 'LG'

controle = Controle_TV()
controle.ligar()
print(controle.brand)
