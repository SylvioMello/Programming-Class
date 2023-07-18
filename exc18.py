L = eval(input())
def mesma_soma_algarismos(L):
        """ Uma função que acumula o somatório dos  algarismos de cada elemento da lista L em uma lista l """
        l = []
        for i in range(len(L)):
            n = L[i]
            s = 0
            while n:
                s += n % 10
                n //= 10
            l.append(s)
        for j in range(len(l)):
            if l[j] == s:
                return True
            else:
                return False


print(mesma_soma_algarismos(L))