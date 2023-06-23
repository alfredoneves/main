# criar dicionários para armazenar os dados dos usuários e contas
#usuarios = {cpf: [nome, data_nascimento, endereco,]}
#contas = {numero_conta: [saldo, extrato, qnt_saques, agencia, usuario]}

usuarios = {}
contas = {}
cpf = 'Realize login'

def menu(cpf):
	menu = f'''MENU:
[l] - Login
[e] - Checar extrato
[d] - Realizar depósito
[s] - Realizar saque		LOGIN ATUAL:{cpf}
[q] - Sair
[u] - Criar usuário
[c] - Criar conta'''
	print(menu)
	
def deposito(contas):
	'Verifica as condições para depositar e atualiza o saldo e o extrato'
	
	try:
		dep = round(float(input('Valor a ser depositado:')), 2)
		numero_conta = int(input('Digite o número da conta:'))
		
		if dep > 0 and numero_conta in contas.keys():
			lista_conta = contas.copy()[numero_conta]	# retorna apenas a lista associada ao número da conta
			lista_conta[0] += dep	# adiciona o depósito ao saldo
			lista_conta[1] += f'Deposito realizado no valor de R$ {dep:.2f}.\n'	# altera o extrato
			contas[numero_conta] = lista_conta.copy()	# altera o valor na lista de contas
			print(f'Depósito realizado no valor de R$ {dep:.2f} .')
		else:
			print('ERRO: o valor do depósito precisa ser maior que 0 e o número da conta precisa existir.')
			
	except:
		print('ERRO: o depósito precisa ser um valor numérico.')
		
def saque(*, contas):
	'Verifica as condições para sacar e atualiza o saldo, limite de saques e extrato'
	#contas = {numero_conta: [saldo, extrato, qnt_saques, agencia, usuario]}
	try:
		saq = round(float(input('Valor a ser sacado:')), 2)
		numero_conta = int(input('Digite o número da conta:'))
		if numero_conta in contas.keys():
			novo_saque = contas[numero_conta].copy()	# cópia da lista da conta
			lim_val_saldo = saq > novo_saque[0]
			lim_qnt_saques = novo_saque[2] > 2
			lim_val_saq = saq > 500
		
		if lim_val_saldo:
			print('Saldo insuficiente.')
		elif lim_qnt_saques:
			print('Seu limite diário de saques é 3 e já foi atingido.')
		elif lim_val_saq:
			print('O limite por saque é de R$ 500,00 .')
		else:
			novo_saque[0] -= saq
			novo_saque[1] += f'Saque realizado no valor de R${saq:.2f}.\n'
			novo_saque[2] += 1
			print(f'Saque realizado no valor de R${saq:.2f} .')
			contas[numero_conta] = novo_saque
	except:
		print('ERRO: o valor a ser sacado e o número da conta precisam ser números.')
		
def mostra_extrato(contas):
	'Mostra o extrato e informações da conta'
	
	try:
		numero_conta = int(input('Digite o número da conta:'))
		extrato = contas[numero_conta].copy()
		extrato[0] = f'Saldo: R${extrato[0]:.2f}'
		print(extrato[0])
		print(extrato[1])
	except:
		print('O número da conta precisa ser um valor inteiro.')
		
def criar_usuario(usuarios):
	'Coleta os dados necessários para o cadastro e atualiza o dicionário fornecido.'
	
	print('Iniciando criação de usuário.')
	cpf = str(input('Digite seu CPF (apenas números):'))
	nome = str(input('Digite seu nome:'))
	data_nascimento = str(input('Digite sua data de nascimento (dd/mm/aaaa):'))
	endereco = str(input('Digite seu endereço (logradouro, nro - bairro - cidade/sigla do estado):'))
	
	# verificar se o cpf já existe
	cpf_existe = usuarios.get(cpf, 'não encontrado')
	if cpf_existe == 'não encontrado':
		usuarios[cpf] = [nome, data_nascimento, endereco]
		print('Usuário criado com sucesso.')
	else:
		print('ERROR: CPF já cadastrado no sistema.')
	
def criar_conta(contas, usuarios):
	'Cria uma conta para um usuário já cadastrado.'
	#contas = {numero_conta: [saldo, extrato, qnt_saques, agencia, usuario]}
	print('Iniciando criação de conta.')
	cpf = str(input('Digite seu CPF (apenas números):'))
	
	# verificar se o cpf já foi cadastrado por um usuário
	if cpf in usuarios.keys():
		agencia = '0001'
		numero_conta = len(contas) + 1
		contas[numero_conta] = [0, 'Extrato:\n', 0, agencia, usuarios[cpf]]
		print('Conta criada com sucesso')
	else:
		print('ERROR: não foi identificada uma conta com esse CPF, crie uma conta para prosseguir.')
		
def login(usuarios):
	'Define o cpf utilizado para que o usuário não precise ficar digitando de forma repetida'
	global cpf
	
	print('Realizando login ...')
	novo_cpf = str(input('Digite seu CPF (apenas números):'))
	
	# verificar se o cpf já foi cadastrado por um usuário
	if novo_cpf in usuarios.keys():
		cpf = novo_cpf
		print(cpf)
		print('Login realizado com sucesso')
	else:
		print('ERROR: não foi identificada uma conta com esse CPF, crie uma conta para prosseguir.')
		
print('Operação bancária iniciada!\n')

while True:
	print('---' * 10 + '\n')
	menu(cpf)
	opt = input('Selecione a opção:').lower()
	
	if opt == 'l':
		login(usuarios)
	elif opt == 'e':
		mostra_extrato(contas=contas)
	elif opt == 'd':
		deposito(contas)
	elif opt == 's':
		saque(contas=contas)
	elif opt == 'q':
		break
	elif opt == 'u':
		criar_usuario(usuarios)
	elif opt == 'c':
		criar_conta(contas, usuarios)
	else:
		print(f'Opção inválida: {opt}')
		
print('Obrigado por usar nosso banco!')
	
	
	
	
