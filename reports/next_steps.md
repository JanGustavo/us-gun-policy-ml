# Estado do projeto e próximos passos

## Pergunta principal atual

**Existe relação entre a quantidade de registros de regras estaduais sobre armas da RAND e a taxa de homicídios nos estados americanos?** A taxa é por 100 mil habitantes. O estudo usa 50 estados e os anos de 2019 a 2024.

## Já concluído

- [x] Fonte de homicídios do CDC identificada e CSV local disponível.
- [x] Planilha RAND 6.0 disponível em `reports/attachments/`.
- [x] Contagem reproduzível dos registros RAND vigentes em 31 de dezembro de cada ano, separada em restritivos e permissivos.
- [x] Integração CDC + RAND por estado e mesmo ano: 300 linhas e 7 colunas.
- [x] Testes de vigência e de perda de linhas na integração.
- [x] Notebook v1.0 no Colab que abre as duas fontes com Pandas.

## Próxima etapa

1. Executar o Colab e os notebooks 01 → 02 → 05 em um ambiente limpo.
2. Conferir a interpretação da contagem RAND e as datas de vigência, principalmente transições durante o ano.
3. Analisar a relação entre as contagens e a taxa de homicídios, separando registros restritivos e permissivos e observando que estados e anos podem diferir por outros motivos.
4. Preparar gráficos e apresentar resultados e limitações com nossas palavras.

Os notebooks 03, 04 e 06 e os resultados de previsão são **históricos**. Eles podem ajudar em análises complementares depois, mas não respondem à pergunta principal atual.
