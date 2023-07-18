a = eval(input())
b = eval(input())
c = d = 0

def matriz_resultante(a, b):
    nova_matriz = []
    for i in range(len(a)):
        line = []
        if type(b[0]) == list:
            for j in range(len(b[0])):
                line.append(0)
            nova_matriz.append(line)
        if type(b[0]) == int:
            for j in range(len(b)):
                line.append(0)
            nova_matriz.append(line)
    return nova_matriz

if len(a)==1 and len(b)==1:
    """caso 1(1x1 * 1x1)"""
    c = [a[0] * b[0]]
    print(c)
if type(b[0]) == list and len(b[0]) == 1:
    """caso 2(1xm * mx1)"""
    for i in range(len(b)):
        c = a[i] * b[i][0]
        d += c
    print([d])
if type(a[0]) == list and len(a[0]) == 1:
    """caso 3(mx1 * 1xm)"""
    def produto(a, b):
        resultado = matriz_resultante(a, b)
        for i in range(len(a)):
            for j in range(len(a)):
                elemento = a[i][0] * b[j]
                resultado[i][j] = elemento
        return resultado
    print(produto(a, b))
if type(a[0]) == list and len(a) >= 2 and type(b[0]) == list and len(b) >= 2:
    def produto(a, b):
        resultado = matriz_resultante(a, b)
        for i in range(len(a)):
            for j in range(len(b[0])):
                elemento = 0
                for k in range(len(b)):
                    elemento += a[i][k] * b[k][j]
                resultado[i][j] = elemento
        return resultado
    print(produto(a,b))