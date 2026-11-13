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
- [x] Semana 2: execução repetida em ambiente limpo, com os mesmos coeficientes. Faltava `openpyxl` no `requirements.txt`.
- [x] Semana 2: revisão das datas de vigência e da contagem RAND (notebook 07).
- [x] Semana 2: gráficos por estado e ano (notebook 08) e [relatório](semana2_relatorio.md) com método, resultado e limitações.

## Próximos passos

1. Baixar de novo os brutos do BLS e do BEA em uma máquina nova e rodar o 03 e o 04 pelo caminho "bruto". Na semana 2 eles rodaram a partir dos CSVs processados.
2. Testar um tipo de regra por vez (por exemplo, só checagem de antecedentes ou só porte velado), decidindo antes quais tipos olhar para não escolher só o que der resultado.
3. Trocar a taxa de homicídios totais pela de homicídios por arma de fogo, se o CDC tiver a série por estado.
4. Avaliar um período mais longo. A RAND vai de 1979 a 2025, então o limite é o dado de homicídios.
5. Montar os slides da apresentação a partir do relatório da semana 2.

O experimento antigo de previsão está preservado em `notebooks/arquivo/06_previsao_anterior.ipynb` e `reports/experiment_results.md`.
