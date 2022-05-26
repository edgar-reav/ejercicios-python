#ite-tiempo
from random import randint
from timeit import default_timer
import matplotlib.pyplot as plot

def generaLista(n):
  Lista = [randint(-10,10) for i in range(2**i)]
  return Lista

i = 1
posicion = []
registro_tiempo = []

while i <= 20:
  inicio = default_timer();
  Lista = generaLista(i);
  rango = len(Lista)
  valorMaximo = 0
  valorActual = 0
  for j in range(rango):
    valorActual= max(Lista[j]+valorActual,Lista[j])
    if valorActual>valorMaximo:
      valorMaximo=valorActual
  fin = default_timer()
  tiempo = fin - inicio;
  print("Suma maxima del array: {}\nEl tiempo de ejecución [s]: {}\nCantidad de datos: {}\n".format(valorMaximo,tiempo,2**i))
  registro_tiempo.append(tiempo)
  posicion.append(i)
  i+=1

plot.grid(True, which="both")
plot.semilogy(posicion,registro_tiempo)
plot.title('Gráfico Iterativo: Tiempo para N datos')
plot.xlabel('2**N cantidad de datos')
plot.xticks(range(2,22,2))
plot.ylabel('Tiempo de ejecución [seg]')
plot.savefig('iterativo.png')
#plot.show()
