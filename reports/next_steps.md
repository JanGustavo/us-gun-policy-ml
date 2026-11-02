# O que já fizemos e o que falta

Este é um trabalho de **dois estudantes**, com foco em aplicar conceitos básicos de aprendizado supervisionado e entender os resultados, não em construir uma pesquisa profissional completa.

## Concluído

- [x] Escolhemos uma pergunta que pode ser testada com dados.
- [x] Reunimos informações de homicídios, leis, desemprego e renda.
- [x] Limpamos e juntamos as tabelas usando estado e ano.
- [x] Criamos exemplos com informações de um ano e taxa de homicídios do ano seguinte.
- [x] Treinamos dois modelos de regressão linear e usamos uma previsão simples como comparação.
- [x] Medimos erros em 2022, 2023 e 2024.
- [x] Conferimos 18 mudanças de classificação das leis de porte de armas na RAND.

## O problema que encontramos

Queríamos saber se adicionar informações sobre leis ajudaria a prever melhor. **Não ajudou de maneira constante** nos testes feitos. O resultado médio mais baixo foi o da previsão simples. Isso não significa que o projeto deu errado: encontramos uma resposta possível, reconhecendo que temos poucos dados e um modelo básico.

## Próximos passos possíveis

- [ ] **Primeiro:** abrir os notebooks na ordem e confirmar que todas as células funcionam depois de reiniciar o Jupyter.
- [ ] **Depois:** simplificar a ordem de preparação dos arquivos, porque hoje precisamos sair do notebook 03, abrir o 05 e voltar ao 03.
- [ ] **Conferir:** se a data de algumas leis foi registrada corretamente, principalmente quando começaram no meio de um ano. Não apagar a versão antiga se precisarmos corrigir algo.
- [ ] **Apresentar:** criar gráficos simples com os erros de cada modelo e explicar com nossas próprias palavras o que fizemos.
- [ ] **Se houver tempo:** testar mais uma ideia de forma planejada, sem escolher o resultado que mais favoreça uma opinião.

## O que não precisamos fazer agora

Não precisamos adicionar muitos algoritmos, criar fórmulas complexas ou fazer afirmações sobre causa e efeito. Uma explicação clara dos métodos e das limitações é mais importante do que deixar o projeto artificialmente complicado.


## Nova ordem de execução (02/11/2026)

A preparação foi reorganizada em **seis notebooks sequenciais** e três blocos por notebook: `01_cdc`, `02_rand`, `03_bls`, `04_bea`, `05_integracao`, `06_modelos`. A lógica do primeiro experimento foi mantida (regressão linear, mesmos atributos e janelas temporais). O CSV supervisionado principal continua sendo a **V3**; as versões V1/V2 foram etapas históricas do desenvolvimento, mas não são mais geradas pelos notebooks novos. Veja [COMECAR_AQUI.md](../COMECAR_AQUI.md) para a ordem e os comandos.

**Reprodutibilidade:** os blocos foram reorganizados para depender apenas dos arquivos de etapas anteriores, mas ainda é necessário conferir a execução completa com os dados originais. As métricas de referência no relatório não foram substituídas por resultados inventados.
