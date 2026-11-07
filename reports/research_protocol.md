# Plano da pesquisa

**Disciplina:** Machine Learning (AV2)  
**Equipe:** dois estudantes de Análise e Desenvolvimento de Sistemas

## Pergunta principal da AV2 v1.0

**Existe relação entre a quantidade de regras estaduais sobre armas registradas na RAND e a taxa de homicídios nos estados americanos?**

A hipótese inicial é que estados com mais registros de regras podem ter taxas diferentes dos estados com menos registros. Contamos os `Law ID` da RAND marcados como `Implement` ou `Modify` vigentes em **31 de dezembro** de cada ano, separando `Restrictive` e `Permissive`. A unidade é registro da RAND, não lei aprovada distinta. O desfecho é a **taxa de homicídios por 100 mil habitantes**, e não o total de crimes. A análise dessa relação fica para a próxima etapa. Mesmo que exista associação, ela não demonstra que as leis causaram a diferença.

## Experimento anterior: previsão

**Informações sobre as leis de armas ajudam a prever a taxa de homicídios do ano seguinte nos estados americanos?**

Escolhemos o tema para praticar o que aprendemos sobre **aprendizado supervisionado**: damos exemplos com informações de um ano e ensinamos o programa a tentar prever um valor do ano seguinte.

Não estamos tentando descobrir qual lei é melhor ou pior, nem provar que determinada lei causa homicídios.

## Como pensamos em testar

Comparamos três opções:

- **Previsão simples:** repetir a taxa de homicídios do ano anterior.
- **Modelo A:** usar a taxa anterior, o desemprego e a renda por pessoa.
- **Modelo B:** usar as informações do A e acrescentar dados sobre leis de porte de armas e verificação de antecedentes em vendas privadas.

Nossa ideia inicial era que o Modelo B **poderia** prever melhor. Tratamos isso como uma pergunta, não como uma resposta pronta.

## De onde vieram os dados?

| Fonte | Informação usada |
| --- | --- |
| CDC | Taxa de homicídios por 100 mil habitantes. |
| RAND | Algumas regras estaduais sobre porte de armas e verificação de antecedentes. |
| BLS | Taxa de desemprego. |
| BEA | Renda pessoal média por habitante. |

Trabalhamos com os 50 estados americanos. As informações de entrada vão de 2019 a 2023, e as taxas que tentamos prever vão de 2020 a 2024. Ao tirar o último ano sem resposta futura, ficamos com 250 exemplos.

## Como treinamos e testamos

Usamos **regressão linear**, um método que tenta combinar os valores de entrada para chegar a uma previsão. Antes, o `StandardScaler` coloca as variáveis em escalas comparáveis. Os dois modelos usam o mesmo método para que a comparação seja justa.

Testamos três vezes. Em cada teste, o programa aprendeu com os anos anteriores:

| Ano que queríamos prever | Anos usados para treinar (informações de entrada) |
| --- | --- |
| 2022 | 2019 e 2020 |
| 2023 | 2019 a 2021 |
| 2024 | 2019 a 2022 |

Esse modo de aumentar aos poucos os anos de treino se chama **janela expansiva**: a quantidade de dados para aprender cresce a cada rodada. Os dados não foram embaralhados.

Medimos os erros com MAE (erro médio) e RMSE (que pesa mais os erros grandes). Quanto menor, melhor.

## Cuidados

As taxas são de **homicídios totais**, não só os cometidos com armas de fogo. As categorias da RAND representam apenas algumas regras estaduais. Além disso, dados históricos podem ser atualizados depois do período que representam. Usar os dados mais antigos para prever os mais recentes ajuda, mas não resolve todas essas limitações.

O plano inicial citava a possibilidade de usar Random Forest, mas **não fizemos esse teste**. O que temos executado e documentado é regressão linear e previsão simples.

## Onde chegamos?

A previsão simples teve menor erro médio nas três rodadas: MAE de 0,785, contra 0,944 no Modelo A e 0,959 no B. Então **não encontramos uma melhoria constante ao acrescentar as informações sobre leis**. É um resultado do nosso trabalho, não uma confirmação de que as leis não têm efeito.

Os números completos estão em [resultados](experiment_results.md). O que ainda falta está em [próximos passos](next_steps.md).


## Organização do experimento anterior (02/11/2026)

A preparação do primeiro experimento usava seis notebooks sequenciais e regressão linear. Para a pergunta principal atual, o fluxo é **01 → 02 → 05**. O notebook 05 agora gera a base de associação, e a V3 supervisionada permanece como artefato histórico do experimento anterior. Veja [COMECAR_AQUI.md](../COMECAR_AQUI.md) para a ordem atual.

**Reprodutibilidade:** os blocos foram reorganizados para depender apenas dos arquivos de etapas anteriores, mas ainda é necessário conferir a execução completa com os dados originais. As métricas de referência no relatório não foram substituídas por resultados inventados.
