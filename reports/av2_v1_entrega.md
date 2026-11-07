# AV2 — entrega da versão 1.0

1. **Dataset escolhido:** *Mapping Injury, Overdose, and Violence - State*, do CDC. Nesta etapa, usamos os registros de homicídios totais por estado e ano, de 2019 a 2024. [Página da base](https://data.cdc.gov/d/fpsi-y8tj).
2. **Hipótese/pergunta:** saber quais leis estaduais sobre porte de armas e verificação de antecedentes estavam em vigor ajuda a prever a **taxa de homicídios do ano seguinte** em cada estado americano? Nossa hipótese inicial é que essas informações podem melhorar a previsão em relação a usar apenas a taxa do ano anterior, o desemprego e a renda.
3. **Colab:** [abrir o notebook da versão 1.0](https://colab.research.google.com/github/JanGustavo/us-gun-policy-ml/blob/main/notebooks/00_av2_v1_colab.ipynb). O notebook lê a base pública com Pandas e mostra as primeiras linhas. Para visualizar os dados, basta clicar em **Executar tudo** no Colab.

**Escopo:** queremos prever uma **taxa por 100 mil habitantes**, e não o número absoluto de homicídios nem o total de crimes. O projeto não mede o efeito da “legalização das armas”: as leis analisadas são categorias específicas de porte e de verificação de antecedentes. Uma previsão melhor ou pior não demonstra que essas leis causaram aumento ou redução dos homicídios.

**Fonte:** vamos manter o tema e as bases dos EUA já usadas no projeto. O CDC não está no dados.gov.br, portal indicado no roteiro da atividade.
