import pandas as pd
df = pd.read_csv('./dadosUsoDataSources.csv', sep=';')
print(df.head())

soma_ds = df.groupby('DataSource')['QtdConexcoesCriadasDia'].sum()
print(soma_ds)