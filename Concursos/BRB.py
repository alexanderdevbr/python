import pandas as pd
dados = [['Distrito Federal', 61, 'DF'],
		 ['Rio de Janeiro', 21, 'RJ'],
         ['São Paulo', 11, 'SP'],
         ['Acre', 68, 'AC'],
         ['Goias', 62, 'GO'],
         ['Inexistente', 0, 'IX']]
df = pd.DataFrame(dados, columns=['Estado', 'DDD', 'Sigla'])
df.set_index('DDD')
print(df.loc[0].values)