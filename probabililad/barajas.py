
import random
import collections

PALOS = ['espada', 'corazon', 'rombo' ,'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota','reina', 'rey']

def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano


def main(tamano_mano, n_simulacion):
    barajas = crear_baraja()
    manos = []

    for _ in range(n_simulacion):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])


        counter = dict(collections.Counter(valores))

        for valor in counter.values():
            if valor == 2:
                pares +=1
                break

    probabilidad_par = pares / n_simulacion
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')
    

if __name__ == "__main__":
    
    tamano_mano = int(input('Tamaño de la mano:'))
    intentos = int(input('Número de intentos:'))
    main(tamano_mano, intentos)
    