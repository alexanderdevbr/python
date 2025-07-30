import os

lista_restaurantes = [{'nome': 'China', 'categoria': 'Chinesa', 'ativo': False},
                      {'nome': 'Igglus', 'categoria': 'Pizzaria', 'ativo': True},
                      {'nome': 'Toca', 'categoria': 'Peixe', 'ativo': False}]

def exibir_nome_restaurante_do_programa():
    # https://fsymbols.com/pt/letras/
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_menu():
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Ativar/Desativar")
    print("4. Sair\n")

def opcao_invalida():
    print('Opção inválida!')
    voltar_menu_principal()
    

def voltar_menu_principal():
    input('\nPressione qualquer tecla para continuar ')
    main()

def exibir_subtitulo(texto):
    limpar_tela()
    print(f'###{texto}\n')

def cadastrar():
    exibir_subtitulo('Cadastro d restaurante')

    nome_restaurante = input('Nome do restaurante: ')
    categoria_restaurante = input(f'Categoria do restaurante {nome_restaurante}: ')
    restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    lista_restaurantes.append(restaurante)
    print(f'Restaurante {restaurante["nome"]} cadastrado com sucesso!')

    voltar_menu_principal()
    

def listar():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in lista_restaurantes:
        status = 'Ativo' if restaurante['ativo'] else 'Desativdo'
        print(f'->{restaurante["nome"].ljust(20)} [{status}]')

    voltar_menu_principal()
    
def alternar_status_restaurante():
    """
    Muda o status de um restaurante.

    Inputs:
        Nome do restaurante

    Outputs:
        Restaurante com status alterado, ou, mensagem de que não foi encontrado o Restaurante
    """
    exibir_subtitulo('Alterando estado do Restaurante')

    nome_restaurante = input('Digite o nome do restaurante desejado: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # restaurante.update({'ativo': True})
            restaurante['ativo'] = not restaurante['ativo']
            msg_acao = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'O restaurante {nome_restaurante} foi {msg_acao} com sucesso!')
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_menu_principal()

def escolha_opcao():
    try:
        opcao_escolhida = int(input("Escolha a opção: "))
        #print(f"Você escolheu a opção {opcao_escolhida}!\n")

        match opcao_escolhida:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                alternar_status_restaurante()
            case 4:
                fim()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def fim():
    print("Parabéns!","Tudo certo","Agora é continuar o programa.", sep = "\n")

def limpar_tela():
    os.system('clear')

def main():
    limpar_tela()
    exibir_nome_restaurante_do_programa()
    exibir_menu()
    escolha_opcao()

if __name__ == '__main__':
    main()