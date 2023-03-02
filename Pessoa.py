class Animal:
	def __init__(self) -> None:
		NotImplemented
		
	def falar(self, fala):
		print(fala)


class Pessoa(Animal):
	def __init__(self, nome: str, idade: int, altura: float, peso: int, cpf: str):
		self.nome = nome
		self.idade = idade
		self.altura = altura
		self.peso = peso
		self.cpf = cpf

	def ola(self):
		print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
		      f'anos e minha altura é {self.altura}')

	def cozinhar(self, receita: str):
		print(f'Estou cozinhando um(a): {receita}')

	def imc(self):
		imc = self.peso / self.altura
		print('IMC de altura {:.3f} e peso {:.2f} é de {:.3f}'.format(self.altura, self.peso, imc))

p = Pessoa(nome='Alexander', idade=40, altura=1.83, peso=79, cpf='901.843.431-00')
p.ola()
p.imc()
p.cozinhar('Macarrão')
p.falar("Teste")

table = {'Alexander': 123, 'Jessica': 456, 'Fernanda': 789}
for nome, num in table.items():
	print(f'{nome:10} ==> {num:7d}')
