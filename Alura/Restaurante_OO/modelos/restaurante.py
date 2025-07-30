from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria=categoria.upper()
        self._avaliacoes = []
        self._cardapio = []
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'-> {restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).rjust(5)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        qtd_notas = len(self._avaliacoes)
        media_notas = round(soma_das_notas / qtd_notas, 1)
        return media_notas
    
    def adicionar_item_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}\n')

        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preco: R$ {item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preco: R$ {item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
