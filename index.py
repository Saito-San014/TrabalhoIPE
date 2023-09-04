import Exercicio1
import Exercicio2
import Exercicio3
import Exercicio4
import Exercicio5
import Exercicio6


sair = True

while sair:
    numExerc = int(input("Qual exercicio deseja corrigir de 1 até 6, qualquer outro valor para sair: "))
    if numExerc == 1:
        Exercicio1.init()
    elif numExerc  == 2:
        Exercicio2.init()
    elif numExerc == 3:
        Exercicio3.init()
    elif numExerc == 4:
        Exercicio4.init()
    elif numExerc == 5:
        Exercicio5.init()
    elif numExerc == 6:
        Exercicio6.init()
    else:
        sair = False
        break
    print("Fim do exercio")