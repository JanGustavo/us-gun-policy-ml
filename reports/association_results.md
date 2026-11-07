# Análise inicial da relação entre regras e homicídios

**Pergunta:** registros de regras estaduais sobre armas da RAND têm relação com a taxa de homicídios dos estados americanos?

## Dados e comparação

Usamos 50 estados em 2019–2024. A base integrada contém 300 linhas e 15 colunas, com CDC (homicídios totais), RAND (registros de regras), BLS (desemprego) e BEA (renda por pessoa). A contagem é de registros `Implement`/`Modify` vigentes em 31 de dezembro, separados entre restritivos e permissivos; não equivale ao número de leis aprovadas.

O modelo relaciona as contagens no fim de um ano à taxa de homicídios do ano seguinte (2020–2024; 250 observações). Inclui desemprego e renda do ano anterior e diferenças fixas de estado e ano. Assim, a comparação usa principalmente mudanças dentro do mesmo estado ao longo do tempo, em vez de comparar diretamente estados muito diferentes. Os erros são agrupados por estado.

## Resultado executado com os arquivos locais

| Contagem no fim do ano anterior | Coeficiente estimado | Intervalo de 95% |
| --- | ---: | ---: |
| Registros restritivos | 0,071 | -0,072 a 0,213 |
| Registros permissivos | -0,251 | -0,904 a 0,403 |

A unidade do coeficiente é ponto da taxa de homicídios por 100 mil habitantes para um registro adicional, mantidas as demais variáveis do modelo. **Os dois intervalos incluem zero.** Nesta análise, não há direção clara de associação para nenhuma das duas contagens. O resultado pode mudar após revisão das fontes, da definição das regras e do período.

## Limitações

- A RAND registra regras de tipos e intensidades diferentes; um `Law ID` não é uma unidade jurídica ou política homogênea.
- A taxa do CDC inclui homicídios por todos os meios, não apenas por arma de fogo.
- Desemprego e renda não medem cultura, policiamento, composição demográfica ou outros fatores relevantes.
- Leis podem ser alteradas em resposta à violência; usar a contagem do ano anterior melhora a ordem temporal, mas não elimina essa possibilidade.
- Há apenas seis anos e poucas mudanças em alguns tipos de regra. O modelo não identifica o efeito isolado de uma lei específica.

Por isso, o resultado **não responde se a legalização ou proibição de armas tem impacto direto, sim ou não**. Ele examina uma associação condicional com os dados disponíveis.
