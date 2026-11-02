# US Gun Policy ML

**Trabalho de Machine Learning (AV2), desenvolvido por dois estudantes de Análise e Desenvolvimento de Sistemas.**

A pergunta que orientou o projeto foi simples: **usar informações sobre leis de armas ajuda a prever a taxa de homicídios do ano seguinte nos estados dos EUA?** Não estamos tentando provar que uma lei causa mais ou menos homicídios. Nosso foco é comparar previsões.

## O que já fizemos

1. Reunimos dados de quatro fontes: CDC (homicídios), RAND (leis sobre armas), BLS (desemprego) e BEA (renda por pessoa).
2. Organizamos dados de 50 estados entre 2019 e 2024.
3. Criamos uma tabela para prever **a taxa de homicídios do ano seguinte**. Ela tem 250 linhas e 13 colunas.
4. Comparamos três formas de prever: repetir a taxa do ano anterior, usar uma regressão linear com dados econômicos (Modelo A) e acrescentar informações sobre as leis (Modelo B).
5. Testamos as previsões para 2022, 2023 e 2024, sempre treinando com anos anteriores.

## O que encontramos

O **MAE** mostra, em média, o quanto o modelo errou na taxa de homicídios por 100 mil habitantes. Quanto menor, melhor. O **RMSE** é outra medida de erro que dá mais peso aos erros grandes.

| Forma de prever | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Repetir a taxa do ano anterior | **0,785** | **1,027** |
| Modelo A: taxa anterior, desemprego e renda | 0,944 | 1,239 |
| Modelo B: Modelo A + informações sobre leis | 0,959 | 1,263 |

A forma mais simples teve os menores erros médios. **Adicionar informações sobre as leis não melhorou os resultados de forma constante**. Em 2024, por exemplo, o Modelo B acertou um pouco mais pelo MAE, mas isso não se repetiu nos outros anos.

Isso não significa que as leis não tenham efeitos. Significa apenas que **não conseguimos melhorar a previsão com essas informações no modelo que testamos**.

## Por que paramos nesse ponto?

Não é porque o código deixou de funcionar. O resultado do teste foi diferente do que poderíamos esperar: acrescentar dados não garantiu uma previsão melhor. Temos poucos anos para testar, e homicídios dependem de muitos fatores que nossa tabela não inclui. Seria errado ficar trocando os algoritmos só até encontrar o resultado que gostaríamos.

## Como o projeto está organizado

| Arquivo | O que fazemos nele |
| --- | --- |
| [01_eda.ipynb](notebooks/01_eda.ipynb) | Baixamos e observamos os dados de homicídios. |
| [02_rand_inspection.ipynb](notebooks/02_rand_inspection.ipynb) | Organizamos as informações das leis. |
| [03_data_integration.ipynb](notebooks/03_data_integration.ipynb) | Juntamos as fontes em uma tabela. |
| [05_bea_inspection.ipynb](notebooks/05_bea_inspection.ipynb) | Preparamos os dados de renda. |
| [06_model_comparison.ipynb](notebooks/06_model_comparison.ipynb) | Treinamos, fazemos previsões e comparamos erros. |

O número 04 foi reservado durante as explorações; não existe um notebook 04 versionado no repositório.

## Para executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Os notebooks foram escritos para trabalhar a partir da pasta `notebooks/`. **Os arquivos de dados brutos e processados não estão no Git**, por isso baixar apenas o repositório não é suficiente para executar tudo.

Fontes utilizadas: [CDC](https://data.cdc.gov/d/fpsi-y8tj), [RAND](https://www.rand.org/pubs/tools/TLA243-2.html), [BLS](https://www.bls.gov/lau/tables.htm) e [BEA](https://apps.bea.gov/itable/?ReqID=70&step=1). A planilha RAND está em `reports/attachments/`; para as outras fontes, os notebooks esperam arquivos em `data/raw/`.

**Ordem de execução atual:** 01, 02, 03 até a tabela V2, 05, voltar ao 03 para criar a V3 e, por último, 06. Ainda queremos simplificar essa sequência.

## O que falta fazer

- Conferir se todos os notebooks executam do começo ao fim sem depender de variáveis salvas na memória.
- Conferir com mais cuidado a data de início e fim de algumas leis.
- Fazer gráficos claros para a apresentação e explicar os erros dos modelos.
- Organizar uma conclusão com os resultados reais, mesmo que diferentes da hipótese inicial.

**Documentos:** [pergunta e plano da pesquisa](reports/research_protocol.md), [explicação das colunas](reports/data_dictionary.md), [resultados completos](reports/experiment_results.md) e [próximos passos](reports/next_steps.md).
