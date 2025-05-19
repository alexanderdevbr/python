import pandas as pd
from collections import Counter

# Ler os números do arquivo, considerando que estão separados por vírgula e em várias linhas
with open('Federal.txt', 'r') as file:
    numeros_str = file.read().replace('\n', ',').split(',')

# Converter os números para inteiros
numeros = [int(num) for num in numeros_str if num]

# Extrair os dois últimos dígitos de cada número
ultimos_digitos = [num % 100 for num in numeros]

# Contar a frequência dos dois últimos dígitos
contagem_digitos = Counter(ultimos_digitos)

# Encontrar os 5 últimos dígitos mais comuns
mais_comuns_digitos = contagem_digitos.most_common(5)

# Converter a lista de números em tuplas para contar repetições
numeros_tuplas = list(zip(*[iter(numeros)]*5))

# Contar a frequência dos resultados (tuplas de 5 números)
contagem_resultados = Counter(numeros_tuplas)

# Encontrar os 5 resultados mais comuns
mais_comuns_resultados = contagem_resultados.most_common(5)

# Imprimir os resultados
print("Os 5 últimos dígitos que mais se repetem e suas respectivas quantidades de repetições:")
for digito, frequencia in mais_comuns_digitos:
    print(f"{digito:02d}: {frequencia} vezes")  # Formatar para garantir dois dígitos

print("\nOs 5 últimos resultados (grupos de 5 números) que mais se repetem e suas respectivas quantidades de repetições:")
for resultado, frequencia in mais_comuns_resultados:
    print(f"{resultado}: {frequencia} vezes")