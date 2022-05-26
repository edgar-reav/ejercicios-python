rut = int(input("rut: "))

a = (rut//10000000) * 3
b = ((rut//1000000)%10) * 2
c = ((rut//100000)%10) * 7
d = ((rut//10000)%10) * 6
e = ((rut//1000)%10) * 5
f = ((rut//100)%10) * 4
g = ((rut//10)%10) * 3
h = ((rut//1)%10) * 2


suma = (a+b+c+d+e+f+g+h)

resto1 = suma//11
resto2 = suma - (11 * resto1)


resta = 11 - resto2

if resta == 11:
    print("dv=",end="")
    print(0)
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)




modulo = __import__('itertools', globals(), locals(), ['cycle'], 0)
cycle = modulo.cycle

def verificador(rut):
    reversed_d = map(int, reversed(str(rut)))
    fac = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_d, fac))
    return (-s) % 11

x = int(input("rut: "))
mo = verificador(x)

mensaje = "dv="

if( mo == 11):

    mensaje += "0"
    print(mensaje)
    
elif( mo == 10):

    mensaje += "K"
    print(mensaje)

else:

    mensaje += str(mo)
    print(mensaje)
