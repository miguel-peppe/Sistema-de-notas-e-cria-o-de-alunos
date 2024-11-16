import math

def par(n: int) -> bool:
    return n % 2 == 0

def media(args: list) -> float:
    return sum(args) / len(args)

def moda(args: list):
    from collections import Counter
    contagem = Counter(args)
    max_frequencia = max(contagem.values())
    modas = [num for num, freq in contagem.items() if freq == max_frequencia]

    if len(modas) == 1:
        return modas, "Unimodal"
    elif len(modas) == 2:
        return modas, "Bimodal"
    elif len(modas) == 3:
        return modas, "Trimodal"
    elif len(modas) > 3:
        return modas, "Polimodal"
    else:
        return [], "Sem modas"

def mediana(args: list) -> float:
    args.sort()  
    tamanho = len(args)

    if par(tamanho):
        mid = tamanho // 2
        el1 = args[mid]
        el2 = args[mid - 1]
        return (el1 + el2) / 2
    else:
        mid = tamanho // 2
        return args[mid]

