# Autor: Thiago Henrique da Costa
# Data Intern Challenge

import pandas as pd
import numpy as np

dataset_cards = pd.read_csv('../Datasets/dataset-cards.csv', sep=';')
dataset_customers = pd.read_csv('../Datasets/dataset-customers.csv', sep=';')
dataset_frauds = pd.read_csv('../Datasets/dataset-frauds.csv', sep=';')
dataset_transactions = pd.read_csv('../Datasets/dataset-transactions.csv', sep=';')

# Encontrando a idade média dos clientes
average_age = dataset_customers['age'].mean()
print('A idade média dos consumidores é de {:.1f} anos.\n'.format(average_age))

# Para analisar como que 'card_family' é baseado no 'credit_limit, realizei um agrupamento pelo 'card_family'
# e verificando assim quais eram seus respectivos limites máximos e mínimos. Equivalente ao GROUP BY do SQL.
cards_grouped_by_family = dataset_cards.groupby("card_family").agg({"credit_limit": [np.min, np.max]})
print(cards_grouped_by_family)

# Para descobrir quais eram os IDs das transações fraudadas com o maior valor, realizei uma junção de tabelas entre
# todas as transações e as transações fraudados por meio do 'transaction_id'. Dessa forma, foi possível encontrar
# quais eram os IDs que satisfazessem a proposição. Equivalente ao INNER JOIN do SQL.
transaction_ids = dataset_frauds['transaction_id']
ids_with_highest_transaction = []
joined_table = pd.merge(dataset_transactions, dataset_frauds, left_on='id', right_on='transaction_id')
transaction_with_frauds = joined_table[['id', 'value']]
value_highest_transaction = transaction_with_frauds['value'].max()

for i in range(len(transaction_with_frauds)):
    if transaction_with_frauds['value'][i] == value_highest_transaction:
        ids_with_highest_transaction.append(transaction_with_frauds['id'][i])

print('\nDentre as transações fraudadas, as que tiveram o maior valor foram: {} e seu valor associado foi de {}.'
      .format(ids_with_highest_transaction, value_highest_transaction))
