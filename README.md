# US Gun Policy ML

Projeto de **dois estudantes de ADS**, desenvolvido para estudar dados públicos sobre armas e homicídios nos estados americanos. A pergunta principal da AV2 é: **existe relação entre a quantidade de regras estaduais sobre armas registradas na RAND e a taxa de homicídios?** A contagem das regras está no notebook 02 e a análise no 06. A revisão e os gráficos da semana 2 estão no [relatório da semana 2](reports/semana2_relatorio.md).

A comparação de modelos de previsão descrita abaixo é um experimento anterior do projeto. Seus resultados não respondem, por si só, à nova pergunta principal.

## <a href="COMECAR_AQUI.md">▶ Comece por aqui: fluxo atual e resultados esperados</a>

Para a pergunta atual, execute **01 CDC → 02 RAND → 03 desemprego → 04 renda → 05 integração → 06 análise → 07 revisão da RAND → 08 gráficos**. O guia mostra como abrir o JupyterLab e o que conferir em cada etapa. O notebook antigo de previsão está guardado em `notebooks/arquivo/`.

## O que já fizemos

Usamos dados públicos de 50 estados dos EUA, entre 2019 e 2024: CDC (homicídios totais), RAND (registros de regras estaduais sobre armas), BLS (desemprego) e BEA (renda por pessoa). A base integrada tem **300 registros e 15 colunas**, um por estado e ano. A análise inicial relaciona as regras do fim de um ano à taxa de homicídios do ano seguinte, considerando desemprego, renda, estado e ano.

Os intervalos estimados para os registros restritivos e permissivos incluem zero. Portanto, **a análise atual não indica uma direção clara de associação** e não permite afirmar que as regras tiveram impacto direto. Veja [os resultados da pergunta atual](reports/association_results.md).

## Resultado do experimento anterior de previsão

O **MAE** é uma medida de erro médio da previsão; o **RMSE** dá mais peso aos erros grandes. Quanto menor, melhor.

| Forma de prever | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Simples: repetir a taxa anterior | **0,785** | **1,027** |
| Modelo A: homicídios anteriores + economia | 0,944 | 1,239 |
| Modelo B: Modelo A + informações sobre leis | 0,959 | 1,263 |

A previsão simples teve o menor erro médio dos três testes realizados (para 2022, 2023 e 2024). **Incluir informações sobre leis não melhorou as previsões de maneira constante.** Isso não prova que as leis não tenham efeitos, pois estamos estudando previsão, não causa e efeito.

## O que falta para a pergunta atual

Na semana 2 repetimos a execução em um ambiente limpo, conferimos as datas de vigência da RAND e fizemos os gráficos. O resultado continuou inconclusivo. Falta olhar um tipo de regra por vez e montar a apresentação. A contagem é de **registros RAND vigentes em 31 de dezembro**, não de leis aprovadas distintas. Não vamos interpretar uma associação como prova de causa e efeito.

## Arquivos principais

- [COMEÇAR AQUI](COMECAR_AQUI.md): **instruções do fluxo principal e do material histórico**.
- [notebooks/](notebooks/): 01 a 08 formam o fluxo atual; `arquivo/` guarda o notebook anterior de previsão.
- [Relatório da semana 2](reports/semana2_relatorio.md): revisão dos dados, gráficos, resultado e limitações.
- [Plano da pesquisa](reports/research_protocol.md): pergunta e método.
- [Dicionário de dados](reports/data_dictionary.md): significado das colunas.
- [Resultados completos](reports/experiment_results.md): tabelas e conclusão.
- [Próximos passos](reports/next_steps.md): o que falta.

As pastas `data/raw/` e `data/processed/` não são enviadas ao Git. O guia mostra quais arquivos precisam estar disponíveis antes de executar. Os resultados anteriores estão preservados em `reports/results/`; ao executar o notebook 06, os arquivos desses resultados são atualizados localmente.
