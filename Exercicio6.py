import random


def init():
    itens_e_precos = [
    {"item": "Água Engarrafada", "faixa_de_preço": [2.0, 5.0]},
    {"item": "Alface", "faixa_de_preço": [2.0, 4.0]},
    {"item": "Arroz Branco", "faixa_de_preço": [4.0, 10.0]},
    {"item": "Bacon", "faixa_de_preço": [6.0, 12.0]},
    {"item": "Bananas", "faixa_de_preço": [3.0, 6.0]},
    {"item": "Café Torrado", "faixa_de_preço": [10.0, 20.0]},
    {"item": "Carne Moída", "faixa_de_preço": [10.0, 20.0]},
    {"item": "Cenouras", "faixa_de_preço": [2.0, 4.0]},
    {"item": "Cereal Matinal", "faixa_de_preço": [5.0, 12.0]},
    {"item": "Cerveja", "faixa_de_preço": [4.0, 8.0]},
    {"item": "Chá Preto", "faixa_de_preço": [4.0, 10.0]},
    {"item": "Frango", "faixa_de_preço": [6.0, 15.0]},
    {"item": "Iogurte", "faixa_de_preço": [2.0, 5.0]},
    {"item": "Leite", "faixa_de_preço": [3.0, 6.0]},
    {"item": "Maçãs", "faixa_de_preço": [3.0, 6.0]},
    {"item": "Manteiga", "faixa_de_preço": [5.0, 10.0]},
    {"item": "Massas", "faixa_de_preço": [2.0, 5.0]},
    {"item": "Ovos", "faixa_de_preço": [4.0, 8.0]},
    {"item": "Pão de Forma", "faixa_de_preço": [4.0, 7.0]},
    {"item": "Peixe", "faixa_de_preço": [12.0, 25.0]},
    {"item": "Queijo", "faixa_de_preço": [5.0, 12.0]},
    {"item": "Refrigerantes", "faixa_de_preço": [3.0, 6.0]},
    {"item": "Salsichas", "faixa_de_preço": [5.0, 10.0]},
    {"item": "Suco de Laranja", "faixa_de_preço": [3.0, 6.0]},
    {"item": "Tomates", "faixa_de_preço": [2.5, 5.0]},
    {"item": "Tortilhas", "faixa_de_preço": [4.0, 8.0]},
    {"item": "Vinho Branco", "faixa_de_preço": [20.0, 40.0]},
    {"item": "Vinho Tinto", "faixa_de_preço": [20.0, 60.0]},
    {"item": "Vodka", "faixa_de_preço": [30.0, 80.0]},
    {"item": "Whisky", "faixa_de_preço": [60.0, 150.0]},
]
    class produto():
        def __init__(self, nome, quantidade, preco):
            self.nome = nome
            self.quantidade = quantidade
            self.preco = preco
        def total(self):
            desconto = 0
            if self.quantidade <= 5 :
                desconto = 0.02
            elif self.quantidade <= 10:
                desconto = 0.03
            else:
                desconto = 0.05
            total = self.preco * self.quantidade
            return total
    autoteste = input("Auto tuestar s/n: ")
    produtos = []
    totalCompra = 0
    if autoteste == 's':
        
        while(len(produtos) < 10):
            item = random.randint(0,len(itens_e_precos)-1)
            novoProduto = produto(itens_e_precos[item]["item"],
                                random.randint(0,20),
                                random.uniform(itens_e_precos[item]["faixa_de_preço"][0],itens_e_precos[item]["faixa_de_preço"][1])
                                )
            if len(produtos) == 0:
                produtos.append(novoProduto)
            else:
                nomesItems = [pro.nome for pro in produtos]
                if novoProduto.nome not in nomesItems:
                    produtos.append(novoProduto)
                    
        
    else:
        while len(produtos) < 10: 
            nome = input("Nome do produto: ")
            quantidade = float(input("Quantidade do produto:"))
            preco = float(input("Preço do produto"))
            novoProduto = produto(nome, quantidade, preco)
            produtos.append = novoProduto

            for pro in produtos:
                print(f"O produto {pro.nome} custa {pro.preco:.2f} onde foi comprado", 
                    f"{pro.quantidade} dando um total de = {pro.total():.2f}")
                totalCompra += pro.total()
            print(f"O total da compra é de {totalCompra:.2f}")