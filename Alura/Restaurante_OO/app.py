from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    obj_restaurante = Restaurante('Nome Restaurante', 'Categoria do Restaurante')
    bebida_suco = Bebida('Suco Melancia', 5, 'Grande')
    prato_pao = Prato('Paozinho', 2, 'Melhor paozinho da cidade')
    obj_restaurante.adicionar_item_no_cardapio(bebida_suco)
    obj_restaurante.adicionar_item_no_cardapio(prato_pao)
    obj_restaurante.exibir_cardapio()


    restaurante_china = Restaurante('China', 'Chinesa')
    restaurante_china.alternar_estado()
    restaurante_china.receber_avaliacao('Alex', 3)

    restaurante_igglus = Restaurante('Igglus', 'Brasileira')
    restaurante_igglus.receber_avaliacao('Joaquim', 10)

    restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
    restaurante_mexicano.alternar_estado()
    restaurante_mexicano.receber_avaliacao('Joaquim', 10)
    restaurante_mexicano.receber_avaliacao('Joao', 5)
    restaurante_mexicano.receber_avaliacao('Maria', 7)

    # Mostrando detalhes do objeto
    #print(dir(obj_restaurante))
    #print(vars(obj_restaurante))


    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()