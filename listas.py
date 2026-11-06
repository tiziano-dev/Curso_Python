numeros = [10,20,30,40,50]

print (numeros[0])
print (numeros[4])

numeros.append (60)

print (numeros)
suma = 0
for numero in numeros:
    print (numero)
    suma = suma + numero

promedio = suma / len(numeros)

print("El promedio es:", promedio)

# modificar, buscar y eliminar elementos

alumnos = ["uma","pedro","rocio","salome"]
alumnos[1] = "tiziano" 
print (alumnos)
if "rocio" in alumnos:
     print ("el alumno esta en la lista")
else: 
    print("el alumno no esta") 

alumnos.remove ("uma")
print (alumnos)

#listas, ciclos y funciones.

def mostrar_alumnos (lista):
        for alumno in lista :
         print(alumno)
alumnos = ["Tiziano", "Rocio", "Salome"]
mostrar_alumnos(alumnos)