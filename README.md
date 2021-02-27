# Data Intern Challenge

Para analisar e manipular os dados disponibilizados, utilizei a biblioteca Pandas do Python que fornece ferramentas úteis para análise de dados.

## Parte 1

O passo a passo de cada solução está no arquivo [analysis-part1.py](https://github.com/Thhc10/data-intern-challenge/blob/main/Soluções/analysis-part1.py).

Após analisar os dados, foi possível encontrar que a idade média dos consumidores é de 35.1 anos.

Tabela 1: Limites de crédito agrupado por Card Family                
|Card Family| Mínimo | Máximo |
| --------- |--------|--------|
|Gold       | 2000   | 50000  |
|Platinum   | 51000  | 200000 |
|Premium    | 108000 | 899000 |

Na tabela acima, é possível inferir que a continuidade entre os limites de crédito dos cartões Gold e Platinum, isto é, o próximo valor acima do máximo limite de crédito do cartão Gold será o limite mínimo de crédito do cartão Platinum. Além disso, não há essa continuidade para o cartão Premium.

Para descobrir quais eram os IDs das transações fraudadas com o maior valor, realizei uma junção entre as tabelas dataset-frauds.csv e dataset-transactions.csv. Desse modo, 
dentre as transações fraudadas, a que teve o maior valor foi a CTID20567160 e seu valor associado foi de 49155.

## Parte 2

Para analisar como as transações fraudulenas estão conectadas a outros dados disponíveis no dataset, utilizei a biblioteca Pandas do Python e após manipular os dados foram encontradas as seguintes relações:

Tabela 1: Transações agrupadas por Vintage Group
| Vintage Group | Todas Transações | Somente Fraudes |    %   |
| ------------- |------------------|-----------------|--------|
| VG1           | 44,6%            | 49,5%           | 4,9pp  |
| VG2           | 22,9%            | 25,7%           | 2,8pp  |
| VG3           | 32,5%            | 24,8%           | -7,7pp |

Gráfico 1: Relação entre Vintage Group e Transações

<img src="https://user-images.githubusercontent.com/39107746/109373026-5bbf8f00-788b-11eb-843d-539af00a8016.png" width="650">

Comparando todas as transações e apenas as transações fraudadas, podemos observar que ocorreu um aumento percentual das transações fraudulentes ante todas as transações nos grupos de usuário mais 'Premium'. Isso se evidencia que no VG1 que é o grupo mais 'Premium' disponível, ocorreu um aumento de 4,9 pontos percentuais.

Para visualizar detalhes da contrução do algoritmo, acesse: [analysis-part2-vintage-group.py](https://github.com/Thhc10/data-intern-challenge/blob/main/Solu%C3%A7%C3%B5es/analysis-part2-vintage-group.py)

Tabela 2: Transações agrupadas por Dias da Semana

| Dias da Semana | Todas Transações | Somente Fraudes |    %   |
| -------------- |------------------|-----------------|--------|
| Domingo        | 14,5%            | 14,7%           | 0,2pp  |
| Segunda-feira  | 13,9%            | 12,8%           | -1,1pp |
| Terça-feira    | 14,5%            |  9,2%           | -5,3pp |
| Quarta-feira   | 14,5%            | 15,6%           | 1,1pp  |
| Quinta-feira   | 13,9%            | 14,7%           | 0,8pp  |
| Sexta-feira    | 14,5%            | 14,7%           | 0,2pp  |
| Sábado         | 14,2%            | 18,3%           | 4,1pp  |

Gráfico 2: Relação entre Dias da Semana e Transações

<img src="https://user-images.githubusercontent.com/39107746/109373202-3e3ef500-788c-11eb-9a5e-3cddb650855d.png" width="750">

Comparando todas as transações e apenas as transações fraudadas, é possível verificar que ocorreu uma grande diferença relativo aos seguintes dias da semana: terça-feira e sábado. Dessa forma, a porcentagem de transações fraudadas no sábado subiu 4,1 pontos percentuais e na terça-feira diminuiu 5,3 pontos percentuais.

Sendo assim, é interessante investigar, principalmente, as transações referente ao Vintage Group: VG1 que ocorreram no sábado.

Para visualizar detalhes da contrução do algoritmo, acesse: [analysis-part2-days-of-week.py](https://github.com/Thhc10/data-intern-challenge/blob/main/Solu%C3%A7%C3%B5es/analysis-part2-days-of-week.py)

