a = int(input())
d = 0
def fatorLychrel(a):
    global d
    a = str(a)
    c = a[::-1]
    if a == c:
        return d
    else:
        d += 1
        if d >= 50:
            return -1
        return fatorLychrel(int(a)+int(c))


print(fatorLychrel(a))