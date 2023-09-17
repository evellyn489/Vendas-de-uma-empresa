import pandas as pd

materiais_df = pd.read_excel("produtos_precos.xlsx")

def vender(produto, quantidade_vendida):
    if produto in materiais_df['Produto'].values:
        quantidade_em_estoque = int(materiais_df[materiais_df['Produto'] == produto]['Quantidade no Estoque'])
        
        if quantidade_vendida > quantidade_em_estoque:
            print('Quantidade excede o limite. Tente Novamente!')
        else:
            materiais_df.loc[materiais_df['Produto'] == produto, 'Quantidade no Estoque'] -= quantidade_vendida
            materiais_df.loc[materiais_df['Produto'] == produto, 'Quantidade Vendida'] += quantidade_vendida

            print(f"{quantidade_vendida} unidades de {produto} foram vendidas.")
        
    else:
        print(f"Produto '{produto}' não encontrado.")


def qtd_produtos_vendidos():
    soma_quantidade = 0
    vendas = materiais_df['Quantidade Vendida'].astype(int)

    for valor in vendas:
        soma_quantidade += valor
    
    print(f'Foram vendidas {soma_quantidade} unidades de produtos ao total!')

def qtd_total_dinheiroRecebido():
    total = 0
    
    for index, row in materiais_df.iterrows():
        renda = int(row['Quantidade Vendida']) * float(row['Preço de Venda'])
        total += renda
        
    print(f'Foi recebido R$ {total} ao total!')


def lucro_total():
    lucro = 0
    original = 0

    for index, item in materiais_df.iterrows():
        acrescimo = item['Quantidade Vendida'] * item['Preço de Venda']
        lucro += acrescimo

        valor_original = item['Quantidade Vendida'] * item['Valor Unitário']
        original += valor_original

    lucro_total = lucro - original
    
    print(f'O lucro total da empresa foi de R$ {lucro_total}!')

def produto_mais_vendido():
    maiorQuantidade = materiais_df['Quantidade Vendida'].loc[0]
    nomeProduto = materiais_df['Produto'].loc[0]

    empate = True

    for x,y in enumerate(materiais_df['Quantidade Vendida'].values):
        if y > maiorQuantidade:
            empate = False
            maiorQuantidade = y
            nomeProduto = materiais_df['Produto'].loc[x]
    
    if empate:
        print('Os produtos apresentam a mesma quantidade de vendas.')
    
    else:
        print(f'O produto {nomeProduto} foi o item mais vendido com {maiorQuantidade} quantidades.')

def produto_menos_vendido():
    menorQuantidade = materiais_df['Quantidade Vendida'].loc[0]
    nomeProduto = materiais_df['Produto'].loc[0]

    empate = True

    for x,y in enumerate(materiais_df['Quantidade Vendida'].values):
        if y < menorQuantidade:
            empate = False
            menorQuantidade = y
            nomeProduto = materiais_df['Produto'].loc[x]
    
    if empate:
        print('Os produtos apresentam a mesma quantidade de vendas.')
    
    else:
        print(f'O produto {nomeProduto} foi o item menos vendido com {menorQuantidade} quantidades.')

def repor_estoque(produto, quantidade):
    if produto in materiais_df['Produto'].values:
        materiais_df.loc[materiais_df['Produto'] == produto, 'Quantidade no Estoque'] += quantidade
    
    print(f"Foram adicionados {quantidade} quantidades do item {produto}")


print(materiais_df)

while True:
    print("\nMenu:")
    print("1. Vender produto")
    print("2. Visualizar quantidade total de produtos vendidos")
    print("3. Visualizar dinheiro total recebido")
    print("4. Visualizar lucro total")
    print("5. Repor estoque")
    print("6. Visualizar o produto mais vendido")
    print("7. Visualizar o produto menos vendido")
    print("8. Sair")



    escolha = int(input("Escolha uma opção (1, 2, 3, 4, 5, 6, 7, 8): "))

    if escolha == 1:
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        vender(produto, quantidade)

    elif escolha == 2:
        qtd_produtos_vendidos()

    elif escolha == 3:
        qtd_total_dinheiroRecebido()

    elif escolha == 4:
        lucro_total()
    
    if escolha == 5:
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digita a quantidade que quer repor: "))
        repor_estoque(produto, quantidade)

    elif escolha == 6:
        produto_mais_vendido()

    elif escolha == 7:
        produto_menos_vendido()
    
    elif escolha == 8:
        break