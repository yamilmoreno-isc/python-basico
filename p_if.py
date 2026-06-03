#Pidele al usuario su edad
#dile niño es menor a 12, adolescente de 12 a 17, joven 18 a 25 y adulto mayor 60 o mas
"""
edad = int(input("Introduce tu edad: "))

if edad < 12:
    print("Niño")
elif edad < 18:      # ya sabemos que tiene 12 o más
    print("Adolescente")
elif edad < 26:      # ya sabemos que tiene 18 o más
    print("Joven")
elif edad < 60:      # ya sabemos que tiene 26 o más
    print("Adulto")
else:
    print("Adulto mayor")
"""
"""
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
operacion = input("Selecciona una opción +,-,*,/: ")
resultado = 0

if operacion == "+":
	resultado = numero1 + numero2
	print(f"{numero1} + {numero2} es: {resultado} ") 
elif operacion == "-":
	resultado = numero1 - numero2
	print(f"{numero1} - {numero2} es: {resultado} ")
elif operacion == "*":
	resultado = numero1 * numero2
	print(f"{numero1} * {numero2} es: {resultado} ")
elif operacion == "/":
	resultado = numero1 / numero2
	print(f"{numero1} / {numero2} es: {resultado} ")
else:
	print("No elegiste ninguna opción")
"""

peticionU = input("Introduce tu usuario: ")
peticionC = input("Introduce tu contraseña: ")
usuario = "yamil"
contrasenia = "1234"

if peticionU != usuario and peticionC != contrasenia:
    print("Ambos incorrectos")
elif peticionU != usuario:
    print("Usuario no encontrado")
elif peticionC != contrasenia:
    print("Contraseña incorrecta")
else:
    print("Bienvenido")

