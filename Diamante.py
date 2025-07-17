import sys

# Classe de Excessao personalizada
class ValorNegativo(Exception):
    """Exceção com passagem de parâmetro com valor negativo"""

try:
    # Qtde de linhas ate meio do Diamante passado por parametro
    # Caso nao seja passado parametro o valor 5 sera utilizado.
    linhas = 5 if len(sys.argv) == 1 else int(sys.argv[1])

    # Caso seja informado um valor 0 ou negativo
    if ( linhas <= 0):
        raise ValorNegativo("Favor informar valor inteiro positivo diferente de zero")
except ValueError:
    print("Favor informar valor inteiro")
    exit()
except ValorNegativo as e:
    print(e)
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()
else:
    print(f"Gerando diamante com {(linhas * 2)-1} linhas!")

# Parte de cima do Diamante
for i in range(1, linhas +1):
    print(" " * (linhas -i) + "*" * ( 2 * i - 1))

# Parte de baixo do Diamante
for i in range(linhas -1, 0, -1):
    print(" " * (linhas -i) + "*" * ( 2 * i - 1))

# Saida
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''