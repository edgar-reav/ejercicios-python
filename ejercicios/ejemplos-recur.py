'''
def MaxR(L, n):
    if (n == 1):
        return L[0]
    return max(L[n - 1], MaxR(L, n - 1))

def Maximo(L,n):
    x = MaxR(L,n)
    return L.index(x)

L = [1, 4, 45, 6, -50, 10, 2]
n = len(L)
print(Maximo(L, n))
'''



##############################################
from pickletools import read_uint1


def cerro(L, a, b):
    if a > b:
        return -1
    else:
        m = (a + b) // 2
        if L[m-1] < L[m] and L[m] > L[m+1]:
            return cerro(L, m+1, b)
        else:
            return cerro(L, a, m-1)

##################################################

def valle(L, a, b):
    if a > b:
        return -1
    else:
        m = (a + b) // 2
        if L[m-1] > L[m] and L[m] > L[m+1]:
            return valle(L, m+1, b)
        else:
            return valle(L, a, m-1)

########################################################
def CalcMaxMitad(arr, mitad):
    suma = 0
    max_izq = -100000000000

    for numero in arr[mitad-1::-1]:
        suma = suma + numero
        if(suma > max_izq):
            max_izq = suma

    suma = 0
    max_der = -100000000000

    for numero in arr[mitad:]:
        suma = suma + numero
        if(suma > max_der):
            max_der = suma
    
    return max_izq + max_der

def MaxArray(arr):
    if len(arr) == 1:
        return arr[0]
    
    mitad = len(arr)//2
    arr_izq = arr[0:mitad]
    arr_der = arr[mitad:]

    max_izq = MaxArray(arr_izq)
    max_der = MaxArray(arr_der)
    max_mitad = CalcMaxMitad(arr, mitad)

    return max(max_izq, max_der, max_mitad)

#################################################################
#recursividad
def totalPaginas(libros):
    if len(libros) == 1:
        return libros[0]

    return libros[0] + totalPaginas(libros[1:])

############################################33
#programmacion dinamica
def cortar_varilla(tamano_varilla, lista_precio):
    if tamano_varilla == 0:
        return 0
    mejor_valor = 0
    for i in range(1, tamano_varilla+1):
        valor = lista_precio[i] + cortar_varilla(tamano_varilla-i, lista_precio)
        if valor > mejor_valor:
            mejor_valor = valor

    return mejor_valor



def cortar_varrilla_dos(tamano_varilla, lista_precios, memory):
    if tamano_varilla == 0:
        return 0
    if memory[tamano_varilla] != -1:
        return memory[tamano_varilla]
    
    mejor_valor = 0
    for i in range(1, tamano_varilla+1):
        valor = lista_precios[i] + cortar_varrilla_dos(tamano_varilla-i, lista_precios, memory)
        if valor > mejor_valor:
            mejor_valor = valor

    memory[tamano_varilla] = mejor_valor
    return mejor_valor



# def cortar_varrilla_tres(tamano_varilla, lista_precios):
#    tabla = [0] * (tamano_varilla+1)

#    for varilla_actual in range(1, tamano_varilla+1):
#        mejor_valor = 0
#        for i in range(1, varilla_actual+1):
#            valor = lista_precios[i] + tabla[varilla_actual-i]
#            if valor > mejor_valor:
#                 mejor_valor = valor
        
#         tabla[varilla_actual] = mejor_valor

#     return tabla[tamano_varilla]


def cortar(tamano_varilla, lista_precio, memory, camino):
    if tamano_varilla == 0:
        return 0
    if memory[tamano_varilla] != -1:
        return memory[tamano_varilla]
    
    mejor_valor = 0
    mejor_corte = 0

    for i in range(1, tamano_varilla+1):
        precio = 0 if len(lista_precio) <= i else lista_precio[i]
        valor = precio + cortar_varilla(tamano_varilla-i, lista_precio, memory, camino)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_corte = i
   
    memory[tamano_varilla] = mejor_valor
    camino[tamano_varilla] = mejor_corte

    return mejor_valor
    

   

 
#################################################3333



Lista = [6, 2, -1, 1, 3, 7] 
#print(valle(Lista, 0, len(Lista)))

Lista2 = [1, 3, 4, 5, 0, -3]
#print(cerro(Lista, 0, len(Lista2)))
