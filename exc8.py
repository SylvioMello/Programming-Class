a = eval(input())
b = eval(input())


def f(a, b):
    if a == b:
        return True
    else:
        if len(a) == 0:
            return False
        elif len(a) == 1:
            for i in range(len(b)):
                if a[0] == b[i]:
                    return True
        elif len(a) > 1:
            for j in range(len(b)):
                if a[0] == b[j]:
                    return f(a[1:],b[j+1:])
        return False

print(f(a,b))