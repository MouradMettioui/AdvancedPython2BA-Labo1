def sqrt(x):
    result=1
    while abs(result - x/result) > 1e-6:
        result = (result + x/result) / 2
    return result

x=int(input("entrer un nombre: "))
print("La racine carreé de", x, "est", sqrt(x))