print("===== CALCULADORA =====")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elegí una operacion: ")

if opcion == "1":
    suma = num1 + num2
    print("El resultado es:", suma)

elif opcion == "2":
    resta = num1 - num2
    print("El resultado es:", resta)

elif opcion == "3":
    multiplicacion = num1 * num2
    print("El resultado es:", multiplicacion)

elif opcion == "4":
    if num2 == 0:
      print ("no se puede dividir por cero")
    else:
     division = num1 / num2
     print("El resultado es:", division)

else:
    print("Opcion no valida")         