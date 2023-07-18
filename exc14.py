x = float(input())
n = int(input())
def Leibniz(x,n):
    resultado = 0.0
    if n == 1:
        return x
    else:
        for i in range(n):
            resultado += (-x)**i/(2.0*i+1.0)
    return resultado
print(Leibniz(x,n))