n = eval( input( "ingrese un numero para el factorial: "))

y = n
z = 1

while( y > 1) :
    z *= y
    y -= 1
    print("valor de z",z,"valor de y",y)
print("el valor del factorial del numero",n,"es",z)
    
