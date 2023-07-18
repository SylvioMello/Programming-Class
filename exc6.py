from copy import deepcopy
a = eval(input())


def matriz_3x3(a):
    return (((a[0][0] * a[1][1] * a[2][2]) + (a[0][1] * a[1][2] * a[2][0]) + (a[0][2] * a[1][0] * a[2][1]))
            - ((a[0][0] * a[1][2] * a[2][1]) + (a[0][1] * a[1][0] * a[2][2]) + (a[0][2] * a[1][1] * a[2][0])))


def matriz_mxm(a):
    d = 0
    if len(a) == 3:
        return matriz_3x3(a)
    else:
        for i, e in enumerate(a[0]):
            b = deepcopy(a)
            del b[0]
            for j in range(len(b)):
                del b[j][i]
            d += e*((-1)**(0+i))*matriz_mxm(b)
        return d


print(matriz_mxm(a))