lista=[]
tamañoLista= int(input())
for i in range(tamañoLista):
  valor=int(input())
  lista.append(valor)
print(lista)
rango=len(lista)
valorMaximo=0
valorActual=0
for i in range(rango):
  valorActual= max(lista[i]+valorActual,lista[i])
  if valorActual>valorMaximo:
    valorMaximo=valorActual
print(valorMaximo)
