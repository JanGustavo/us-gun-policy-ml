# Estado do projeto e próximos passos

## Pergunta principal

**Os registros de regras estaduais sobre armas da RAND têm relação com a taxa de homicídios nos estados americanos?** A taxa é por 100 mil habitantes. Usamos 50 estados e os anos 2019–2024.

## Concluído

- [x] Fontes CDC, RAND, BLS e BEA preparadas localmente.
- [x] Contagem reproduzível dos registros RAND vigentes em 31 de dezembro, separando restritivos e permissivos.
- [x] Painel integrado por estado e ano: 300 linhas e 15 colunas.
- [x] Modelo inicial que usa regras e economia do ano anterior e considera diferenças fixas entre estados e anos.
- [x] Testes de datas, cobertura da integração e ordem temporal do modelo.
- [x] Notebook v1.0 no Colab que abre CDC e RAND com Pandas.

## Próximos passos

1. Executar 01 → 06 em um ambiente limpo. Os arquivos brutos BLS/BEA existem nesta máquina, mas não estão no Git e precisam ser baixados em uma cópia nova do repositório.
2. Conferir datas de vigência da RAND, especialmente leis que mudaram no meio do ano.
3. Avaliar se a contagem de registros é uma boa medida para a pergunta. Regras de tipos diferentes não têm a mesma intensidade.
4. Explorar comparações mais específicas, como uma categoria de regra ou mudanças em um subconjunto de estados, sem escolher apenas resultados favoráveis.
5. Preparar gráficos e uma apresentação que explique as limitações. A análise atual não permite responder “impacto direto: sim ou não”.

O experimento antigo de previsão está preservado em `notebooks/arquivo/06_previsao_anterior.ipynb` e `reports/experiment_results.md`.
