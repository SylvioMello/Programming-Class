n = int(input())
def eprimo(n):
    """Verifica se o número n é primo"""
    d = 0
    for i in range(1, n+1):
        if n % i == 0:
            d += 1
    if d == 2:
        return True
    else:
        return False

def remove_repetidos(lista):
    """Remove os itens repetidos dentro de uma lista"""
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def rotacoes(n):
    """Retorna uma lista com as rotações de n"""
    rot = []
    for i in range(len(str(n))):
        m = (str(n)[i:] + str(n)[:i])
        m = int(m)
        rot.append(m)
    return rot

def primoscirculares(n):
    """Retorna uma lista com os primos circulares antes de n"""
    l = []
    for i in range(2, n+1):
        if eprimo(i):
            a = rotacoes(i)
            for j in a:
                if all(eprimo(c) for c in a):
                    l.append(j)
    for k in l:
        if k > n:
            l.remove(k)
    l = remove_repetidos(l)
    return l

print(primoscirculares(n))