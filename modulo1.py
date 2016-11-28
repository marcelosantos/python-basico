'''Arquivo de calculo'''

def soma(a,b):
	'''Calcula a soma de dois numeros'''
	return a+b

def somas(a,b,*numeros):
	'''Soma varios numeros passados'''
	n=a+b
	for i in numeros:
		n+=i
	return n	

def somat(*numeros):
	'''Soma varios de forma simples'''
	r = [ for n in numeros ]
	return r

def diferenca(a,b):
	'''Calcula a diferenca entre dois numeros'''
	return a-b

if __name__ == '__main__' :
	print somat(2,5), diferenca(5,4)
elif __name__ == 'modulo1':
	print 'Importado'
else:	
	print 'Algo de errado ocorreu'
	
