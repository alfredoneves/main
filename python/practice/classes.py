class Bike:
	def __init__(self, color, model, price):
		self.color = color
		self.model = model
		self.price = price
	def __str__(self):
		return f'{self.__class__.__name__}: {[f"{key}:{value}" for key, value in self.__dict__.items()]}'

b1 = Bike('red', 'caloi', '300')
print(b1)

# list comprehension example
#test = 'abc'
#print(f'{test} --- {[f"{x.upper()}" for x in test]}')

# inheritance

class Veiculo():
	def __init__(self, cor, placa, nro_rodas):
		self.cor = cor
		self.placa = placa
		self.nro_rodas = nro_rodas
		
	def buzinar(self):
		print("FOOOOOOON")
	
	def __str__(self):
		return f'{self.__class__.__name__}: {[f"{key}:{value}" for key, value in self.__dict__.items()]}'
			
class Caminhao(Veiculo):
	def __init__(self, cor, placa, nro_rodas, carga):
		super().__init__(cor, placa, nro_rodas)	# recebe of atributos de da classe Veiculo
		self.carga = carga

	def esta_carregado(self):
		print(f'Caminhão carregado:{self.carga}')
		
cam = Caminhao('vermelho', 'aacc-1234', 9, True) 
print(cam)
cam.esta_carregado()	

# multiple inheritance

class Animal:
	def __init__(self, nro_patas):
		self.nro_patas = nro_patas
	
	def __str__(self):
		return f'{self.__class__.__name__}: {[f"{key}:{value}" for key, value in self.__dict__.items()]}'
		
class Mamifero(Animal):
	def __init__(self, cor_pelo, **kw):
		self.cor_pelo = cor_pelo
		super().__init__(**kw)	# pega key:value da classe pai para evitar conflitos

class Ave(Animal):
	def __init__(self, cor_bico, **kw):
		self.cor_bico = cor_bico
		super().__init__(**kw)
		
class Ornitorrinco(Mamifero, Ave):
	def __init__(self, cor_bico, cor_pelo, nro_patas):
		super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)	# key:value por causa dos **kw
		print(Ornitorrinco.__mro__)	# caminho pelo qual a classe procura os métodos e atributos
		
perry = Ornitorrinco(nro_patas=2, cor_pelo='verde claro', cor_bico='amarelo')
print(perry)
	
	
	
		
		
		
		
		
		
