def max(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>b and c>a :
        return c
    else:
        print("je n'ai pas compris")
a= float(input("entrer un nombre: "))
b=float(input("entrer un nombre: "))
c=float(input("entrer un nombre: "))
print("le plus grand nombre est ", max(a, b, c))
def max(L):
    m= L[0]
    for elem in L:
        if elem>m:
            m=elem
    return m
