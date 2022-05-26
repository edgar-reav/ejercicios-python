#Cajero Automático

#Credeciales de prueba para comparar
usuario_ejemplo = 10334151
clave_ejemplo = 1803

#Datos de ejemplo del cajero
saldo_cajero = 1000000
saldo_usuario = 100000

intentos = 1

while True: 
    print("\n########## Usuario=10334151 ########## Clave=1803 ##########")
    
    #Ingresa las credenciales por teclado
    usuario = int(input("Ingrese el usuario: "))
    clave = int(input("Ingrese su clave: "))

    if(usuario != usuario_ejemplo): #Validando si el usuario es correcto 
        print("Usuario no coincide. Intentelo de nuevo")
    else: 
        while intentos < 3:
            if(clave != clave_ejemplo): #Validando si la clave del usuario es correcta
                print("Clave incorrecta. Tiene "+str(3-intentos)+" intentos para acceder o se bloqueara la tarjeta\n")
                clave = int(input("Ingrese de nuevo su clave: "))
                intentos+=1
            else:
                break
        
        if(intentos > 3): #el usuario tiene 3 intentos para ingresar sin que se bloquee la tarjeta
            print("Lo sentimos, su tarjeta ha sido bloqueada")
        break
  

if(intentos < 3): # Si coincide la clave con el usuario, se le pregunta cuanto quiere retirar de su cuenta
    
    print("Tiene un saldo de $"+str(saldo_usuario)+" en su cuenta.")
    monto = int(input("¿Cuánto desea retirar?: "))    
    
    if monto > saldo_usuario and monto > saldo_cajero:   
        print("monto no perimitido")
    else:
        saldo_usuario -= monto
        saldo_cajero -= monto
        print("\nSaldo cuenta: "+str(saldo_usuario))
        print("Saldo cajero: "+str(saldo_cajero))





