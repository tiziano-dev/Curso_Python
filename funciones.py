def calcular_cuadrado(numero):
   resultado = numero ** 2
   return (resultado)

resultado = calcular_cuadrado(4)
print("El cuadrado es:", resultado)

def multiplicar (num1,num2):
   resultado = num1 * num2
   return (resultado)

resultado = multiplicar(7,8) 
print("El resultado es:", resultado)

def promedio(num1, num2, num3):
    resultado = (num1 + num2 + num3) / 3
    return resultado

resultado = promedio(8, 7, 9)
print("El promedio es:", resultado)

def es_mayor_de_edad (edad):
    return edad >= 18

print(es_mayor_de_edad(20))  
print(es_mayor_de_edad(18))  
print(es_mayor_de_edad(15))
