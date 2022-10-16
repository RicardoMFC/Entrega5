#Función para leer numeros estrictamente distintos de 0.
def introducir_num():
  i=0
  try:
    num=int (input("Introduzca un numero\n"))
    while num==0 and i==0:
    i+=1
      num=int (input("Error. Introduzca un numero\n"))
  except:
    pass
  else:
    return num

#Función que pregunta por teclado cuantos numeros se van a introducir.
def numeros_a_introducir():
  cantidad_numeros= int (input("Cuantos numeros quiere meter\n"))
  return cantidad_numeros

#Función que indica si los numeros están estrictamente en orden ascendente
def comparacion_orden_ascendente(numeros_totales):
  contador=0
  val=1
  while True:
    numero=introducir_num()
    if contador>0 and aux>numero:
      val=0
    aux=numero
    contador+=1
    if contador==numeros_totales:
      return val
#Utilizo la variable auxiliar para almacenar el numero y así poder compararlo con el siguiente que se va a introducir. La función devuleve 1 si se verifica que están en orden ascendente y sino devuelve un 0.
#Indico que el valor=1 porque supongo que se cumple que están ordenados en orden ascendente, si para algún caso no se cumple que el anterior numero (aux) es menor que numero, el valor cambia a 0.
      
def main():
  numeros_totales = numeros_a_introducir()
  valor = comparacion_orden_ascendente(numeros_totales)
  if valor==1:
    print ("Están ordenados en orden ascendente\n")
  else:
    print ("No están ordenados en orden ascendente\n")
main()