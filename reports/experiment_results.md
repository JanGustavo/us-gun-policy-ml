# Resultados dos experimentos de Machine Learning

## 1. Objetivo

Avaliar se a inclusão de indicadores estaduais de legislação armamentista melhora a previsão da taxa de homicídios do ano seguinte nos Estados Unidos.

O estudo compara dois modelos de regressão linear e uma estratégia de previsão ingênua.

## 2. Base de dados

Foram utilizadas informações de quatro fontes:

- **CDC:** taxas anuais de homicídios.
- **RAND:** classificações estaduais de legislação armamentista.
- **BLS:** taxas anuais de desemprego.
- **BEA:** renda pessoal per capita.

O dataset supervisionado contém 250 observações, correspondentes aos 50 estados americanos, com variáveis de entrada de 2019 a 2023 e taxas de homicídios previstas de 2020 a 2024.

## 3. Modelos avaliados

**Modelo ingênuo:** utiliza a taxa de homicídios do ano anterior como previsão para o ano seguinte.

**Modelo A:** regressão linear utilizando taxa anterior de homicídios, desemprego e renda pessoal per capita.

**Modelo B:** utiliza as mesmas variáveis do Modelo A, acrescentando indicadores de porte de armas e de verificação de antecedentes em vendas privadas.

Os Modelos A e B foram implementados com `StandardScaler` e `LinearRegression`, utilizando um pipeline do scikit-learn.

## 4. Metodologia de avaliação

Foi utilizada uma validação temporal expansiva, com três rodadas:

| Ano previsto | Anos de entrada utilizados no treinamento | Observações de teste |
| --- | --- | ---: |
| 2022 | 2019–2020 | 50 |
| 2023 | 2019–2021 | 50 |
| 2024 | 2019–2022 | 50 |

As métricas adotadas foram o erro absoluto médio (MAE) e a raiz do erro quadrático médio (RMSE). Valores menores representam melhor desempenho.

## 5. Resultados

| Ano previsto | Modelo | MAE | RMSE |
| --- | --- | ---: | ---: |
| 2022 | Ingênuo | 0,808 | 1,126 |
| 2022 | Modelo A | 1,330 | 1,763 |
| 2022 | Modelo B | 1,380 | 1,822 |
| 2023 | Ingênuo | 0,710 | 0,884 |
| 2023 | Modelo A | 0,826 | 1,001 |
| 2023 | Modelo B | 0,832 | 0,979 |
| 2024 | Ingênuo | 0,838 | 1,072 |
| 2024 | Modelo A | 0,677 | 0,953 |
| 2024 | Modelo B | 0,664 | 0,988 |

### Médias das três rodadas

| Modelo | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Ingênuo | 0,785 | 1,027 |
| Modelo A | 0,944 | 1,239 |
| Modelo B | 0,959 | 1,263 |

O RMSE médio corresponde à média dos RMSEs das três rodadas, não ao RMSE global calculado sobre todas as previsões.

## 6. Discussão

Em 2022 e 2023, o modelo ingênuo apresentou menores erros absolutos médios que os modelos de regressão. Em 2024, os modelos A e B superaram a previsão ingênua.

A inclusão de indicadores legislativos não apresentou melhoria consistente. O Modelo B obteve MAE ligeiramente menor em 2024, mas seus erros médios foram superiores aos do Modelo A na avaliação consolidada.

Esses resultados indicam que acrescentar variáveis não garante maior capacidade preditiva.

## 7. Limitações

O estudo utiliza apenas três anos de avaliação temporal e observa repetidamente os mesmos 50 estados.

As variáveis legislativas representam classificações anuais, não necessariamente a exposição durante todos os meses do ano.

A renda per capita foi utilizada em dólares correntes, sem ajuste pela inflação.

As bases históricas podem conter revisões posteriores às datas dos eventos, portanto o experimento é retrospectivo e não representa integralmente previsões realizadas com informações disponíveis em tempo real.

A regressão linear também não contempla todas as possíveis relações não lineares, interações entre variáveis ou fatores não observados.

## 8. Conclusão preliminar

Nos experimentos realizados, a inclusão de indicadores de legislação armamentista não apresentou ganho preditivo consistente em relação ao modelo de referência.

A previsão ingênua obteve o menor erro médio nas três rodadas avaliadas.

Os resultados não permitem estabelecer relações causais entre legislação armamentista e homicídios, nem comprovar a ausência dessas relações. A interpretação fica restrita ao desempenho preditivo observado nos modelos e períodos analisados.
