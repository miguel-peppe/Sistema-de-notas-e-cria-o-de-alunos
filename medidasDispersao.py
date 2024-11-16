import math

def variancia(dados):
    media = sum(dados) / len(dados)
    return sum((x - media) ** 2 for x in dados) / len(dados)

def desvio_padrao(dados):
    return math.sqrt(variancia(dados))

def coeficiente_variacao(dados):
    return (desvio_padrao(dados) / (sum(dados) / len(dados))) * 100


