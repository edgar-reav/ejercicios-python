usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803


billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000


def bills(c,x):
    billetes = c // x
    resto = c % x
    return billetes,resto

while clave != passw:
    intentos += 1
    
    if clave == passw:
        print("clave incorrecta")
        break

    if intentos > 3:
        break

    print("clave invalida")
    clave = int(input("Ingrese de nuevo su clave: "))


if intentos > 3:
    print("tarjeta bloqueada")

if usuario == user :
    
    if clave == passw:
        monto = int(input("¿Cuanto quiere retirar?: "))
        
        if monto > saldo_usuario and monto > saldo_cajero:
            print("monto no perimitido")
        else:

            saldo_usuario -= monto
            saldo_cajero -= monto
            b, r = bills(monto,billetes_20)
            c , r = bills(r , billetes_10)
            j , r = bills(r, billetes_5)

            print("saldo cuenta="+str(saldo_usuario))
            print("saldo cajero="+str(saldo_cajero))
            print("billetes20000="+str(b))
            print("billetes10000="+str(c))
            print("billetes5000="+str(j))





