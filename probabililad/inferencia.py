import math
import random



def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0

    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_standard(X):
    return math.sqrt(varianza(X))

if __name__ == "__main__":
    X = [random.randint(9,12) for i in range(20) ]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_standard(X)
    print(f'Los valores son {X} y su media es {mu}')
    print(f'La varianza es {Var} y su desviación estándard es {sigma}')
   