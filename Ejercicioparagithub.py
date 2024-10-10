import math

#-3ptos
#subir a github later
#dado el siguiente ejercicio calcular el seno de el resultado de la multiplicacion de dos variables

num1 = float(input("Por favor introduzca los datos:"))
num2 = float(input("Por favor introduzca los datos:"))


Parte2= num1*num2
Parte3= math.radians(Parte2)
Resultado= math.sin(Parte3)

print("El seno es:", Resultado)