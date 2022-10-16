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

#Función que indica cual es el elemento o elementos con el mayor numero de caracteres de la lista. Con un bucle for se va comparando el elemento de la lista con el anterior, si el elemento es mayor que el anterior se guarda su longitud en una variabe X. Después se compara X con la longitud del primer elemento de la lista, si el primer elemento de la lista es más largo, se guarda en la X su longitud.
#Por último, creamos otro bucle for en el que metemos los elementos de longitud X (mayor longitud de los elementos de la lista) en un lista auxiliar (aux[]). Además, ponemos un contador para saber cuantas palabras de la lista tienen la máxima longitud, ya que puede ser más de una.
def elemento_mas_largo(lista, longitud):
  aux=[]
  contador=0
  for i in range (longitud-1):
    if len(lista[i]) < len(lista[i+1]):
      x=len(lista[i+1])
        
  if len(lista[0])>x:
    x=len(lista[0])

  for i in range (longitud):
    if x==len(lista[i]):
      aux.append(lista[i])
      contador+=1
      
  return aux, x, contador

#Función principal desde la que llamamos al resto de funciones.
def main():
  longitud = tamano_lista()
  lista = introducir_lista(longitud)
  lista2, numero_caracteres ,contador = elemento_mas_largo(lista, longitud)
  if contador ==1:
    print("El elemento con más caracteres de la lista es {}, tiene {} caracteres\n".format(lista2, numero_caracteres))

  else:
    print("Hay {} elementos con el mayor numero de caracteres, {} cada uno tiene {} caracteres\n".format(contador,lista2,numero_caracteres))
main()