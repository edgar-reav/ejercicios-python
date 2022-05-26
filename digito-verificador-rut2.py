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
