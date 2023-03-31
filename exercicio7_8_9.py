def maximo(x):
    if len(x) == 1:
        return x[0]
    else:
        max_valor = max(x[1:])
        return x[0] if x[0] > max_valor else max_valor
def min(y):
    if len(y) == 1:
        return y[0]
    else:
        min_valor = min(y[1:])
        return y[0] if y[0] < min_valor else min_valor
def media(z):
    if len(z) == 1:
        return z[0]
    else:
        return (z[0] + media(z[1:])) / len(z)
lista = [6, 8, 33, 91, 98, 54, 135]
med = media(lista)
menorvalor = min(lista)
maiorvalor = max(lista)
print(f'maior valor: {maiorvalor}')
print(f'media: {med}')
print(f'menor valor: {menorvalor}')