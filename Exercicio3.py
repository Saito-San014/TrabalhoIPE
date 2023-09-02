
def init():
    numeros = []
    menor = 0
    posicoes = ["primeiro", "segundo", "terceiro"]
    numeros.append(float(input("Digite o primeiro numero: ")))
    numeros.append(float(input("Digite o segundo numero: ")))
    numeros.append(float(input("Digite o terceiro numero: ")))
    if numeros[0] < numeros[1]:
        if numeros[0] < numeros[2]:
            menor = 0
    elif numeros[1] < numeros[2]:
        menor = 1
    else:
        menor = 2
    print(f"O menor numero digitado é o {posicoes[menor]}, sendo {numeros[menor]}")
