# AV2 — entrega da versão 1.0

1. **Datasets escolhidos:** [*Mapping Injury, Overdose, and Violence - State* (CDC)](https://data.cdc.gov/d/fpsi-y8tj), com taxas de homicídios totais por estado e ano; e [*State Firearm Law Database 6.0* (RAND)](https://www.rand.org/pubs/tools/TLA243-2-v4.html), com registros de regras estaduais sobre armas. Vamos estudar os 50 estados americanos no período de 2019 a 2024.
2. **Hipótese/pergunta:** existe relação entre a quantidade de registros de regras estaduais sobre armas da RAND e a taxa de homicídios nos estados americanos? Nossa hipótese inicial é que estados com mais registros podem ter taxas diferentes dos estados com menos registros. Ainda não sabemos se a diferença existe nem em qual direção.
3. **Colab:** [abrir o notebook da versão 1.0](https://colab.research.google.com/github/JanGustavo/us-gun-policy-ml/blob/main/notebooks/00_av2_v1_colab.ipynb). Ele abre as duas bases com Pandas e mostra as primeiras linhas. No Colab, clique em **Executar tudo**.

No desenvolvimento do projeto, também usamos desemprego do BLS e renda por pessoa do BEA para tornar a comparação entre estados e anos mais cuidadosa. A entrega inicial no Colab abre as duas bases centrais, CDC e RAND.

**O que queremos medir:** a taxa de homicídios por 100 mil habitantes, não o total de crimes. Para a contagem, usamos os registros `Implement` e `Modify` da RAND vigentes em 31 de dezembro de cada ano. Cada registro pode representar uma regra ou alteração, não necessariamente uma lei distinta. Separamos os registros restritivos dos permissivos. Uma relação observada entre os dados não prova que as leis causaram aumento ou redução de homicídios.

**Fonte:** mantivemos o tema e as bases dos EUA do projeto. Elas não vêm do dados.gov.br, portal indicado no roteiro da atividade.

Dupla: Janderson Gustavo Alves da Silva - 03355736
Dupla: Lucas Paulino Da Silva - 03355947
