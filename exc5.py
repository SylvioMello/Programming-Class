a = eval(input())
def matriz_1x1(a):
    return (a[0])
if len(a) == 1:
    print(matriz_1x1(a))
def matriz_2x2(a):
    return ((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))
if len(a) == 2:
    print(matriz_2x2(a))
def matriz_3x3(a):
    return(((a[0][0]*a[1][1]*a[2][2])+(a[0][1]*a[1][2]*a[2][0])+(a[0][2]*a[1][0]*a[2][1]))
    - ((a[0][0]*a[1][2]*a[2][1])+(a[0][1]*a[1][0]*a[2][2])+(a[0][2]*a[1][1]*a[2][0])))
if len(a) == 3:
    print(matriz_3x3(a))