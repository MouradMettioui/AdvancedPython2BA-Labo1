def primes100():
    a=1
    p=1
    while a<=100:
        b=1
        if p%b==0:
            while p>b:
                b+=1
                if p%b !=0:
                    x=1
                else:
                    break
        while p==b:
                print(a, ":", p)
                b+=1
                a+=1
        p+=1
primes100()

