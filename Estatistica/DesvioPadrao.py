def desvio(serie):
    media = sum(serie) / len(serie)

    # Gerando vetor com o quadrado da diferenca entre cada um dos valores da serie e a media
    quadrados_diferenca_media = []
    for i in serie:
        v = i - media
        quadrados_diferenca_media.append(v * v)
    variancia = (sum(quadrados_diferenca_media) / len(quadrados_diferenca_media))

    # Calculando a Variancia que e a media do vetor com o quadrado da diferenca
    desvio = variancia ** 0.5
    return media, quadrados_diferenca_media, variancia, desvio



# Algoritmo para calcular desvio padrao de uma serie de numeros
serie = [6,2,3,1]
m, qdm, v, d = desvio(serie)
print("Serie.........:", serie)
print("Quadrado Dif..:", qdm)
print("Media.........: %.2f" % m)
print("Variancia.....: %.2f" % v)
print("Desviro Padrao: %.2f" % d)
print("")

serie = [1,4,7,2,6]
m, qdm, v, d = desvio(serie)
print("Serie.........:", serie)
print("Quadrado Dif..:", qdm)
print("Media.........: %.2f" % m)
print("Variancia.....: %.2f" % v)
print("Desviro Padrao: %.2f" % d)