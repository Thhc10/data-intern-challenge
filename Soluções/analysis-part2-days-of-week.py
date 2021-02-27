# Analisando a relação entre todas as transações e apenas as fraudulentes referente aos dias da semana

import pandas as pd
import datetime
import calendar


# Encontra o dia da semana referente a data informada
def find_day_of_week(date, date_type):
    if date_type == 'week':
        date = datetime.datetime.strptime(date, '%d/%m/%Y').weekday()
        return calendar.day_name[date]


# Adiciona uma coluna com os dias da semana, referente a columa com a data informada
def add_day_of_week(df, date):
    for i in range(len(df)):
        week_day = find_day_of_week(df[date][i], 'week')
        df.loc[i, 'week_day'] = week_day
    return None


dataset_cards = pd.read_csv('../Datasets/dataset-cards.csv', sep=';')
dataset_customers = pd.read_csv('../Datasets/dataset-customers.csv', sep=';')
dataset_frauds = pd.read_csv('../Datasets/dataset-frauds.csv', sep=';')
dataset_transactions = pd.read_csv('../Datasets/dataset-transactions.csv', sep=';')

transactions_with_frauds = pd.merge(dataset_transactions, dataset_frauds, left_on='id', right_on='transaction_id')
add_day_of_week(transactions_with_frauds, 'transaction_date')
add_day_of_week(dataset_transactions, 'transaction_date')

week_day_transaction_fraud = transactions_with_frauds['week_day'].value_counts(normalize=True) * 100
week_day_all_transactions = dataset_transactions['week_day'].value_counts(normalize=True) * 100

print(week_day_transaction_fraud)
print(week_day_all_transactions)
