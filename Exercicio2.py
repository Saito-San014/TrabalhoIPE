
def init():
    numeros = []
    numeros.append(float(input("Digite o primeiro numero: ")))
    numeros.append(float(input("Digite o segundo numero: ")))
    numeros.append(float(input("Digite o terceiro numero: ")))
    numMaior = numeros[0]
    if numeros[1] > numMaior:
        numMaior = numeros[1]
    if numeros[2] > numMaior:
        numMaior = numeros[1]
    print(f"O maior numero digitado é o {numMaior}")
