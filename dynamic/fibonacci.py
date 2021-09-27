
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


# Usando memorización

def fibonacci_dinamico(n,list = {}):
    if n == 0 or n== 1:
        return 1

    try:
        return list[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, list) + fibonacci_dinamico(n - 2, list)
        list[n] = resultado

        return resultado



if __name__ == "__main__":
    print(fibonacci_dinamico(50))