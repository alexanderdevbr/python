# Estatisticas referente aos objetos MinIO PJe 1G e 2G TRF1
import pandas as pd

# Lendo arquivo CSV usando ; como delimitador
objetos = pd.read_csv('d:/tmp/lista_objetos_minio1.csv', delimiter=';')

# Imprimindo dataframe
print(objetos)

# Imprimindo os 3 maiores valores de 'Tamanho Kb'
print('\nMaiores valores')
print(objetos.nlargest(n=3, columns='Tamanho Kb'))

# Imprimindo dataset ordenado
print('\nDataframe ordenado por Tamanho KB')
print(objetos.sort_values(['Tamanho Kb']))
print()

maiores_objetos=objetos.nlargest(n=10, columns='Tamanho Kb')
maior_objeto=maiores_objetos['Tamanho Kb'].max() / 1024;
qtde_objetos=len(objetos)

# Média, Mediana, Moda, Varianca e Desvio Padrao dos valores 'Tamanho Kb'
media=objetos['Tamanho Kb'].mean()
mediana=objetos['Tamanho Kb'].median()
moda=objetos['Tamanho Kb'].mode()
variancia=objetos['Tamanho Kb'].var()
desvio_padrao=objetos['Tamanho Kb'].std()

print(f"Quantidade de Objetos: {qtde_objetos}, Maior Objeto: {maior_objeto:.2f}Mb, Media: {media:.2f}Kb, Mediana: {mediana}Kb, Moda: {moda[0]}Kb, Variancia: {variancia:.2f}, Desvio Padrao: {desvio_padrao:.2f}")
print()

'''
Resultado para CSV com todos Objetos armazenados MinIO
------------------------------------------------------
$ C:/Users/alexa/AppData/Local/Programs/Python/Python310/python.exe c:/Users/alexa/Workspace/Python/EstatisticaObjetosMinIO.py

          Tamanho Kb  AnoMes  Dia                                      Hash
54665577      408128  202206    1  f458146cc887fba93c32629b0445ed50c8c0241d
53057635      364772  202205   31  0562a7f57041afea63760dbb5dd9c166a9373384
41540166      353244  202203   25  1bb2e6fededef38a63aeeb0e99b568145b6a2d87

Quantidade de Objetos: 92758090, Maior Objeto: 398.56Mb, Media: 778.36Kb, Mediana: 44.0Kb, Moda: 24Kb, Variancia: 35122613.50, Desvio Padrao: 5926.43
'''