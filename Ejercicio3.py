#Función que permite leer caracteres
def introducir_caracter():
  try:
    caracter = input("Inroduzca un letra\n")
  except:
    pass
  else:
    return caracter

#Función que llama a introducir_caracter() y que comprueba si la letra introducida es igual a 'a' ó 'á'. Además, se utiliza la función lower() por si se introduce 'A' ó 'Á'
def contador_letras_a():
  contador_a=0
  while True:
    letra=introducir_caracter()
    letra=letra.lower()
    if letra=='a' or letra=='á':
      contador_a+=1
    if letra=='.':
      return contador_a

#A través de la función principal llamamos a la función contador_letras_a() que devuelve el numero de veces que se ha introducido la letra 'a'.
def main():
  numero_de_a = contador_letras_a()
  print ("Ha introducido {} veces la letra a".format(numero_de_a))
main()