#recur-tiempo
from random import randint
from timeit import default_timer
import matplotlib.pyplot as plot

def maxSumaCruzada(arr, l, m, r):
    suma = 0
    sumaizq = float('-inf')
    i = m
    while i > (l-1):
        suma = suma + arr[i]
        if suma > sumaizq:
            sumaizq = suma
        i -= 1
    suma = 0
    sumader = float('-inf')
    i = m + 1
    while i < (r+1):
        suma = suma + arr[i]
        if suma > sumader:
            sumader = suma
        i+= 1
    return max(sumaizq+sumader, sumaizq, sumader)

def maxSumaRec(arr, l, r):
    if l == r:
        return arr[l]
    m = (l+r)//2
    return max(maxSumaRec(arr,l,m), maxSumaRec(arr,m+1,r), maxSumaCruzada(arr,l,m,r))

def generaLista(n):
    Lista = [randint(-10,10) for i in range(2**n)]
    return Lista

registro_tiempo =[]
can_datos = []
i = 1;

while i <= 20:
    inicio = default_timer();
    Lista = generaLista(i)
    n = len(Lista)-1
    max_sum = maxSumaRec(Lista, 0, n)
    fin = default_timer();
    tiempo = fin -inicio;
    print("Suma maxima del array: {}\nEl tiempo de ejecución [s]: {}\nCantidad de datos: {}\n".format(max_sum,tiempo,2**i))
    registro_tiempo.append(tiempo)
    can_datos.append(i)
    i+=1

plot.grid(True, which="both")
plot.semilogy(can_datos, registro_tiempo)
plot.title('Gráfico Recursivo: Tiempo para N datos')
plot.ylabel('Tiempo de ejecución [seg]')
plot.xlabel('2**N cantidad de datos')
plot.savefig('recursivo.png')
plot.xticks(range(2,22,2))
#plot.show()