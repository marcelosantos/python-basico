

numeros = range(101)
ret=[]

for n in numeros:
	if n % 2:
		ret.append( n ** 2 )
	
#print ret

def impar(n):
	return n % 2

def quadrado(n):
	return n ** 2

#print map(quadrado,filter(impar,numeros))
		
ret = [ n ** 2 for n in numeros if n % 2 ]

print ret
	
