import numpy as np

def LeerArchivo(dir_txt):
    txt = open(dir_txt,"r")
    #Extrae el archivo por lineas
    lineas = [lineas.strip('\n') for lineas in txt.readlines()]
    
    gallinas = np.full(int(lineas[0]), 0, dtype = int).tolist()
    tiros = [tiro.split() for tiro in lineas[2: 2+int(lineas[1])]]
    preguntas = [pregunta.split() for pregunta in lineas[2+int(lineas[1])+1:]]

    return gallinas, tiros, preguntas

#Algoritmo de divide y venceras, Añadiendo el maiz a cada gallina
def lanzaMaiz(gallinas, desde, hasta, comienzo, final):
    #caso base
    if comienzo == final:
        #si el elemento iterado esta en el rango de la pregunta se le suma una unidad (+1).
        if (comienzo >= desde) and (comienzo <= hasta) : 
            gallinas[comienzo]+=1
        #Retorna 0 para detener la recursividad llegado al centro de la lista
        return 0

    mitad = (comienzo + final) // 2
    lanzaMaiz(gallinas, desde, hasta, comienzo, mitad)      #Lado izquierdo 
    lanzaMaiz(gallinas, desde, hasta, mitad+1, final)       #Lado derecho

    return gallinas

#Suma las cantidades de maiz segun las preguntas y las escribe en un txt
def pregLanzamientos(archivo, gallinas, preguntas, len):
    archivo = open("salida/"+"salida-"+archivo, "w")
    i = 1
    for pregunta in preguntas:
        #suma los elementos desde n hasta m 
        suma = sum( gallinas[ int(pregunta[0]) : int(pregunta[1])+1 ] )

        if(i < len(preguntas)):
            archivo.write(str(suma)+"\n")
        else:
            archivo.write(str(suma))
        
        i+=1
    
    archivo.close()    


#_main_#
archivo = "ejem3.txt"
gallinas, tiros, preguntas = LeerArchivo(archivo)

# print(gallinas)
# print(tiros)
# print(preguntas)

comienzo = 0
final = len(gallinas)-1

#Segun cuantos tiros de maiz haya...
for tiro in tiros:
    #...Se rellenaran los tubos de cada gallina
    gallinas = lanzaMaiz(gallinas, int(tiro[0]), int(tiro[1]), comienzo, final)

#Devuelve las cantidades de cuanto maiz hay, las preguntas, desde n hasta m tuberia.
pregLanzamientos(archivo, gallinas, preguntas, len(preguntas))





########################## archivo.txt ################################
# 9                 gallinas
# 3                 lazamientos de maiz a las gallinas
# 2 6               lazamiento 1
# 5 8               lanzamiento 2
# 3 7               lanzamiento 3
# 1                 preguntas para contar cuantos maices hay 
# 3 8               pregunta 1 => desde 3 hasta 8, cuantos maices hay