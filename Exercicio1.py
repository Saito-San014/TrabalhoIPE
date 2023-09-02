
def init () :
    numeros = []
    numero = int(input("Digite o numero: "))
    numeros.append(numero)
    for i in range(1,51):
        numeros.insert(0,numero - i)
        numeros.append(numero + i)
    print(numeros)