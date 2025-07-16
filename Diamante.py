# Qtde de linhas ate meio do Diamante
linhas=5

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