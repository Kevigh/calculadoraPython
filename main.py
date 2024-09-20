#Calculadora en Phyton

import time
from datetime import datetime

#funciones de Operaciones Matematicas

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "ERROR DE OPERACION!!!"
    
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        
        except:
            print("Error, introduce un numero valido")


historial = []

def agregar_al_historial(operacion):
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return historial.append(f"{hora_actual} - {operacion}")

while True:

    print("\nElige una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Mostrar historial")
    print("6. Salir")

    opcion = input("Introduce la opción que quieres realizar (1/2/3/4/5/6): ")

    if opcion == "6":
        print("Off")
        break

    if opcion in ["1","2","3","4"]:

        numero1 = pedir_numero("Introduce un primer número: ")
        numero2 = pedir_numero("Introduce un segundo número: ")

        if opcion == "1":
            operacion = f"Suma: {numero1} + {numero2} = {suma(numero1,numero2)}"

        elif opcion == "2":
            operacion = f"Suma: {numero1} - {numero2} = {resta(numero1,numero2)}"

        elif opcion == "3":
            operacion = f"Suma: {numero1} x {numero2} = {multiplicacion(numero1,numero2)}"

        elif opcion == "4":
            operacion = f"Suma: {numero1} / {numero2} = {division(numero1,numero2)}"

        else:
            print("Opcion invalida, elige una opcion valida")

        agregar_al_historial(operacion)
        print(operacion)

    if opcion == "5":
        while True:
            print("\nHISTORIAL")
            for i in historial:
                print(i)

            nueva_opcion = pedir_numero("Desea salir? (1) Yes, (0) No:")

            if nueva_opcion == 1:
                print("Saliendo del Historial")
                break

    time.sleep(3)