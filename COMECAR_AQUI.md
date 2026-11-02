# COMEÇAR AQUI · US Gun Policy ML

Este guia é para **dois estudantes de ADS** que querem abrir o trabalho, entender o que cada parte faz e reproduzir o experimento sem executar dezenas de células isoladas.

## 1. Abrir o projeto

Abra o terminal **na pasta raiz do repositório** (onde estão `README.md`, `notebooks/` e `requirements.txt`). Se o projeto já estiver instalado e a pasta `.venv` existir:

```bash
source .venv/bin/activate
jupyter lab
```

Se for a primeira vez neste computador:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

No navegador, abra `notebooks/` e comece pelo **01**. Para manter a ordem, execute os três blocos de código de cada notebook **um por vez**. Leia a explicação curta antes do bloco; não precisa dar Play em cada linha.

## 2. Ordem correta: 01 → 02 → 03 → 04 → 05 → 06

| Notebook | O que faz | O que você confere ao terminar |
| --- | --- | --- |
| **01_cdc** | Baixa os homicídios do CDC. | 300 linhas, 50 estados, anos 2019–2024. |
| **02_rand** | Transforma dados das leis RAND em colunas. | Dois arquivos, cada um com 300 linhas. |
| **03_bls** | Organiza o desemprego do BLS. | 300 linhas, 3 colunas. |
| **04_bea** | Organiza a renda por habitante do BEA. | 300 linhas, 3 colunas. |
| **05_integracao** | Junta as quatro fontes e cria a resposta do ano seguinte. | Base V3 com **250 linhas e 13 colunas**. |
| **06_modelos** | Treina A e B, compara com previsão simples e mede os erros. | Tabela de nove resultados e resumo das médias. |

Cada notebook tem **3 blocos** e explicação de cada um. Total: **18 execuções de código**, em vez de aproximadamente 75 células espalhadas. Alguns blocos contêm mais de uma operação, mas continuam organizados por objetivo: **abrir → preparar → conferir/salvar**.

### Antes de executar: arquivos que precisam existir

O Git **não inclui** `data/raw/` e `data/processed/`. Confira estas entradas:

- Notebook 01: internet para baixar o CSV do CDC automaticamente.
- Notebook 02: `reports/attachments/TL-A243-2-v4 State Firearm Law Database 6.0.xlsx` (já está no repositório).
- Notebook 03: `data/raw/staadata/staadata.xlsx` (extraído do arquivo `staadata.zip` disponível no [BLS](https://www.bls.gov/lau/tables.htm)).
- Notebook 04: `data/raw/bea/personal_income.csv` (exportação CSV da tabela **SAINC1** do [BEA](https://apps.bea.gov/itable/?ReqID=70&step=1), renda pessoal per capita em dólares).

Para usar os mesmos dados históricos, mantenha as mesmas fontes e anos. Fontes atualizadas podem mudar valores por revisão.

## 3. Como estudar sem se perder

Em cada notebook, siga esta sequência:

1. Leia a frase que explica **para que serve o bloco**.
2. Execute aquele bloco e observe **a quantidade de linhas e colunas**.
3. Só avance se o resultado fizer sentido ou se a validação terminar sem erro.

Se ocorrer `FileNotFoundError`, confira o nome e o lugar do arquivo. Se ocorrer `NameError`, execute os blocos anteriores **do mesmo notebook**, na ordem. Se aparecer `AssertionError`, alguma verificação não correspondeu à versão esperada dos dados; investigue antes de continuar.

## 4. Resultado esperado ao executar o notebook 06

Com os mesmos dados do experimento original, os valores devem ser próximos destes. **Quanto menor o erro, melhor a previsão.**

| Modelo | MAE médio | RMSE médio |
| --- | ---: | ---: |
| **Ingênuo**: repetir o ano anterior | **0,785** | **1,027** |
| **Modelo A**: taxa anterior + desemprego + renda | 0,944 | 1,239 |
| **Modelo B**: modelo A + leis de armas | 0,959 | 1,263 |

**MAE** é o erro médio; **RMSE** dá maior peso aos erros grandes. O teste é chamado **aprendizado supervisionado** porque ensinamos o programa com exemplos cujas respostas são conhecidas. O treino em **janela expansiva** significa que aumentamos a quantidade de anos usados para aprender em cada rodada.

Esses valores são nossa **referência histórica**, não garantia de números idênticos se alguma fonte oficial tiver sido atualizada. A regressão linear foi mantida para não alterar a experiência sem necessidade.

## 5. O que concluir?

Nos testes atuais, acrescentar informações sobre leis **não ajudou de forma constante** a prever a taxa de homicídios do próximo ano. A previsão mais simples teve o menor erro médio. Isso é um resultado legítimo do trabalho, mas **não demonstra** que uma lei aumenta ou reduz homicídios. Nosso alvo são homicídios totais, não apenas os causados por armas.

Os números completos estão em [resultados](reports/experiment_results.md). O [README](README.md) explica o projeto em poucos minutos.

## 6. O que fazer após reproduzir?

Confira os gráficos e prepare uma apresentação curta: nossa pergunta, de onde vieram os dados, como treinamos, os três resultados e as limitações. **Não precisamos adicionar outro algoritmo para concluir esta etapa.**
