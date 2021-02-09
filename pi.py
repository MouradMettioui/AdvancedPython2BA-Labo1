def pi():
    x = 0
    a=1
    from math import sqrt 
    while a < 1000:
        x= x + (1/(a**2))
        a+=1 
    return sqrt(6*x)

print(pi())