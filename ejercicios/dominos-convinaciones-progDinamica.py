def CombinacionesPosiblesDominos(n_dominos):
    #Tamaño de los dominos 3 x 1 en un tablero de 3 x N° de dominos
    
    #Casos bases para n_dominos existen 1 o 2 combinaciones segun su tamaño de tablero
    if n_dominos <= 2:
        return 1
    elif n_dominos == 3:
        return 2
    else:
        #casos bases
        lista = [0]*(n_dominos+1)
        lista [1] = 1
        lista [2] = 1
        lista [3] = 2
        
        #iteracion en las combinaciones
        i = 4
        while i <= n_dominos:
            #[i-1] => caso donde queda un domino en forma vertical 
            #[i-3] => caso donde queda 3 dominos en forma vertical u horizontal 
            lista [i] = lista [i - 1] + lista [i - 3]
            i = i + 1
        
        #retorna la cantidad de combinaciones posibles
        return lista [-1]       

print(CombinacionesPosiblesDominos(50))
