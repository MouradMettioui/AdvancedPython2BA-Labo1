D = {n: n-1 for n in range(2, 21)}
print("6:", D)
D1 = {int(n/3) : n for n in range( 3, 31) if n%3 ==0 }
print( 1 in D1 )