#Función para leer numeros estrictamente distintos de 0.
def introducir_num():
  try:
    num=int (input("Introduzca un numero\n"))
    while num==0:
      num=int (input("Error. Introduzca un numero\n"))
  except:
    pass
  else:
    return num

#Función que pregunta por teclado cuantos numeros se van a introducir.
def numeros_a_introducir():
  cantidad_numeros= int (input("Cuantos numeros quiere meter\n"))
  return cantidad_numeros

#Función a través de la que se introducen los numeros leidos por teclado en una lista.
def lista(numeros_totales):
  lista=[]
  for i in range (numeros_totales):
    lista.append(introducir_num())
  resultado=comparacion_orden_ascendente(lista, numeros_totales)
  return resultado
  
#Función que indica si los elementos de la lista están estrictamente en orden ascendente
def comparacion_orden_ascendente(lista, numeros_totales):
  for i in range (numeros_totales-1):
    if int(lista[i])>= int(lista[i+1]):
      return 0
  return 1
  
#Desde la función main llamamos a la función lista, que a su vez llama a la función introducir_num para meter los elementos en la lista. Una vez metidos todos los elementos desde la función lista se llama a la función comparación_orden que devuelve 0 si no están estrictamente en orden ascendente, y devuelve 1 si lo están.
#Después devuelve la variable resultado a la función main, si es 1 se muestra por pantalla que están en orden ascendente y si devuelve 0 muestra que no.
def main():
  numeros_totales = numeros_a_introducir()
  valor=lista(numeros_totales)
  if valor==1:
    print("Los elementos de la lista están en orden ascendente\n")
  else:
    print("Los elementos de la lista no están en orden ascendente\n")
main()