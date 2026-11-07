# COMEÇAR AQUI · AV2

Este guia é para executar o **fluxo principal atual** do projeto. Nossa pergunta é: **existe relação entre a quantidade de registros de regras estaduais sobre armas da RAND e a taxa de homicídios nos estados americanos?** A entrega v1.0 pede as fontes, a hipótese e as bases abertas com Pandas no [Colab](https://colab.research.google.com/github/JanGustavo/us-gun-policy-ml/blob/main/notebooks/00_av2_v1_colab.ipynb). A análise da relação vem depois.

## Fluxo principal: 01 → 02 → 05

| Notebook | O que faz | Saída esperada |
| --- | --- | --- |
| `01_cdc.ipynb` | Baixa e confere as taxas de homicídios do CDC. | CSV bruto com 306 linhas, incluindo Washington, D.C. |
| `02_rand.ipynb` | Abre a planilha RAND, preserva as colunas antigas e conta registros de regras vigentes no fim de cada ano. | `rand_law_counts_2019_2024.csv` com 300 linhas. |
| `05_integracao.ipynb` | Junta CDC e RAND pelo mesmo estado e ano. | `us_gun_policy_association_2019_2024.csv` com 300 linhas e 7 colunas. |

A planilha RAND já está em `reports/attachments/`. O notebook 01 precisa de internet para baixar o CSV do CDC. Os arquivos em `data/raw/` e `data/processed/` são gerados localmente e não são enviados ao Git.

## Como executar no computador

Na pasta raiz do repositório:

```bash
source .venv/bin/activate
jupyter lab
```

Se `.venv` não existir, crie o ambiente e instale `requirements.txt` antes. Abra os notebooks indicados acima e execute os **três blocos de código de cada um, na ordem**. No notebook 05, confira 50 estados em cada ano de 2019 a 2024.

## Como interpretar a contagem

Cada `Law ID` é um **registro da base RAND**, não necessariamente uma lei aprovada distinta. Contamos registros `Implement` ou `Modify` vigentes em **31 de dezembro** do ano. Não contamos eventos `Repeal` nem linhas `See note`. A RAND classifica os registros como `Restrictive` ou `Permissive`; guardamos as duas contagens e a soma. Assim, “mais registros” não significa automaticamente “leis mais rígidas”.

A variável de homicídios é uma **taxa por 100 mil habitantes** e considera homicídios totais, não apenas os cometidos com armas de fogo. Encontrar uma relação entre as colunas não provará que as leis causaram uma mudança na taxa.

## Material do experimento anterior

`03_bls.ipynb` e `04_bea.ipynb` preparam indicadores econômicos usados na antiga tarefa de previsão. Eles dependem de arquivos brutos externos que não estão no Git. `06_modelos.ipynb`, a base `us_gun_policy_supervised_v3.csv` e `reports/experiment_results.md` documentam aquele experimento. **Não são necessários para reproduzir a base da pergunta principal atual.** Seus resultados continuam guardados como histórico, sem serem apresentados como resposta à nova hipótese.

Para conferir a lógica de preparação da nova base, rode:

```bash
.venv/bin/python -m unittest discover -s tests -v
```
