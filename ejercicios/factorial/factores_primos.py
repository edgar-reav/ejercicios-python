def descomp(num):

    primos = []

    for i in range(2, num+1):

        while num % i == 0:

            primos.append(i)
            num = num / i 

    for x in primos:
        print(x)



numero = int(input("número: "))
result = descomp(numero)
