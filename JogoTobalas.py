import numpy as np
import statistics

jogos = [5,11,13,29,45,51,52,
         7,14,18,25,28,29,36,
         3,5,6,15,20,22,38,
         2,12,20,27,33,51,60,
         7,17,23,28,36,42,58,
         2,7,11,24,32,39,58]

jogos.sort()

print(jogos)
print("Quantidade jogos.........: ", len(jogos))
print("Media dos numeros jogados:  %2.2f" % np.mean(jogos))
print("Mediana dos numeros......:  %2.2f" % np.median(jogos))
print("Moda dos números jogados.: ", statistics.mode(jogos))
print("Variância................:  %2.2f" % statistics.variance(jogos))
print("Desvio Padrão............:  %2.2f" % statistics.stdev(jogos))