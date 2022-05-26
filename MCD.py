#ejercicio de máximo común divisior
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a
 
# solicitamos los dos números
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
#mostramos por consola
print("El máximo común divisor de ", num1," y ", num2," es ", mcd(num1, num2))
