# US Gun Policy ML

Projeto de **dois estudantes de ADS**, desenvolvido para praticar conceitos básicos de Machine Learning. Nossa pergunta é: **informações sobre as leis de armas ajudam a prever a taxa de homicídios do ano seguinte nos estados americanos?**

## <a href="COMECAR_AQUI.md">▶ Comece por aqui: comandos, seis notebooks e resultados esperados</a>

Você vai executar **seis notebooks em ordem, com três blocos de código em cada um**: 01 CDC, 02 RAND, 03 desemprego, 04 renda, 05 integração e 06 modelos. O guia mostra como abrir o JupyterLab e explica o que conferir depois de cada etapa.

## O que já fizemos

Usamos dados públicos de 50 estados dos EUA, entre 2019 e 2024: CDC (homicídios totais), RAND (algumas regras sobre porte e antecedentes), BLS (desemprego) e BEA (renda per capita). Juntamos as informações numa base com **250 registros e 13 colunas** e comparamos previsões do ano seguinte.

## O resultado até agora

O **MAE** é uma medida de erro médio da previsão; o **RMSE** dá mais peso aos erros grandes. Quanto menor, melhor.

| Forma de prever | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Simples: repetir a taxa anterior | **0,785** | **1,027** |
| Modelo A: homicídios anteriores + economia | 0,944 | 1,239 |
| Modelo B: Modelo A + informações sobre leis | 0,959 | 1,263 |

A previsão simples teve o menor erro médio dos três testes realizados (para 2022, 2023 e 2024). **Incluir informações sobre leis não melhorou as previsões de maneira constante.** Isso não prova que as leis não tenham efeitos, pois estamos estudando previsão, não causa e efeito.

## O que falta

Reexecutar e conferir tudo em um ambiente limpo, revisar alguns detalhes sobre as datas das leis e montar gráficos simples para a apresentação. O foco é **entender o que fizemos**, não aumentar a quantidade de algoritmos para encontrar um resultado específico.

## Arquivos principais

- [COMEÇAR AQUI](COMECAR_AQUI.md): **instruções de execução em sequência**.
- [notebooks/](notebooks/): os seis notebooks numerados de 01 a 06.
- [Plano da pesquisa](reports/research_protocol.md): pergunta e método.
- [Dicionário de dados](reports/data_dictionary.md): significado das colunas.
- [Resultados completos](reports/experiment_results.md): tabelas e conclusão.
- [Próximos passos](reports/next_steps.md): o que falta.

As pastas `data/raw/` e `data/processed/` não são enviadas ao Git. O guia mostra quais arquivos precisam estar disponíveis antes de executar. Os resultados anteriores estão preservados em `reports/results/`; ao executar o notebook 06, os arquivos desses resultados são atualizados localmente.
