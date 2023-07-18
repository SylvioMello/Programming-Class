class Polinomio:
    def __init__(self, coeficientes=None):
        if coeficientes is None:
            coeficientes = []
        self.coeficientes = coeficientes

    def __setitem__(self, grau, coeficiente):
        if len(self.coeficientes) - 1 < grau:
            while len(self.coeficientes) - 1 < grau:
                self.coeficientes.append(0)
            self.coeficientes[grau] = coeficiente
        else:
            self.coeficientes[grau] = coeficiente

    def __getitem__(self, grau):
        return self.coeficientes[grau]

    def grau(self):
        return len(self.coeficientes) - 1

    def __mul__(self, p):
        resultado = []
        if len(self.coeficientes) >= len(p.coeficientes):
            for i in range(2 * len(self.coeficientes) - 1):
                resultado.append(0)
        elif len(p.coeficientes) > len(self.coeficientes):
            for i in range(2 * len(p.coeficientes) - 1):
                resultado.append(0)
        if len(self.coeficientes) > len(p.coeficientes):
            adiciona = len(self.coeficientes) - len(p.coeficientes)
            for i in range(adiciona):
                p.coeficientes.append(0)
        elif len(p.coeficientes) > len(self.coeficientes):
            adiciona = len(p.coeficientes) - len(self.coeficientes)
            for i in range(adiciona):
                self.coeficientes.append(0)
        for i in range(len(self.coeficientes)):
            for j in range(len(self.coeficientes)):
                resultado[i+j] += self.coeficientes[i]*p.coeficientes[j]
        return Polinomio(resultado)

    def __add__(self, p):
        if len(self.coeficientes) > len(p.coeficientes):
            adiciona = len(self.coeficientes) - len(p.coeficientes)
            for i in range(adiciona):
                p.coeficientes.append(0)
        elif len(p.coeficientes) > len(self.coeficientes):
            adiciona = len(p.coeficientes) - len(self.coeficientes)
            for i in range(adiciona):
                self.coeficientes.append(0)
        resultado = []
        for i in range(len(self.coeficientes)):
            somatorio = self.coeficientes[i] + p.coeficientes[i]
            resultado.append(somatorio)
        return Polinomio(resultado)

    def __sub__(self, p):
        if len(self.coeficientes) > len(p.coeficientes):
            adiciona = len(self.coeficientes) - len(p.coeficientes)
            for i in range(adiciona):
                p.coeficientes.append(0)
        elif len(p.coeficientes) > len(self.coeficientes):
            adiciona = len(p.coeficientes) - len(self.coeficientes)
            for i in range(adiciona):
                self.coeficientes.append(0)
        resultado = []
        for i in range(len(self.coeficientes)):
            diferenca = self.coeficientes[i] - p.coeficientes[i]
            resultado.append(diferenca)
        return Polinomio(resultado)

    def avalia(self, x):
        s = 0
        for i in range(len(self.coeficientes)):
            if i == 0:
                s += self.coeficientes[i]
                continue
            s += self.coeficientes[i] * x ** i
        return s

    def __repr__(self):
        return str(self.coeficientes)


p = Polinomio(eval(input()))
q = Polinomio(eval(input()))
x = input()
if '.' in x:
    x = float(x)
else:
    x = int(x)
print(p.avalia(x), q.avalia(x), (p + q).avalia(x), (p - q).avalia(x), (p * q).avalia(x))