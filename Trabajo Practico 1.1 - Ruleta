#Trabajo Practico 1.1 - Ruleta
#Integrantes: Alvarez, Elicegui, Galarza, Muñoz

import numpy as np
import matplotlib.pyplot as plt


def grafHisto(bin_edges,hist,nroDeRepeticiones,nroVueltas):
    plt.bar(bin_edges[:-1], hist,   linewidth=1, width = 1,edgecolor='grey',alpha=0.7) 
    plt.xlim(-1, max(bin_edges)) 
    plt.grid(False)
    plt.title("Nros de Repeticiones: "+str(nroDeRepeticiones) +'\n'+
        "Vueltas de la Ruleta: "+str(nroVueltas) +'\n'+"Histograma el Nro "+ str(nro_frec))
    plt.xlabel('Conjunto de Numeros')
    plt.ylabel('Frecuencia Absoluta')

def grafFrecRel(frec_rel, frecuencia,nroDeRepeticiones,nroVueltas,nro_frec):
    for i in range(nroDeRepeticiones):
        plt.plot(frec_rel[i],linewidth=0.2)
        plt.axhline(frecuencia,color='red')
        plt.title("Nros de Repeticiones: "+str(nroDeRepeticiones) +'\n'+
        "Vueltas de la Ruleta: "+str(nroVueltas) +'\n'+"Frecuencia Relativa del Nro "+ str(nro_frec))
        plt.xlabel('Tiradas')
        plt.ylabel('Fr')    
        plt.xlim(0, nroVueltas)
        plt.ylim(0, max(frec_rel[i]))
    plt.show()

def grafEsperanza(esperanzas, esperanza, nroDeRepeticiones,nroVueltas):
    for i in range(nroDeRepeticiones):
        plt.plot(esperanzas[i],linewidth=0.2)
        plt.axhline(esperanza,color='red')
        plt.title("Nros de Repeticiones: "+str(nroDeRepeticiones) +'\n'+
        "Vueltas de la Ruleta: "+str(nroVueltas) +'\n'+"Esperanza el Nro "+ str(nro_frec))
    plt.show()

def grafDesvio(desvios, desvio, nroDeRepeticiones,nroVueltas):
    for i in range(nroDeRepeticiones):
        plt.plot(desvios[i],linewidth=0.2)
        plt.axhline(desvio,color='red')
        plt.title("Nros de Repeticiones: "+str(nroDeRepeticiones) +'\n'+
        "Vueltas de la Ruleta: "+str(nroVueltas) +'\n'+"Desvio Estandar el Nro "+ str(nro_frec))
        plt.xlabel('Tiradas')
        plt.ylabel('Valores')
    plt.show()

def grafVarianza(varianzas, varianza, nroDeRepeticiones,nroVueltas):
    for i in range(nroDeRepeticiones):
        plt.plot(varianzas[i],linewidth=0.2)
        plt.axhline(varianza,color='red')
        plt.title("Nros de Repeticiones: "+str(nroDeRepeticiones) +'\n'+
        "Vueltas de la Ruleta: "+str(nroVueltas) +'\n'+"Varianza el Nro "+ str(nro_frec))
        plt.xlabel('Tiradas')
        plt.ylabel('Valores')
    plt.show()

if __name__ == '__main__':
    nros = np.arange(0, 37)
    frecuencia = round(1/len(nros),3)
    media = round(np.mean(nros), 3)
    varianza = round(np.var(nros), 3)
    desvio = round(np.std(nros), 3) 
    nro_frec = int(input('Calcularemos la frecuencia del numero :'))
    cant_repet = int(input('Indique la cantidad de repeticiones: '))
    cant_tiradas = int(input("Indique la cantidad de tiradas: "))
    frec_rel=np.zeros((cant_repet,cant_tiradas+1))
    frecAbsoluta=np.zeros((cant_repet,cant_tiradas+1))
    promedios=np.zeros((cant_repet,cant_tiradas+1))
    desvios=np.zeros((cant_repet,cant_tiradas+1))
    varianzas=np.zeros((cant_repet,cant_tiradas+1))

    for j in range(cant_repet):
        for i in range(1,cant_tiradas+1):
            nros = np.random.randint(0,37,i,dtype ='int')
            nroAciertos = np.count_nonzero(nros == nro_frec)
            frec_rel[j][i] = nroAciertos/i
            frecAbsoluta[j][i] = nroAciertos
            promedios[j][i]=np.mean(nros)
            desvios[j][i]=np.std(nros)
            varianzas[j][i]=np.var(nros)
            if  i==cant_tiradas:
                hist, bin_edges = np.histogram(nros, bins = range(38))
                if j==0:
                    grafHisto(bin_edges,hist,1,cant_tiradas)
                    plt.show() 
                    plt.clf()
                if cant_repet != 1:    
                    grafHisto(bin_edges,hist,cant_repet,cant_tiradas)
    if cant_repet != 1:    
        plt.show() 
    grafVarianza(varianzas, varianza, cant_repet,cant_tiradas)
    grafFrecRel(frec_rel,frecuencia,cant_repet,cant_tiradas,nro_frec)
    grafEsperanza(promedios, media, cant_repet,cant_tiradas)
    grafDesvio(desvios, desvio, cant_repet,cant_tiradas)
    grafVarianza(varianzas, varianza, cant_repet,cant_tiradas)

