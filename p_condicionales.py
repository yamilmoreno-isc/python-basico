#Ejercicio 1 — if
#Pídele al usuario dos números y dile cuál es el mayor. Si son iguales dile que son iguales.
"""
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))

if numero1 > numero2:
	print(f"El número {numero1} es mayor que {numero2}")
	
elif numero2 > numero1:
	print(f"El número {numero2} es mayor que {numero1}")

else:
	print("Son iguales")
"""

#Ejercicio 2 — for
#Imprime solo los números pares del 1 al 20. Pista: recuerda el operador %
"""
for numero in range(21):
	if numero % 2 == 0:
		print(f"Numero par: {numero}")
"""

#Ejercicio 3 — while
#Crea un programa que sume todos los números que el usuario vaya escribiendo.
# Cuando escriba 0 para y muestra el total.

numero = 0
suma = 0

while numero != 0:
    numero = int(input("Escribe un número: "))
    suma = suma + numero

print(f"El total es: {suma}")

	


