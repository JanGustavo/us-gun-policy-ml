# Continuidade da pesquisa · 02/11/2026

## O problema atual

O ganho preditivo com indicadores de legislação não se sustentou nas três rodadas temporais. MAE médio: persistência **0,785**, Modelo A **0,944**, Modelo B **0,959**. Isso não é falha de código nem prova de ausência de efeitos jurídicos: é uma limitação do poder preditivo dos modelos testados e do horizonte de avaliação.

## Roteiro de trabalho, em ordem

- [ ] **P0 Reprodutibilidade:** executar notebooks em kernels limpos, mover a leitura BLS e BEA para etapas independentes, registrar versões das fontes e checksums. Atualmente o 03 depende do 05 no meio do fluxo.
- [ ] **P0 Testes:** assegurar 50 estados × seis anos em cada fonte, chaves sem duplicação, valores válidos, deslocamento correto do alvo e comparação dos nove resultados versionados.
- [x] **Auditoria parcial CCW:** conferir seis transições may-issue para shall-issue em 2022 e 12 transições para permitless entre 2021 e 2023 com os registros RAND.
- [ ] **P1 Auditoria RAND:** examinar dias/meses, revogações, datas de substituição, regras multicategoria (incluindo Louisiana 2024), categorias de antecedentes e duração de exposição. Qualquer correção cria V4 e novo experimento identificado.
- [ ] **P2 Robustez pré-definida:** investigar influência de outliers, heterogeneidade entre estados, choques de pandemia, renda nominal, diferentes cortes de treino e dependência temporal. Não selecionar algoritmos conforme resultado desejado.
- [ ] **P3 Divulgação acadêmica:** visualizações por rodada, resultados favoráveis e desfavoráveis, distinção de predição e causalidade, referências e apresentação para dois estudantes.

## Critérios de avanço

O pipeline precisa executar desde os arquivos originais, sem depender de variáveis antigas do Jupyter. Resultados devem ser comparados com `reports/results/temporal_validation.csv` e `model_comparison_summary.csv`. Hipóteses e escolhas exploratórias posteriores devem ser declaradas e não confundidas com a avaliação inicial.
