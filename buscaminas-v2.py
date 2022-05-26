
import random

####################################################################

def Abrir_Arhivo(Nombre_Del_Archivo):
    lista = []
    archivo = open(Nombre_Del_Archivo, "r")
    lines = archivo.readlines()

    for line in lines:
        line = line.rstrip()
        lista.append(line)
    archivo.close()
    
    return lista

####################################################################

def Crear_Archivo_Sal(Nombre_Archivo,Archivo_Lista,Dimension_Tablero):

    Nombre_Archivo = Nombre_Archivo.replace('.txt','.sal')

    Archivo = open(Nombre_Archivo,'w')
    Archivo.write(str(Dimension_Tablero)+'\n')

    for mina in Archivo_Lista:
        Archivo.write(mina+'\n')

    Archivo.close()

####################################################################

def Modo_De_Juego(Archivo_lista):
    
    Dimension_Tablero = int(Archivo_lista[0])
    Dificultad = Archivo_lista[1]
    porcentaje = 0

    if Dificultad == 'F':
        porcentaje = 10
    if Dificultad == 'M':
        porcentaje = 15
    if Dificultad == 'D':
        porcentaje = 20
    if Dificultad == 'X':
        porcentaje = 30

    Total_Minas = pow(Dimension_Tablero,2)
    Cantidad_Minas = (Total_Minas * porcentaje)//100

    return Cantidad_Minas,Dimension_Tablero

###################################################################

def Minas_Aleatorias(numero_minas,dimension_tablero):
    i = 0
    abecedario = list(map(chr,range(65,91)))
    cord_minas = []

    while True:
        columnas = random.randint(1,dimension_tablero)
        filas = random.randint(0,dimension_tablero-1)

        cod_fila = abecedario[filas]
        coordenada = cod_fila+str(columnas) 

        if coordenada not in cord_minas:
            cord_minas.append(coordenada)
            i +=1

        if i == numero_minas:
            break

    return cord_minas

####################################################################

def Crear_Tablero(Dimension_Tablero,valor):
    
    abecedario = list(map(chr,range(65,91)))
    tablero = []
    numeros = []

    for i in range(Dimension_Tablero+1):
        if i == 0:
            numeros.append(' ')
        if i > 0:
            numeros.append(str(i))

    tablero.append(numeros)

    for letra in range(Dimension_Tablero):
        tablero.append([abecedario[letra]])

    for x in range(Dimension_Tablero):
        for y in range(Dimension_Tablero):
            tablero[x+1].append(valor)

    return tablero

#########################################################################

def Print_tablero(tablero):
    for i in range(len(tablero)):
        for k in range(len(tablero)):
            if i == 0:  
                if len(tablero[i][k]) < 2:
                    if tablero[i][k] == '9':
                         print(tablero[i][k],end="  ")
                    else:
                         print(tablero[i][k],end="  ")
                else:
                    print(tablero[i][k],end=" ")
            else:
                 print(tablero[i][k],end="  ")
        print()
    return ()

#############################################################################

def Separar_Archivo_SAL(Archivo_Sal):
    
    Dimension_Tablero = int(Archivo_Sal[0])
    Archivo_Sal.pop(0)

    return Dimension_Tablero,Archivo_Sal 
    

##############################################################

def Colocar_minas(Cord_Minas_Lista,tablero):

    abecedario = list(map(chr,range(64,91)))

    for mina in Cord_Minas_Lista:
        if len(mina) < 3 :
            letra = mina[0]
            num = int(mina[1])
        else:
            letra = mina[0]
            num = int(mina[1:3])
            
        ln = abecedario.index(letra)

        tablero[ln].pop(num)
        tablero[ln].insert(num,'*')

    return tablero 

#########################################################################

def Poner_Pista(lista, Dimension):
    for y in range(Dimension+1):
        for x in range(Dimension+1):
           if lista[y][x]=="*":
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0<= y+i <= Dimension and 0<= x+j <= Dimension:
                            if type(lista[y+i][x+j])!= str:
                                lista[y+i][x+j]+=1                  
    return lista


##############################################################################################

def Descubrir_minas(coordenada,listaOculta,listaVisible):
    coordenada = coordenada.upper()
    abecedario = list(map(chr,range(64,91)))
    
    letra = coordenada[0]
    N = int(coordenada[1:])

    L = abecedario.index(letra)

    valor = listaOculta[L][N]
    
    listaVisible[L].pop(N)
    listaVisible[L].insert(N,valor)

    return listaVisible
    
##########################################################################################
def Repetir_Mina(MINA,DIMENSION):
    abecedario = list(map(chr,range(65,65+DIMENSION)))
    numero = [str(num) for num in range(1,DIMENSION+1)]
    lista = [abecedario,numero]
    numero = MINA[1:]

    if len(MINA) == 2 or len(MINA) == 3:
        letra = MINA[0]
        if letra in lista[0]:
            if numero in lista[1]:
                return True
    return False
##########################################################################

def contar(lista,coordenada,contador):

    if coordenada in lista:
        return contador
    else:
        lista.append(coordenada)
        contador += 1

    return contador


########################################################################################


def Casilla_Tablero(tablero,dimension):

    while True:
        
        Print_tablero(tablero)
        casilla = str(input("Ingresa la casilla del tablero que quieres abrir: "))
        casilla = casilla.upper()
        casx = Repetir_Mina(casilla,dimension)
        if casx == True:
            return casilla
            break

########################################################################3

def Perdiste(lista,oculto,visible):
    for coordenada in lista:
        tablero = Descubrir_minas(coordenada,oculto,visible)  
    return tablero

#####################################################################################

def OpcionDeJuego():
    tipos_opciones = ['1','2','3']
    
    while True:
        
        opcion = str(input("Escoge una opción: (1) Generar tablero (2) Cargar tablero (3) Salir : "))

        if opcion in tipos_opciones:
            
            opcion = int(opcion)

            if opcion == 1 or opcion == 2:

                while True:
                    
                    Nombre_Archivo = str(input('Ingresa el nombre del archivo: '))

                    try:
                        Data = Abrir_Arhivo( Nombre_Archivo )
                    except:
                        pass

                    else:
                        if Nombre_Archivo[-4:] == '.sal' and opcion == 2:
                            Data = Abrir_Arhivo( Nombre_Archivo )
                            break

                        if Nombre_Archivo[-4:] == '.txt' and opcion == 1:
                            Data = Abrir_Arhivo( Nombre_Archivo )
                            break

                return opcion,Nombre_Archivo
                break
            
            else:
                Nombre_Archivo = 'NINGUNO'
                return opcion,Nombre_Archivo
                break 

#######################################################################################


DATA_STATE = OpcionDeJuego()
opcion = DATA_STATE[0]


if opcion == 1:
    
    Nombre_del_Archivo = DATA_STATE[1]

    Archivo_txt = Abrir_Arhivo( Nombre_del_Archivo )
                
    Minas_Tablero , Dimension_Del_Tablero = Modo_De_Juego( Archivo_txt )

    Coordenadas_Minas_Tablero = Minas_Aleatorias( Minas_Tablero , Dimension_Del_Tablero )

    Crear_Archivo_Sal( Nombre_del_Archivo , Coordenadas_Minas_Tablero , Dimension_Del_Tablero )
    

                
                
if opcion == 2:

    Nombre_del_Archivo = DATA_STATE[1]

    coordenadas_puestas = []

    Data_Juego = Abrir_Arhivo( Nombre_del_Archivo )

    Dimension_Tablero,Lista_Minas = Separar_Archivo_SAL( Data_Juego )

    Numero_Minas = len(Lista_Minas)

    Total_para_Ganar = (pow(Dimension_Tablero,2) - Numero_Minas)

    visible = Crear_Tablero(Dimension_Tablero,'.')
    
    oculto = Crear_Tablero(Dimension_Tablero, 0)

    oculto = Colocar_minas(Lista_Minas,oculto)

    oculto = Poner_Pista(oculto,Dimension_Tablero)

    contador = 0

    while contador < Total_para_Ganar:

        abrir_casillas = Casilla_Tablero(visible,Dimension_Tablero)
        
        if abrir_casillas not in Lista_Minas:

            contador = contar(coordenadas_puestas,abrir_casillas,contador)
            visible = Descubrir_minas(abrir_casillas,oculto,visible)

        else:
            break
    
    
    if contador < Total_para_Ganar:

        visible = Perdiste(Lista_Minas,oculto,visible)
        Print_tablero(visible)
        print("Perdiste")

    else:
        visible = Descubrir_minas(abrir_casillas,oculto,visible)
        visible = Perdiste(Lista_Minas,oculto,visible)
        Print_tablero(visible)
        print("Ganaste")









    























