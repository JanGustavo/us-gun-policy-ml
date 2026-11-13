# Resultados dos nossos testes

> **Arquivo histórico:** estes resultados pertencem à pergunta anterior sobre previsão da taxa de homicídios do ano seguinte. Eles não testam a pergunta principal atual da AV2 sobre a relação entre a contagem de regras RAND e a taxa de homicídios do ano seguinte.

## O que queríamos descobrir?

Queríamos comparar previsões de homicídios feitas **com e sem informações sobre leis de armas**. Antes de comparar, também testamos uma opção bem simples: usar a taxa do ano anterior como previsão.

Usamos a mesma base de 50 estados e os mesmos anos de teste para os modelos A e B. O programa tentou prever as taxas de 2022, 2023 e 2024.

## Como ler os números

- **MAE:** quanto a previsão erra, em média. Por exemplo, MAE 1 significa erro médio de 1 homicídio por 100 mil habitantes.
- **RMSE:** outra forma de calcular o erro, que dá mais importância às previsões que erraram muito.
- **Quanto menor o resultado, melhor foi a previsão.**

## Resultados por ano

| Ano previsto | Modelo | MAE | RMSE |
| --- | --- | ---: | ---: |
| 2022 | Simples (repetir ano anterior) | **0,808** | **1,126** |
| 2022 | A | 1,330 | 1,763 |
| 2022 | B | 1,380 | 1,822 |
| 2023 | Simples (repetir ano anterior) | **0,710** | **0,884** |
| 2023 | A | 0,826 | 1,001 |
| 2023 | B | 0,832 | 0,979 |
| 2024 | Simples (repetir ano anterior) | 0,838 | 1,072 |
| 2024 | A | 0,677 | **0,953** |
| 2024 | B | **0,664** | 0,988 |

## Média dos três testes

| Modelo | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Simples | **0,785** | **1,027** |
| A: com dados econômicos | 0,944 | 1,239 |
| B: com dados econômicos e leis | 0,959 | 1,263 |

O RMSE médio desta tabela é a média dos três valores anuais, não um cálculo único com todas as previsões juntas.

## O que aprendemos?

O Modelo B teve resultados um pouco melhores em alguns casos, mas também errou mais em outros. Em 2024, por exemplo, B teve erro absoluto menor em 24 estados e maior em 26. Olhar só para o ano de 2024 poderia dar a impressão de que acrescentar as leis foi vantajoso, mas **isso não aconteceu de forma constante nos três anos**.

A descoberta que mais chamou nossa atenção foi que **a previsão simples teve os menores erros médios**. Isso mostra que um modelo com mais informações nem sempre prevê melhor.

## Por que ainda não podemos afirmar muita coisa?

Usamos apenas três anos de teste, com os mesmos estados aparecendo várias vezes. Homicídios também dependem de fatores que não estão na nossa tabela. Os valores das fontes são históricos e podem ter sido atualizados. Além disso, algumas leis mudaram durante o ano, e nossa tabela não diferencia quantos meses cada regra esteve em vigor.

Não podemos dizer que uma lei aumenta ou diminui homicídios só porque uma variável ajudou ou não ajudou a prever um valor. **Previsão não é a mesma coisa que causa.**

## Conclusão até o momento

**Nos testes que fizemos, acrescentar informações sobre as leis não melhorou de maneira constante as previsões de homicídios.** A forma mais simples de prever apresentou o menor erro médio nas três rodadas.

Isso responde à pergunta sobre **nosso modelo e nossos dados**, mas não resolve o debate sobre os efeitos reais das leis. O caminho agora é conferir a organização dos dados, explicar as limitações e apresentar com clareza o que aprendemos.

Os valores usados nesta seção estão preservados em `reports/results/temporal_validation.csv` e `model_comparison_summary.csv`.
