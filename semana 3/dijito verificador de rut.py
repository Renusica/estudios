
rut = "156083403"

mult = 2
num = 0
total = 0
suma_total = 0
resultado = 0
resto = 0

for caracter in reversed(rut):
    num = int(caracter)
    total = num * mult
    mult+=1
    if mult > 7:
        mult = 2
    print(total)
    suma_total = suma_total + total
    #resultado = total % 11

print(suma_total)
#resto = 






#rut = int(input("ingrese su rut: "))

#print(f"Su rut es: {rut}")