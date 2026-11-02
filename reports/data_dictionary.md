# Dicionário de Dados

## Dataset 01: Homicídios nos Estados Unidos

**Fonte:** Centers for Disease Control and Prevention (CDC)  
**Dataset:** Mapping Injury, Overdose, and Violence - State  
**Link:** <https://data.cdc.gov/d/fpsi-y8tj>  
**Unidade de análise desejada:** Estado e ano  
**Situação:** Coleta concluída e estrutura validada para 2019–2024.

### Variáveis planejadas

| Variável | Descrição |
| --- | --- |
| `state` | Estado americano |
| `year` | Ano de referência |
| `homicide_count` | Número anual de homicídios |
| `homicide_rate` | Taxa anual de homicídios por 100 mil habitantes |

Esses são os nomes padronizados que pretendemos utilizar no projeto. Os nomes originais das colunas serão identificados após a inspeção do dataset.

### Critérios de seleção

- Utilizar inicialmente os 50 estados americanos.
- Selecionar registros anuais, não períodos móveis de 12 meses.
- Utilizar homicídios totais, independentemente do meio utilizado.
- Preferir taxas brutas por 100 mil habitantes para a variável-alvo.
- Verificar a existência de dados provisórios, ausentes ou suprimidos.
- Registrar os anos disponíveis antes de definir o período da pesquisa.

### Observações

A base utiliza informações de mortalidade do National Vital Statistics System (NVSS).

Homicídios, suicídios e mortes por intervenção legal não devem ser somados indiscriminadamente.

A cobertura temporal foi confirmada de 2019 a 2024, com registros dos 50 estados. Ainda será necessário verificar possíveis revisões e o caráter definitivo das informações.

## Coleta 01: CDC - Homicídios

**Fonte:** Centers for Disease Control and Prevention (CDC)  
**Dataset:** Mapping Injury, Overdose, and Violence - State  
**Arquivo:** `data/raw/cdc_homicides_2019_2024.csv`  
**Período:** 2019 a 2024  
**Indicador:** `All_Homicide`  
**Data da coleta:** 02/11/2026

### Resultado da validação inicial

- 306 registros originais, incluindo Washington, D.C.
- 300 registros referentes aos 50 estados americanos.
- 50 estados representados em cada ano.
- Nenhum registro duplicado por estado e ano.
- Nenhuma taxa ou contagem ausente nos 300 registros analisados.

### Campos utilizados

| Campo original | Significado |
| --- | --- |
| `geoid` | Código geográfico do estado |
| `name` | Nome do estado |
| `period` | Ano de referência |
| `count_sup` | Contagem de homicídios |
| `rate` | Taxa de homicídios por 100 mil habitantes |
| `data_as_of` | Data de referência da versão dos dados |

### Decisões metodológicas

- Utilizar `All_Homicide`, sem misturar suicídios e outras causas de morte.
- Excluir Washington, D.C. apenas na etapa de processamento.
- Preservar o CSV original sem alterações.
- Utilizar a taxa de homicídios como variável-alvo.
- Documentar possíveis revisões dos dados e verificar seu caráter final ou provisório.

## Dataset 02: Legislação de porte oculto (RAND)

**Fonte:** RAND State Firearm Law Database 6.0  
**Período:** 2019 a 2024  
**Arquivo processado:** `data/processed/rand_ccw_2019_2024.csv`  
**Unidade de análise:** Estado e ano

### Variáveis

| Variável | Descrição |
| --- | --- |
| `state` | Estado americano |
| `year` | Ano de referência |
| `ccw_shall_issue` | Existência de regime de licença do tipo shall issue |
| `ccw_permitless` | Existência de modalidade de porte oculto sem exigência de licença |
| `ccw_may_issue` | Existência de regime de licença do tipo may issue |
| `ccw_prohibited` | Existência de registro de proibição de porte oculto |

As variáveis utilizam 1 para presença e 0 para ausência da modalidade identificada nos registros da RAND.

### Tratamento realizado

- Seleção da categoria `carrying a concealed weapon (ccw)`.
- Identificação das modalidades por estado e ano.
- Exclusão de Washington, D.C., do arquivo processado.
- Validação de 300 observações, sem duplicações ou combinações sem modalidade identificada.
- Identificação de uma observação com modalidades simultâneas.

**Limitação:** a codificação utiliza os anos de entrada em vigor e substituição como aproximação anual, sem considerar datas específicas dentro do ano. O arquivo representa uma versão inicial da transformação, sujeita a validação metodológica antes do treinamento.

### Classificação anual das leis de porte de armas (CCW)

Os indicadores de porte de armas foram construídos a partir da RAND State
Firearm Law Database 6.0.

Foram consideradas quatro modalidades: `shall_issue`, `may_issue`,
`permitless` e `prohibited`.

Para esta análise, utilizamos uma classificação anual do regime de porte,
tomando como referência a situação vigente ao final de cada ano (31 de
dezembro).

A verificação das transições de 2019 a 2023 identificou 18 mudanças de
modalidade: 12 para `permitless` e seis de `may_issue` para `shall_issue`.
Todas apresentaram correspondência com os anos de alteração registrados na
RAND.

As seis mudanças de `may_issue` para `shall_issue` em 2022 estão associadas à
decisão judicial *New York State Rifle & Pistol Association v. Bruen*, de 23 de
junho de 2022.

**Limitações:** a classificação não representa necessariamente o regime vigente
durante os 12 meses de cada ano. Além disso, `permitless` não significa que um
estado deixou de emitir licenças opcionais, e uma mudança de classificação não
representa necessariamente uma nova lei aprovada pelo Legislativo.

A conferência realizada verificou as transições observadas na base
supervisionada, mas não substitui uma auditoria completa de todos os registros
legislativos.

## Dataset 03: Verificação de antecedentes (RAND)

**Fonte:** RAND State Firearm Law Database 6.0  
**Período:** 2019 a 2024  
**Arquivo processado:** `data/processed/rand_background_2019_2024.csv`  
**Categoria:** `background checks`  
**Subtipo:** `private sales : point of sale`  
**Unidade de análise:** Estado e ano

### Variáveis

| Variável | Descrição |
| --- | --- |
| `state` | Estado americano |
| `year` | Ano de referência |
| `background_handgun` | Exigência estadual identificada para vendas privadas de armas curtas |
| `background_longgun` | Exigência estadual identificada para vendas privadas de armas longas |

### Tratamento realizado

- Selecionados os registros do subtipo `private sales : point of sale`.
- Consideradas as datas de entrada em vigor e substituição.
- Registros classificados como `Repeal` não foram considerados exigências vigentes.
- Registros do tipo `handgun and long gun` foram considerados para ambas as variáveis.
- Excluído Washington, D.C., para manter os 50 estados.
- Geradas 300 observações, sem duplicações por estado e ano.

### Resultado da validação inicial

Em 2024, a codificação identificou:

- 18 estados com exigência relativa a armas curtas.
- 17 estados com exigência relativa a armas longas.
- North Carolina apresentou mudança de 1 para 0 na variável de armas curtas em 2023, consistente com a revogação registrada pela RAND.

### Limitações

As variáveis representam exclusivamente o subtipo legislativo analisado, não todas as exigências estaduais ou federais de verificação de antecedentes.

A transformação utiliza uma aproximação anual das datas de vigência e ainda necessita de validação adicional antes do treinamento.

## BLS: desemprego

BLS LAUS, médias anuais estaduais de 2019–2024. `unemployment_rate` é porcentagem anual. Arquivo processado `data/processed/bls_unemployment_2019_2024.csv`: 300 estado-anos, sem duplicações ou ausência de taxa.

## BEA: renda pessoal per capita

BEA SAINC1, `Per capita personal income (dollars)`. `income_per_capita` é renda **nominal**, não renda mediana, nem ajustada pela inflação. Arquivo processado `data/processed/bea_income_2019_2024.csv`: 300 estado-anos, sem duplicações ou ausência.

## Versão supervisionada V3

`data/processed/us_gun_policy_supervised_v3.csv`: 250 × 13, entradas de 2019–2023 e taxa alvo `homicide_rate_next_year` de 2020–2024. `homicide_count` permanece na tabela, porém não é variável preditora nos modelos atuais; `state` e `year` são chaves. A usa `homicide_rate`, `unemployment_rate`, `income_per_capita`. B acrescenta `ccw_permitless`, `ccw_may_issue`, `background_handgun`, `background_longgun`, usando `ccw_shall_issue` como categoria implícita de referência; `ccw_prohibited` não variou no treino.

As quatro categorias CCW somaram exatamente 1 nas 250 observações supervisionadas verificadas, **não** necessariamente nos 300 registros de 2019–2024; Louisiana 2024 apresentou sobreposição. A vigência jurídica foi aproximada pelo ano, e a convenção de fim de ano precisa de validação com datas completas.
