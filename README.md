# US Gun Policy ML

Pesquisa acadêmica exploratória sobre a **previsão da taxa anual de homicídios totais** nos 50 estados americanos. Comparamos a previsão ingênua (repetir a taxa anterior), um modelo linear com histórico de homicídios e fatores econômicos (A), e o mesmo modelo acrescido de indicadores de legislação sobre armas (B). **Previsão não demonstra causalidade.**

## Status da pesquisa · 02/11/2026

Integração de quatro fontes concluída: CDC (homicídios totais), RAND (porte oculto e verificação de antecedentes em vendas privadas), BLS (desemprego) e BEA (renda pessoal per capita). Dataset V3: **250 registros × 13 colunas**, com entradas de 2019–2023 para prever alvos de 2020–2024.

### Resultado principal

Média das métricas nas três rodadas de teste, prevendo 2022, 2023 e 2024. Quanto menor, melhor; unidade: homicídios por 100 mil habitantes.

| Modelo | MAE médio | RMSE médio |
| --- | ---: | ---: |
| Ingênuo, repetir o ano anterior | **0,785** | **1,027** |
| A: taxa anterior, desemprego e renda | 0,944 | 1,239 |
| B: A + indicadores de legislação | 0,959 | 1,263 |

O modelo B **não melhorou consistentemente** a previsão em relação ao A. Em 2024, o B teve MAE ligeiramente menor, mas RMSE maior; em 2022 e 2023 o modelo ingênuo superou ambos os modelos lineares em MAE. **Não foi testado se a legislação causa aumento ou redução de homicídios.**

### O que impede a conclusão mais forte?

O experimento não está tecnicamente travado: o resultado observado é que os modelos complexos não superaram a persistência, em média, num período curto. A série tem apenas três anos de teste; as observações por estado se repetem; há choques temporais e variáveis não observadas. A renda BEA é nominal; as séries históricas podem ter revisões posteriores. A codificação RAND usa aproximações anuais de vigência, sem medir meses de exposição. Algumas modalidades CCW podem coexistir (Louisiana 2024). **Não é apropriado tentar vários algoritmos até aparecer um resultado favorável.**

## Executando localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Abra os notebooks a partir de `notebooks/` como diretório de trabalho. Arquivos:

- [01_eda.ipynb](notebooks/01_eda.ipynb): CDC, coleta e análise exploratória.
- [02_rand_inspection.ipynb](notebooks/02_rand_inspection.ipynb): leis RAND, processamento e auditoria.
- [03_data_integration.ipynb](notebooks/03_data_integration.ipynb): V1, V2, V3 e preparação BLS.
- [05_bea_inspection.ipynb](notebooks/05_bea_inspection.ipynb): preparação BEA.
- [06_model_comparison.ipynb](notebooks/06_model_comparison.ipynb): previsão ingênua, A e B, MAE/RMSE por ano.

**Dependência conhecida:** o notebook 03 cria V2 e depois depende de BEA gerado pelo notebook 05. Para executar manualmente num ambiente limpo: 01, 02, 03 até V2, 05, retornar ao 03 para gerar V3 e, por último, 06. Ainda será necessário automatizar essa dependência e testar a reprodução integral.

**Dados brutos e processados não estão no Git.** O `.gitignore` exclui `data/raw/` e `data/processed/`. Um clone isolado não permite reproduzir os resultados. Prepare os seguintes arquivos originais:

- CDC [Mapping Injury, Overdose, and Violence – State](https://data.cdc.gov/d/fpsi-y8tj), `All_Homicide`, 2019–2024: `data/raw/cdc_homicides_2019_2024.csv`.
- BLS [LAUS](https://www.bls.gov/lau/tables.htm), planilha de `staadata.zip`: `data/raw/staadata/staadata.xlsx`.
- BEA [SAINC1](https://apps.bea.gov/itable/?ReqID=70&step=1), per capita personal income, exportação CSV: `data/raw/bea/personal_income.csv`.
- Planilha RAND 6.0 já versionada em `reports/attachments/`.

Os CSVs processados são gerados nos notebooks. Os resultados de validação estão versionados em `reports/results/`.

## Documentação

- [Protocolo e hipóteses](reports/research_protocol.md)
- [Fontes e dicionário de variáveis](reports/data_dictionary.md)
- [Resultados por rodada e interpretação](reports/experiment_results.md)
- [Problemas atuais e plano de continuidade](reports/next_steps.md)

**Próximo marco:** reproduzir integralmente em ambiente limpo, auditar vigência de leis com datas completas e sobreposições e realizar análises de sensibilidade pré-definidas. Se a regra de classificação mudar, gerar V4 e preservar V3 e as métricas históricas.
