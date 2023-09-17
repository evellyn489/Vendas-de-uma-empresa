'''Manipular o dataset produtos.xlsx para:
1. Mudar o nome da coluna "Quantidade" para "Quantidade no estoque"
2. Adicionar mais dez na quantidade de produtos no estoque, a fim de aumentar a quantidade de produtos disponíveis
3. Multiplicar toda a coluna do preço de venda por 1.20 pois isso representa um acréscimo de 20% na venda
4. Adicionar a coluna de quantidade vendida
5. Remover do dataset os produtos repetidos
5. Extrair apenas as colunas "Produto", "Valor Unitário" e "Quantidade". '''

import pandas as pd

vendas_df = pd.read_excel("produtos.xlsx")

vendas_df.rename(columns={'Quantidade': 'Quantidade no Estoque'}, inplace=True)

vendas_df['Quantidade no Estoque'] += 10
vendas_df.loc[:, "Preço de Venda"] = vendas_df['Valor Unitário'] * 1.20
vendas_df.loc[:, "Quantidade Vendida"] = 0
materiais_df_sem_duplicatas = vendas_df.drop_duplicates(subset=['Produto'])

produtos = materiais_df_sem_duplicatas[['Produto', 'Valor Unitário', 'Preço de Venda', 'Quantidade no Estoque', 'Quantidade Vendida']]

novo_arquivo = "produtos_precos.xlsx"
produtos.to_excel(novo_arquivo, index=False)