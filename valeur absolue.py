def abs(a):
    if a<0:
        print(-a)
    elif a>0:
        print(a)
    else : 
        print ("zéro n'a pas de valeur absolue")

a =float(input("entrer un nombre: "))
abs(a)