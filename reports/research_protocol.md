# Protocolo de Pesquisa

**Projeto:** Legislação sobre armas de fogo e taxas de homicídios nos Estados Unidos  
**Disciplina:** Machine Learning (AV2)  
**Equipe:** 2 integrantes

## 1. Tema e pergunta de pesquisa

O projeto busca investigar a relação entre as legislações estaduais sobre armas de fogo e as taxas de homicídios nos Estados Unidos, utilizando técnicas de Machine Learning.

**Pergunta principal:**

A inclusão de informações sobre as leis de armas de fogo melhora a capacidade de prever as taxas de homicídios nos estados americanos?

A pesquisa não parte do pressuposto de que leis mais restritivas ou mais permissivas necessariamente aumentam ou reduzem a criminalidade.

## 2. Objetivo

Desenvolver e avaliar um modelo de Machine Learning capaz de prever a taxa anual de homicídios por 100 mil habitantes nos estados americanos.

Para isso, serão comparadas duas versões do modelo:

- **Modelo A:** utiliza dados históricos de homicídios e indicadores socioeconômicos.
- **Modelo B:** utiliza os mesmos dados, acrescentando informações sobre as leis estaduais de armas de fogo.

O objetivo é verificar se as variáveis legislativas ajudam a melhorar as previsões.

## 3. Hipóteses

- **H0:** adicionar informações sobre a legislação de armas não melhora a capacidade preditiva.
- **H1:** adicionar essas informações melhora a capacidade preditiva.

Independentemente do resultado, a pesquisa buscará apresentar os dados de forma imparcial.

## 4. Dados utilizados

A pesquisa utilizará dados públicos referentes aos 50 estados americanos, organizados por estado e ano.

**Fontes previstas:**

- **CDC:** informações sobre homicídios.
- **RAND Corporation:** histórico das legislações estaduais sobre armas de fogo.
- **US Census Bureau e outras fontes oficiais:** dados populacionais e socioeconômicos.

**Variáveis iniciais:**

| Variável | Descrição |
| --- | --- |
| Estado | Estado americano analisado |
| Ano | Ano de referência |
| Taxa de homicídios | Homicídios por 100 mil habitantes |
| Desemprego | Taxa de desemprego estadual |
| Renda | Indicador de renda da população |
| População | Quantidade de habitantes |
| Legislação | Características das leis de armas vigentes |

As variáveis legislativas específicas e o período histórico serão definidos após verificar a disponibilidade e a compatibilidade das bases.

A variável-alvo será a **taxa de homicídios do ano seguinte**, utilizando informações disponíveis em anos anteriores.

## 5. Metodologia

O desenvolvimento seguirá cinco etapas:

1. **Coleta:** obter os datasets das fontes selecionadas.
2. **Preparação:** organizar os dados, tratar valores ausentes e reunir as informações por estado e ano.
3. **Análise exploratória (EDA):** criar gráficos e identificar padrões, diferenças e possíveis relações entre as variáveis.
4. **Treinamento:** utilizar um algoritmo de regressão, inicialmente Random Forest, para realizar as previsões.
5. **Avaliação:** comparar as previsões dos modelos A e B com os valores reais.

Os dados serão divididos cronologicamente. Os anos mais antigos serão utilizados no treinamento, e os três últimos anos completos e compatíveis serão reservados para teste.

A métrica principal será o **MAE (Erro Absoluto Médio)**, que representa a diferença média entre as taxas previstas e observadas. Quanto menor o MAE, melhor o desempenho.

## 6. Cuidados para evitar resultados enviesados

Para preservar a confiabilidade do trabalho, adotaremos os seguintes critérios:

- Utilizar todos os 50 estados, desde que existam dados comparáveis.
- Não selecionar ou excluir estados com base no resultado esperado.
- Registrar problemas encontrados nos dados e justificar possíveis exclusões.
- Não utilizar informações futuras para realizar previsões de anos anteriores.
- Aplicar os mesmos critérios de avaliação aos dois modelos.
- Apresentar resultados favoráveis ou contrários às hipóteses iniciais.

**Limitação importante:** uma relação estatística ou uma melhora nas previsões não demonstra, isoladamente, que determinada legislação causou aumento ou redução dos homicídios.

## 7. Organização e entregas

| Data | Atividade |
| --- | --- |
| 06/11 | Definição do problema, hipóteses e coleta inicial |
| 13/11 | Limpeza dos dados, EDA e preparação para treinamento |
| 27/11 | Treinamento, avaliação e análise dos erros |
| 04/12 | Apresentação final |

**Divisão inicial da equipe:**

- **Integrante 1:** levantamento das fontes, coleta e organização dos dados.
- **Integrante 2:** análise exploratória, treinamento e avaliação dos modelos.

Ambos participarão da revisão dos resultados, documentação e apresentação.

## 8. Resultado esperado

Ao final, esperamos apresentar um modelo funcional capaz de estimar taxas de homicídios, acompanhado de gráficos, métricas de desempenho e uma comparação entre os modelos com e sem variáveis legislativas.

A conclusão será construída a partir dos resultados encontrados, sem assumir previamente que maior restrição ou maior liberdade de acesso às armas seja responsável por determinado nível de criminalidade.

## Registro da execução · 02/11/2026

O planejamento inicial citava Random Forest, mas a primeira rodada efetivamente realizada empregou **LinearRegression com StandardScaler**, além de previsão ingênua, e três janelas expansivas com alvos 2022, 2023 e 2024. Random Forest não foi executado e não deve ser descrito como resultado. Médias MAE: ingênuo 0,785, A 0,944, B 0,959. A inclusão da legislação não melhorou consistentemente as previsões no experimento realizado. Ver `reports/experiment_results.md`.
