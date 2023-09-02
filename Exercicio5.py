import random
import numpy as np
import pandas as pd
def init():
    municipios = []
    municipio_sao_paulo = [
    "São Paulo",
    "Campinas",
    "Guarulhos",
    "São Bernardo do Campo",
    "São José dos Campos",
    "Santo André",
    "Osasco",
    "Ribeirão Preto",
    "Sorocaba",
    "Santos",
    "São José do Rio Preto",
    "Jundiaí",
    "Piracicaba",
    "São Vicente",
    "Itaquaquecetuba",
    "Mogi das Cruzes",
    "Diadema",
    "Carapicuíba",
    "Bauru",
    "Franca"
]
    class municipio:
        def __init__(self, nome, votosBranco, votosNulos, votosValidos):
            self.nome = nome
            self.votosBranco = votosBranco
            self.votosNulos = votosNulos
            self.votosValidos = votosValidos
            self.eleitores = votosBranco + votosNulos + votosValidos
    autoTeste = input("Auto tester com valores aleatorios: s/n")
    #Verifica se quer executar o auto teste do codigo
    if autoTeste == "s":
        while len(municipios)< 10:
            novoMunicipio = municipio(
                municipio_sao_paulo[random.randint(0,len(municipio_sao_paulo)-1)],
                                      random.randint(0,1000),random.randint(0,1000),
                                      random.randint(0,1000))
            if len(municipios) == 0:
                municipios.append(novoMunicipio)
            else:
                nomesMunicipios = [mun.nome for mun in municipios]
                if novoMunicipio.nome not in nomesMunicipios:
                    municipios.append(novoMunicipio)
        for xmun ,mun in enumerate(municipios):
            print(xmun," ",mun.nome)    
    else:
        while(len(municipios)<10):
            nome = input("Nome da município")
            votosBranco = int(input("Quantos votos em branco"))
            votosNulos =  int(input("Quantos votos nulos"))
            votosValidos =  int(input("Quantos votos validos"))
            novoMunicipio = municipio(nome, votosBranco, votosNulos, votosValidos)
            print(f"Com esses dados podesse afirmar que o município de {novoMunicipio.nome} têm {novoMunicipio.eleitores} eleitores")
            municipios.append(novoMunicipio)
    campos = ['nome', 'eleitores', 'votosValidos', 'votosBranco', 'votosNulos']
    newCampos = [ 'eleitores', 'votosValidos', 'votosBranco', 'votosNulos']
    df = pd.DataFrame([{campo: getattr(mun, campo) for campo in campos} for mun in municipios])
    dataResumo = {
        'nome': ['','','',''],
        'quantidade': [0,0,0,0],
        'porcentagem': ['','','','']
    }
    campoResumo =  ["Municipio com mais eleitores", 
                    "Município com mais votos em branco", 
                    "Município com mais votos nulos",
                    "Município com mais votos válidos"]
    for mun in municipios:
        if mun.eleitores > dataResumo["quantidade"][0]:
            dataResumo["nome"][0] = mun.nome
            dataResumo["quantidade"][0] = mun.eleitores
            dataResumo["porcentagem"][0] = str(round(mun.eleitores / mun.eleitores * 100))+'%'
        if mun.votosBranco > dataResumo["quantidade"][1]:
            dataResumo["nome"][1] = mun.nome
            dataResumo["quantidade"][1] = mun.votosBranco
            dataResumo["porcentagem"][1] = str(round(mun.votosBranco / mun.eleitores * 100))+'%'
        if mun.votosNulos > dataResumo["quantidade"][2]:
            dataResumo["nome"][2] = mun.nome
            dataResumo["quantidade"][2] = mun.votosNulos
            dataResumo["porcentagem"][2] = str(round(mun.votosNulos / mun.eleitores * 100))+'%'   
        if mun.votosValidos > dataResumo["quantidade"][3]:
            dataResumo["nome"][3] = mun.nome
            dataResumo["quantidade"][3] = mun.votosValidos
            dataResumo["porcentagem"][3] = str(round(mun.votosValidos / mun.eleitores * 100))+'%'
          
        data = {
            "Quantidade": [getattr(mun, campo) for campo in newCampos],
            "Porcetagem": [str(round(getattr(mun, campo) / mun.eleitores * 100,2))+"%"  for campo in newCampos]
        }
        dfMun = pd.DataFrame(data, index=[newCampos])
        dfResumo = pd.DataFrame(dataResumo,index=[campoResumo])
        print("\n",mun.nome)
        print(dfMun)
        print(dfResumo)
    
    print(df)
    #getattr(mun, campo) / mun.eleitores for campo in newCampos if type(getattr(mun, campo)) =="int" /