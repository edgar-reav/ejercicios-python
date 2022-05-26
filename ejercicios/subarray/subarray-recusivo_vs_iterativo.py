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
  cantidad_datos = pow(2,n)
  Lista = [randint(-10,10) for i in range(cantidad_datos)]
  return Lista



############################################################################################################################

i = 1
can_dato=[]
rt_ite = []
rt_rec = []

while i <= 20:
    inicio = default_timer();
    Lista = generaLista(i);
################################################    iterativo
    rango = len(Lista)
    valorMaximo = 0
    valorActual = 0
    for j in range(rango):
        valorActual= max(Lista[j]+valorActual,Lista[j])
        if valorActual>valorMaximo:
            valorMaximo=valorActual
    fin = default_timer()
    tiempo = fin - inicio;
    rt_ite.append(tiempo)
###############################################     recursivo
    inicio = default_timer();
    n = len(Lista)-1
    max_sum = maxSumaRec(Lista, 0, n)
    fin = default_timer();
    tiempo = fin -inicio;
    rt_rec.append(tiempo)
    can_dato.append(i)
    i+=1

############################################################################################################################

plot.grid(True, which="both")
plot.semilogy(can_dato,rt_rec, can_dato, rt_ite)
plot.title('Gráfico comparativo: recursivo vs iterativo')
plot.legend(['Recursivo', 'Iterativo'])
plot.xlabel('2**N cantidad de datos')
plot.xticks(range(2,22,2))
plot.ylabel('Tiempo de ejecución [seg]')
plot.savefig('comparacion.png')
#plot.show()