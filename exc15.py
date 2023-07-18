a = str(input())
b = str(input())

def anagrama(a,b):
    a = list(a)
    b = list(b)
    for i in a:
        if i in b:
            del b[b.index(i)]
    if len(b) == 0:
        return True
    else:
        return False

print(anagrama(a,b))