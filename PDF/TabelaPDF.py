from tabula import read_pdf
import pandas as pd

# pages='all' para ler tudo
tables = read_pdf("./388-receita-federal-analise-definitiva-homologados_com-anexo.pdf", pages='85')
df = pd.concat(tables)

analista=df['Cargo'].str.count("^Analista").sum()
auditor=df['Cargo'].str.count("^Auditor").sum()

print(f'Quantidade de Analista: ', analista)
print(f'Quantidade de Auditor.: ', auditor)