from tabula import read_pdf
import pandas as pd

# pages='all' para ler tudo 118
tables = read_pdf("/tmp/266_sef_mg-resultado-preliminar-prova-objetiva-2023-02-25.pdf", pages='133')
df = pd.concat(tables)
df.drop(index=df.index[0:7], axis=0, inplace=True)
print(df)
#analista=df[9].str.count("^Aprovado").sum()
#analista=df.iloc[9].str.count("^Aprovado").sum()
#print(f'Quantidade: ', analista)