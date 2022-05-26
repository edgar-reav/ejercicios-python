#Juego adivina el número secreto
import random 

x =  random.randrange(1,100)
intentos = 6

while intentos > 0:
    print("\n#######################################################################")
    print("Adivina un número secreto aleatorio entre el rango de 1 y 100")
    print("#######################################################################\n")
    
    num = int(input("Yo creó que el número es...: "))
    intentos -= 1

    if x < num:
       print("El número secreto es menor. Te quedan "+str(intentos)+" intentos")
    if x > num:
        print("El número secreto es mayor. Te quedan "+str(intentos)+" intentos")
    if num == x:
        break

if num == x :
    print("Adivinaste, el número secreto era "+str(x)) 
if num != x:
    print("No adivinaste, el número secreto era "+str(x))
       
