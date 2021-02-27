# Analisando a relação entre todas as transações e apenas as fraudulentes referente ao 'vintage_group'

import pandas as pd

dataset_cards = pd.read_csv('../Datasets/dataset-cards.csv', sep=';')
dataset_customers = pd.read_csv('../Datasets/dataset-customers.csv', sep=';')
dataset_frauds = pd.read_csv('../Datasets/dataset-frauds.csv', sep=';')
dataset_transactions = pd.read_csv('../Datasets/dataset-transactions.csv', sep=';')

transactions_with_frauds = pd.merge(dataset_transactions, dataset_frauds, left_on='id', right_on='transaction_id')
customers_and_cards = pd.merge(dataset_customers, dataset_cards, left_on='id', right_on='customer_id')

# Junção das tabelas: transactions, frauds e cards
features_transactions_frauds = pd.merge(customers_and_cards, transactions_with_frauds, on='card_number')
# Junção das tabelas: transactions, customers e cards
features_transactions = pd.merge(customers_and_cards, dataset_transactions, on='card_number')

# Agrupando as transações por Vintage Group e comparando o percentual de todas as transações e apenas as transações
# fraudadas, de modo a encontrar relação entre Vintage Group e transações com fraudes.
frauds_grouped_by_vintage_group = features_transactions_frauds['vintage_group'].value_counts(normalize=True) * 100
all_transaction_grouped_by_vintage_group = features_transactions['vintage_group'].value_counts(normalize=True) * 100

print("Relação entre 'vintage_group' e todas as transações")
print(all_transaction_grouped_by_vintage_group)

print("\nRelação entre 'vintage_group' e transações com fraudes")
print(frauds_grouped_by_vintage_group)
