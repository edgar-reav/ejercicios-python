from random import randint
from timeit import default_timer
import matplotlib.pyplot as plot

def Subarray_FuerzaB(array):
    cantidad_datos = len(array)
    suma_max = 0
    for i in range(0, cantidad_datos):
        suma = 0
        for j in range(1, cantidad_datos):
            suma += array[j]
            if suma > suma_max:
                suma_max = suma
    return suma_max

def generaLista(n):
  Lista = [randint(-10,10) for i in range(2**n)]
  return Lista

##########################################################
datos = []
registro_tiempo = []
i = 1

while i <= 20:
    arr = generaLista(i)
    inicio = default_timer()
    sumaSubarray = Subarray_FuerzaB(arr)
    fin = default_timer()
    tiempo = fin - inicio;
    registro_tiempo.append(tiempo)
    datos.append(i)
    print("Suma maxima del array: {}\nEl tiempo de ejecución [s]: {}\nCantidad de datos: {}\n".format(sumaSubarray,tiempo,2**i))
    i+=1


plot.grid(True, which="both")
plot.semilogy(datos, registro_tiempo)
plot.title('Gráfico Fuerza Bruta: Tiempo para N datos')
plot.ylabel('Tiempo de ejecución [seg]')
plot.xlabel('2**N cantidad de datos')
plot.savefig('fuerza-bruta.png')
plot.xticks(range(2,22,2))
#plot.show()