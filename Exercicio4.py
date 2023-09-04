def init ():
    idadeAnos = int(input("Quantos anos de vida: "))
    idadeMeses = int(input("Quantos meses de vida: "))
    idadeDias = int(input("Quantos dias de vida: "))

    totalDias = (idadeAnos*365) + (idadeMeses * 30) + idadeDias

    print(f"São {totalDias} vividos")
