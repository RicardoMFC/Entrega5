#Función que pregunta por teclado cuantos elementos tiene la lista.
def tamano_lista():
  longitud= int (input("Indique la longitud de la lista\n"))
  return longitud

#Función a través de la que se introducen los numeros leidos por teclado en una lista.
def introducir_lista(longitud):
  lista=[]
  for i in range (longitud):
    lista.append(input("Introduzca el elemento de la lista\n"))
    
  return lista
#Función en la que se guardan los elementos en la lista ordenados de mayor a menor numero de caracteres, a través de la función sort(). Después, mediante un bucle while que iniciamos con i=0, guardamos todos los elementos que tengan tantos caracteres como el primero de la lista en una lista auxiliar. 
def elementos_con_mas_caracteres(longitud, lista):
  aux=[]
  lista.sort(key=len, reverse=1)
  i=0
  while len(lista[i])==len(lista[0]):
    aux.append(lista[i])
    i+=1
  x=len(lista[0])
  return aux, i, x

#Función principal desde la que llamamos al resto de funciones.
def main():
  longitud = tamano_lista()
  lista = introducir_lista(longitud)
  lista_aux, contador, numero_caracteres = elementos_con_mas_caracteres(longitud, lista)
  if contador ==1:
    print("El elemento con más caracteres de la lista es {}, tiene {} caracteres\n".format(lista_aux, numero_caracteres))

  else:
    print("Hay {} elementos con el mayor numero de caracteres, {} cada uno tiene {} caracteres\n".format(contador,lista_aux,numero_caracteres))
main()