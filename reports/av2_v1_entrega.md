# AV2 — entrega da versão 1.0

1. **Datasets escolhidos:** [*Mapping Injury, Overdose, and Violence - State* (CDC)](https://data.cdc.gov/d/fpsi-y8tj), com taxas de homicídios por estado e ano; e [*State Firearm Law Database 6.0* (RAND)](https://www.rand.org/pubs/tools/TLA243-2-v4.html), com registros de regras estaduais sobre armas. Vamos estudar os 50 estados americanos no período de 2019 a 2024.
2. **Hipótese/pergunta:** existe relação entre a quantidade de regras estaduais sobre armas registradas na RAND e a taxa de homicídios nos estados americanos? Nossa hipótese inicial é que estados com mais regras registradas podem ter taxas diferentes dos estados com menos regras. Ainda não sabemos se a diferença existe nem em qual direção.
3. **Colab:** [abrir o notebook da versão 1.0](https://colab.research.google.com/github/JanGustavo/us-gun-policy-ml/blob/main/notebooks/00_av2_v1_colab.ipynb). Ele abre as duas bases com Pandas e mostra as primeiras linhas. No Colab, clique em **Executar tudo**.

**O que queremos medir:** a taxa de homicídios por 100 mil habitantes, não o total de crimes. Na próxima etapa, será necessário definir quais regras entram na contagem e conferir o período em que cada uma estava vigente. Uma relação observada entre os dados não prova que as leis causaram aumento ou redução de homicídios.

**Fonte:** mantivemos o tema e as bases dos EUA do projeto. Elas não vêm do dados.gov.br, portal indicado no roteiro da atividade.
