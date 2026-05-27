#edad = int(input("¿Cuantos años tienes?"))

#if edad >= 18:
#	print("Eres mayor de edad")
#else:
#	print("Eres menor de edad")

"""nota = int(input("¿Cuál es tu nota?"))

if nota >= 90:
	print("Excelente")
elif nota >= 80:
	print("Bien")
elif nota >= 70:
	print("Regular")
else:
	print("Reprobado")"""

"""salario = int(input("¿Cúanto dinero ganas al mes?: "))

if salario >= 15000:
	print("Salario alto")
elif salario >= 5000:
	print("Salario medio")
else:
	print("Salario bajo")
"""

"""edad = int(input("Cuántos años tienes?: "))
tiene_licencia = input("Tienes licencia? si/no: ")

if edad >= 18 and tiene_licencia == "si":
	print("Puedes manejar")
elif edad >= 18 and tiene_licencia == "no":
	print("Eres mayor de edad, pero no puedes manejar")
else:
	print("Eres menor de edad")"""

edad = int(input("Cuántos años tienes?: "))

if edad >= 18:
	tiene_licencia = input("Tienes lincencia? si/no: ")
	if tiene_licencia == "si":
		print("Puedes manejar")
	elif tiene_licencia == "no":
		print("No puedes manejar")
else:
    print("Eres menor de edad")

