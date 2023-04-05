def leapyear(a):
    b = a%4 == 0 and a%100 != 0
    c=(a%400 ==0)
    if b== True :
        return b
    elif  c== True :
        return c
    else :
        return c
a= int(input("entrer une année:"))
print(leapyear(a))