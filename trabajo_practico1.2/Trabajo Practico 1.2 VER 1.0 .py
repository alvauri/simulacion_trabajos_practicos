import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import os

global cantApFav

def ruleta():
    return rnd.randint(0,36)

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def girar(calculaPromedio, modo, dinero_tot = None):
    if dinero_tot == None:
        dinero_disp = 0
    else:
        dinero_disp = dinero_tot
    valorApuesta = 1
    cantApFav = 0
    resultados = []
    resultados.append(dinero_disp)
    frecRelativa = []
    apuesta = 1
    if (modo == "Fibonacci"):
        contafib = 1

    for i in range(tiradas):
        result = ruleta()
        if (modo == "Martingala"):
            if (result%2 == apuesta) & (result != 0):
                dinero_disp += valorApuesta
                valorApuesta = 1
                cantApFav+=1
            else:
                dinero_disp -= valorApuesta
                valorApuesta = valorApuesta*2
        elif (modo == "D'Alambert"):
            if (result%2 == apuesta) & (result != 0):
                cantApFav+=1
                dinero_disp += valorApuesta
                if apuesta > 1:
                    valorApuesta = valorApuesta -1
            else:
                dinero_disp -= valorApuesta
                valorApuesta = valorApuesta + 1
        elif (modo == "Fibonacci"):
            contafib = 0 #OJO AQUI YO PUSE ESTO NO SE SI ESTA BIEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if (result % 2 == apuesta) & (result != 0):
                dinero_disp += valorApuesta        
                cantApFav += 1
                if contafib < 3:
                    contafib = 1
                else:
                    contafib -= 2
            else:
                dinero_disp -= valorApuesta
                contafib += 1
            valorApuesta = fib(contafib)
        resultados.append(dinero_disp)
        frecRelativa.append(cantApFav/(i+1))
        if calculaPromedio:
            promedio[0][i]=promedio[0][i]+dinero_disp/repeticiones
            promedio[1][i]=promedio[1][i]+cantApFav/(i+1)/repeticiones
        if dinero_tot != None:
            if dinero_disp == 0:
                break
            elif dinero_disp<valorApuesta:
                valorApuesta = dinero_disp
    results = []
    results.append(frecRelativa)
    results.append(resultados)
    return results

def correr(modo, dinero_tot = None):
    if tiradas == 1:
        results = girar(False, modo, dinero_tot)
        plt.plot(results[0])
        plt.title(modo + " - Frecuencia relativa de apuestas ganadas")
        plt.hlines((18/37),0,tiradas, color='red')
        plt.ylabel('Frecuencia relativa')
        plt.xlabel('Numero total de apuestas')
        plt.show()

        plt.plot(results[1])
        plt.title(modo)
        if dinero_tot != None:
            plt.ylabel('Dinero')
            plt.hlines(cap_ini,0,tiradas, color='red')
        else:
            plt.ylabel('Beneficio acumulado')
            plt.hlines(0,0,tiradas, color='red')
        plt.xlabel('Numero de apuestas')
        plt.show()
    else:
        global promedio
        promedio = [[],[]]
        din = []
        fr = []
        for i in range(tiradas):
            promedio[0].append(0)
            promedio[1].append(0)

        for j in range(repeticiones):
            results = girar(True, modo, dinero_tot)
            fr.append(results[0])
            din.append(results[1])

        for i in range(repeticiones):
            plt.plot(fr[i])
        plt.plot(promedio[1], color='black', label='Promedio')
        plt.legend(loc="lower left")
        plt.title(modo + " - Frecuencia relativa de apuestas ganadas")
        plt.hlines((18/37),0,tiradas, color='red')
        plt.ylabel('Frecuencia relativa')
        plt.xlabel('Numero total de apuestas')
        plt.show()

        for i in range(repeticiones):
            plt.plot(din[i])
        plt.plot(promedio[0], color='black', label='Promedio')
        plt.legend(loc="lower left")
        plt.title(modo)

        if dinero_tot != None:
            plt.ylabel('Dinero')
            plt.hlines(cap_ini,0,tiradas, color='red')
        else:
            plt.ylabel('Beneficio acumulado')
            plt.hlines(0,0,tiradas, color='red')
        plt.xlabel('Numero de apuestas')
        plt.show()

def menu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("1 - Martingala")
    print ("2 - Fibonacci")
    print ("3 - D'Alambert")
    print ("0 - Salir")

def martingalaMenu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("1 - MARTINGALA - Capital infinito")
    print ("2 - MARTINGALA - Capital acotado")
    print ("0 - Menu principal")  

def fibonacciMenu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("1 - FIBONACCI - Capital infinito")
    print ("2 - FIBONACCI - Capital acotado")
    print ("0 - Menu principal")

def  dAlambertMenu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("1 - D'Alambert - Capital infinito")
    print ("2 - D'Alambert - Capital acotado")
    print ("0 - Menu principal")  

if __name__ == '__main__':

    promedio = [[],[]]
    repeticiones = int(input('Indique la cantidad de veces a repetir el experimento:'))
    tiradas = int(input('Indique la cantidad de veces que se hara girar la ruleta:'))
    cap_ini = int(input("Indique el monto de capital inicial con el que comenzaremos: "))

    while True:

        menu()
        seleccion = input("Inserte su opcion >> ")
        if seleccion=="1":
            while True:
                martingalaMenu()
                seleccion = input("Inserte su opcion >> ")
                if seleccion=="1":
                    correr("Martingala")
                elif seleccion=="2":
                    correr("Martingala",cap_ini)
                elif seleccion=="0":
                    break
                else:
                    print(" ")
                    input("La opcion ingresada no es valida.")
                os.system('cls')
        elif seleccion=="2":
            while True:
                fibonacciMenu()
                seleccion = input("Inserte su opcion >> ")
                if seleccion=="1":
                    correr("Fibonacci")
                elif seleccion=="2":
                    correr("Fibonacci",cap_ini)
                elif seleccion=="0":
                    break
                else:
                    print(" ")
                    input("La opcion ingresada no es valida.")
                os.system('cls')
        elif seleccion=="3":
            while True:
                dAlambertMenu()
                seleccion = input("Inserte su opcion >> ")
                if seleccion=="1":
                    correr("D'Alambert")
                elif seleccion=="2":
                    correr("D'Alambert",cap_ini)
                elif seleccion=="0":
                    break
                else:
                    print(" ")
                    input("La opcion ingresada no es valida.")
                os.system('cls')
        elif seleccion=="0":
            break
        else:
            print ("")
            input("La opcion ingresada no es valida.")