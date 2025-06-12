print("Calculadora")
print("1. Sumar.")
print("2. Restar.")
print("3. Multiplicar.")
print("4. Dividir.")
print("5. Salir.")

opcion = int(input("ingrese una opcion: "))

while opcion < 5:
    if opcion == 1:
        
        num1 = int(input("Ingrese la primera variable: "))
        num2 = int(input("Ingrese la segunda variable: "))
        resultado = num1 + num2
        print(f"el resultado es: {resultado}")
    elif opcion == 2:
        um1 = int(input("Ingrese la primera variable: "))
        num2 = int(input("Ingrese la segunda variable: "))
        resultado = num1 - num2
        print(f"el resultado es: {resultado}")
    elif opcion == 3:
        um1 = int(input("Ingrese la primera variable: "))
        num2 = int(input("Ingrese la segunda variable: "))
        resultado = num1 * num2
        print(f"el resultado es: {resultado}")
    elif opcion == 4:
        um1 = int(input("Ingrese la primera variable: "))
        num2 = int(input("Ingrese la segunda variable: "))
        resultado = num1 / num2
        print(f"el resultado es: {resultado}")

print("Gracias, hasta pronto")
