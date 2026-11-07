# COMEÇAR AQUI · AV2

A pergunta principal é: **os registros de regras estaduais sobre armas da RAND têm relação com a taxa de homicídios nos estados americanos?** Para fazer uma comparação menos desigual, usamos também desemprego (BLS) e renda por pessoa (BEA). O notebook 06 examina a associação entre regras vigentes no fim de um ano e a taxa de homicídios do ano seguinte. Ele **não identifica um impacto causal direto**.

## Ordem: 01 → 02 → 03 → 04 → 05 → 06

| Notebook | O que faz | O que conferir |
| --- | --- | --- |
| `01_cdc.ipynb` | Baixa homicídios totais do CDC. | CSV bruto com 306 linhas, incluindo Washington, D.C. |
| `02_rand.ipynb` | Lê a RAND, prepara categorias de porte/antecedentes e conta registros vigentes. | Três CSVs RAND, cada um com 300 linhas. |
| `03_bls.ipynb` | Prepara desemprego estadual. | 300 linhas. |
| `04_bea.ipynb` | Prepara renda pessoal por habitante. | 300 linhas. |
| `05_integracao.ipynb` | Junta as quatro fontes por estado e mesmo ano. | **300 linhas e 15 colunas.** |
| `06_modelos.ipynb` | Ajusta um modelo de associação com estado, ano, desemprego e renda. | Coeficientes e intervalos para registros restritivos e permissivos. |

Cada notebook tem **três blocos de código**. Execute os blocos na ordem, lendo o texto entre eles. Também é possível usar **Run → Run All Cells** em um notebook de cada vez, depois de concluir o anterior. Se o Jupyter já estava aberto quando o arquivo mudou, feche a aba sem salvar e reabra o notebook do disco.

## Arquivos necessários

- `01`: internet para baixar o CSV do CDC. O arquivo local é salvo em `data/raw/cdc_homicides_2019_2024.csv`.
- `02`: `reports/attachments/TL-A243-2-v4 State Firearm Law Database 6.0.xlsx`, já no repositório.
- `03`: `data/raw/staadata/staadata.xlsx`, extraído do ZIP do [BLS](https://www.bls.gov/lau/tables.htm).
- `04`: `data/raw/bea/personal_income.csv`, exportação da tabela SAINC1, indicador *Per capita personal income (dollars)*, do [BEA](https://apps.bea.gov/itable/?ReqID=70&step=1).

Os arquivos brutos de BLS/BEA e os arquivos processados **não são enviados ao Git**. Nesta máquina, os arquivos brutos e processados estão disponíveis e os notebooks 03/04 foram executados com os brutos. Em uma cópia nova do repositório, será preciso baixar os arquivos indicados acima. Se apenas os CSVs processados estiverem disponíveis, os notebooks 03/04 os reutilizam e informam a origem na tela.

## Abrir o JupyterLab

Na pasta raiz do projeto:

```bash
source .venv/bin/activate
jupyter lab
```

Se `.venv` não existir, crie o ambiente e instale `requirements.txt` antes. Abra a pasta `notebooks/` no navegador.

## Como interpretar o resultado

A variável de homicídios é uma **taxa por 100 mil habitantes**, não a contagem de todos os crimes. Cada `Law ID` é um registro RAND, não necessariamente uma lei aprovada distinta. Contamos registros `Implement` e `Modify` vigentes em **31 de dezembro** de cada ano, separados em `Restrictive` e `Permissive`.

O 06 compara mudanças **dentro do mesmo estado**, considera diferenças gerais entre anos e usa desemprego e renda do ano anterior. Isso controla algumas diferenças observadas e características estáveis do estado; **não mede cultura diretamente** nem elimina todos os fatores que podem influenciar homicídios e legislação. Os intervalos atuais das duas contagens incluem zero: a direção da associação é inconclusiva. Não respondemos “as leis causam aumento ou queda” com um sim ou não.

O experimento anterior de previsão foi preservado em `notebooks/arquivo/06_previsao_anterior.ipynb` e `reports/experiment_results.md`; seus resultados não são a resposta da pergunta atual.

Para executar os testes do código:

```bash
.venv/bin/python -m unittest discover -s tests -v
```
