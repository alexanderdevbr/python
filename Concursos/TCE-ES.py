import pandas as pd 

# Item D) da Prova Discurssiva TCE/ES
def provaDiscurssivaTCEES():
    processos = {
        "numero": [37,38,39],
        "paginas": [50,10,2000],
        "autor": ['joao','maria','antonio']
    }

    tabela_processo = pd.DataFrame(processos)
    for x in tabela_processo.index:
        if tabela_processo.loc[x, "paginas"] > 120:
            tabela_processo.drop(x, inplace=True)

    print(tabela_processo)


provaDiscurssivaTCEES()