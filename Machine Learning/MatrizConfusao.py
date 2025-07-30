from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# 10 macacos (0), 10 sapos (1)
# Valores reais
valores_reais    = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
valores_preditos = [0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1]

# Escolhendo classe Positiva como macacos, o que não representa macaco será negativo.
# True Positive (TP)  - 8 macacos foram previstos como macacos
# False Positive (FP) - 3 sapos foram previstos como macacos
# True Negative (TN)  - 7 sapos foram previstos com não macacos
# False Negative (FN) - 2 macacos foram previstos como sapos

# Acuracia
# Previsões corretas em relacao ao total de exemplos do conjunto (total de previsões)
# acuracia = (TP + TN) / (TP + FP + TN + FN)

# Precisao
# Proporção de verdadeiros positivos em relação total de exemplos positivas
# precisao = TP / (TP + FP)

# Recall
# Proporção de verdadeiros positivos em relação ao total de exemplos positivos reais
# recal = TP / (TP + FN)

# F-Score
# Média entre precisão e recall, proporcionando uma média mais equilibrada do desempenho de um modelo de classificação
# fscore = 2 * ( (precisao * recall) / (precisao + recall) )

print(confusion_matrix(valores_reais, valores_preditos))
print(classification_report(valores_reais, valores_preditos, target_names=['Macaco', 'Sapo']))