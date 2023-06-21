saldo = 0
extrato = 'Extrato:\n'
qnt_saques = 0

menu = '''MENU:
[e] - Checar extrato
[d] - Realizar depósito
[s] - Realizar saque
[q] - Sair'''

def deposito():
	'Verifica as condições para depositar e atualiza o saldo e o extrato'
	
	global saldo
	global extrato
	global qnt_saques
	
	try:
		dep = round(float(input('Valor a ser depositado:')), 2)
		
		if dep > 0:
			saldo += dep
			extrato += f'Deposito realizado no valor de R$ {dep:.2f}.\n'
			print(f'Depósito realizado no valor de R$ {dep:.2f} .')
			print('---' * 10)
		else:
			print('ERRO: o valor do depósito precisa ser maior que 0.')
			print('---' * 10)
			
	except:
		print('ERRO: o depósito precisa ser um valor numérico.')
		print('---' * 10)
		
def saque():
	'Verifica as condições para sacar e atualiza o saldo, limite de saques e extrato'
	
	global saldo
	global extrato
	global qnt_saques
	
	try:
		saq = round(float(input('Valor a ser sacado:')), 2)

		lim_val_saldo = saq > saldo
		lim_qnt_saques = qnt_saques > 2
		lim_val_saq = saq > 500
		
		if lim_val_saldo:
			print('Saldo insuficiente.')
			print('---' * 10)
		elif lim_qnt_saques:
			print('Seu limite diário de saques é 3 e já foi atingido.')
			print('---' * 10)
		elif lim_val_saq:
			print('O limite por saque é de R$ 500,00 .')
			print('---' * 10)
		else:
			saldo -= saq
			qnt_saques += 1
			extrato += f'Saque realizado no valor de R${saq:.2f}.\n'
			print(f'Saque realizado no valor de R${saq:.2f} .')
			print('---' * 10)
			
	except:
		print('ERRO: o valor a ser sacado precisa ser um número.')
		print('---' * 10)
		
def mostra_extrato():
	'Mostra o extrato e o saldo'
	
	global extrato
	global saldo
	
	print(extrato)
	print(f'Saldo: R${saldo:.2f}')
	print('---' * 10)
	
while True:
	print(menu)
	opt = input('Selecione a opção:').lower()
	if opt == 'e':
		mostra_extrato()
	elif opt == 'd':
		deposito()
	elif opt == 's':
		saque()
	elif opt == 'q':
		break
	else:
		print(f'Opção inválida: {opt}')
		print('---' * 10)
		
print('Obrigado por usar nosso banco!')
	
	
	
	
