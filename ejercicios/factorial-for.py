
def factorial(n):
    factorial_total = 1
    x = 1
    for x in range (n):
        factorial_total *= n
        x += 1
        n -= 1
    return factorial_total
 
try:
	numero = int(input("inserta un numero "))
 
	# Ejecutamos la función recusiva para el calculo

	calculo=factorial(numero)
	print ("El factorial de %s es %s" % (numero,calculo))
except:
	print ("Tiene que ser un valor numerico")
    

