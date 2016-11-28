

class Pessoa:

	def __init__(self,nome,email):
		self.nome = nome
		self.email = email

	def digaOi(self):
		print 'Oi, eu sou %s ' % self.nome

	def ler(self,arquivo):
		print arquivo.read()	

class Programador(Pessoa):

	def digaOi(self):
		print 'Sou programador'

class Grupo:

	def __init__(self,*pessoas):
		self.pessoas=pessoas

	def apresentacao(self):
		for p in self.pessoas:
			p.digaOi()	
		


if __name__ == '__main__':
	p=Programador('Jose','jose@gmail.com')
	p.digaOi()
	print 'Email ', p.email 

