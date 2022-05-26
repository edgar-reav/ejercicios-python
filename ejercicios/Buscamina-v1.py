
def crear_lista(fila,columna,valor):
    b = [[' ', '1', '2', '3','4', '5', '6'],["A"],["B"],["C"],["D"],["E"],["F"]]
    for i in range(fila):
        for j in range(columna):
            b[i+1].append(valor)
    return b

def colocar_minas(mina,lista):
    letra = mina[0]
    posicion = int(mina[1])
    filas = [0,"A","B","C","D","E","F"]
    fila = filas.index(letra)
    if posicion > 0:
        if letra in filas:
            lista[fila].pop(posicion)
            lista[fila].insert(posicion,"*")

def exp_tablero(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end=" ")
        print()
    
def pista(lista, fila, columna):
    for y in range(fila+1):
        for x in range(columna+1):
           if lista[y][x]=="*":
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0<= y+i <= fila and 0<= x+j <=columna:
                            if type(lista[y+i][x+j])!= str:
                                lista[y+i][x+j]+=1                  
    return lista


def descubrir(cord,lista_oculta,lista_visible):
    cord = cord.upper()
    letra = cord[0]
    filas = [0,"A","B","C","D","E","F"]
    f = filas.index(letra)
    p = int(cord[1])
    valor = lista_oculta[f][p] 
    lista_visible[f].pop(p)
    lista_visible[f].insert(p,valor)

    return lista_visible


def contador(mina,mina2,mina3):
    total = 36
    if mina == mina2 and mina2 == mina3 :
        total -= 1
        return total
    if (mina != mina2 and mina == mina3) or (mina != mina3 and mina == mina2) or (mina2 != mina and mina2 == mina3):
        total -= 2
        return total
    if mina != mina2 and mina2 != mina3 and mina != mina3:
        total -= 3
        return total

def cord_contador(lista,cord,contador):
    if cord in lista:
        return contador
    else:
        lista.append(cord)
        contador += 1
        return contador
    
  
def repetir_mina(mina):
    if len(mina) == 2:
        x = mina[0]
        y = mina[1]
        vef = [['A','B','C','D','E','F'],['1', '2', '3','4', '5', '6']]
        if x in vef[0]:
            if y in vef[1]:
                return True
    return False
    

def repetir_string(string):
    string = string.upper()
    if len(string) == 6:
        m1 = repetir_mina(string[0:2])
        m2 = repetir_mina(string[2:4])
        m3 = repetir_mina(string[4:6])
        if m1 == False or m2 == False or m3 == False:
            return False
        else:
            return True
    return False


def fuera_parametros_tablero():
    while True:
        cast_minas = str(input("Ingresa el string con las posiciones de las minas: "))
        m = repetir_string(cast_minas)
        if m != False:
            exp_tablero(visible)
            return cast_minas
            break
        else:
            exp_tablero(visible)
            
def fuera_paramatros_casilla():
    while True:
        casilla = str(input("Ingresa la casilla del tablero que quieres abrir: "))
        casilla = casilla.upper()
        rep = repetir_mina(casilla)
        if rep != False:
            return casilla
            break
        exp_tablero(visible)
        

 
AllCasillas = []

oculto = crear_lista(6,6,0)
visible = crear_lista(6,6,".")

minas_cord = fuera_parametros_tablero()
minas_cord = minas_cord.upper()

mina1 = minas_cord[0:2]
mina2 = minas_cord[2:4]
mina3 = minas_cord[4:6]

contar = contador(mina1,mina2,mina3)

colocar_minas(mina1,oculto)
colocar_minas(mina2,oculto)
colocar_minas(mina3,oculto)

pista(oculto,6,6)

abrir_casillas = fuera_paramatros_casilla()
#print(abrir_casillas)

contador = 0
contador = cord_contador(AllCasillas,abrir_casillas,contador)


while contador < contar :

    if abrir_casillas == mina1 or abrir_casillas == mina2 or abrir_casillas == mina3:

        colocar_minas(mina1,visible)
        colocar_minas(mina2,visible)
        colocar_minas(mina3,visible)
        exp_tablero(visible)
        break

    else:
        
        visible = descubrir(abrir_casillas,oculto,visible)
        exp_tablero(visible)  

    abrir_casillas = fuera_paramatros_casilla()
    contador = cord_contador(AllCasillas,abrir_casillas,contador)
    

if contador < contar :
    print("PERDISTE")
else:
    visible = descubrir(abrir_casillas,oculto,visible)
    colocar_minas(mina1,visible)
    colocar_minas(mina2,visible)
    colocar_minas(mina3,visible)
    exp_tablero(visible)
    print("GANASTE")


