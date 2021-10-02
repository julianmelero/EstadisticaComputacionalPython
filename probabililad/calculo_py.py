import random
import math
from inferencia import desviacion_standard, media


def poner_agujas(num_agujas):
    dentro_circulo = 0


    for _ in range(num_agujas):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distancia_desde_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_centro <= 1:
            dentro_circulo += 1
        
    return (4 * dentro_circulo) / num_agujas

def estimacion(num_agujas, n_simulacion):
    estimados = []

    for _ in range(n_simulacion):
        estimacion_pi = poner_agujas(num_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)

    sigma = desviacion_standard(estimados)

    print(f'Estimados {round(media_estimados, 5)}, y sigma {round(sigma,5)} con {num_agujas} agujas')

    return(media_estimados, sigma)

def estimar_pi(precision, num_intentos):
    num_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(num_agujas, num_intentos)
        num_agujas = num_agujas *  2

    return media



if __name__ == "__main__":
    estimar_pi(0.01, 1000)
    


