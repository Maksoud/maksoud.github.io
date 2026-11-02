[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Lost in the Middle

## O que é

Lost in the Middle é um fenômeno observado em LLMs no qual o modelo tende a utilizar melhor as informações que aparecem no início ou no final de um contexto longo do que informações igualmente relevantes posicionadas no meio.

Isso é importante em RAG porque o sistema pode recuperar corretamente uma informação, mas a LLM pode não utilizá-la adequadamente se ela estiver escondida entre muitos outros trechos.

O problema não significa que a LLM literalmente "esqueça" tudo que está no meio. Trata-se de uma tendência de desempenho que pode aparecer quando o contexto contém muitas informações.

Podemos representar a ideia assim:

```
Contexto

[Informação relevante]       ← maior chance de utilização
[Informação secundária]
[Informação secundária]
[Informação importante]       ← pode receber menos atenção
[Informação secundária]
[Informação secundária]
[Informação relevante]       ← maior chance de utilização
```

Esse fenômeno é diferente de Context Compression. Context Compression tenta reduzir o excesso de informação antes que ele chegue à LLM. Lost in the Middle descreve um possível problema que pode ocorrer quando muita informação já está presente no contexto.

## Como funciona

Imagine que um sistema RAG recupere vários documentos para responder a uma pergunta.

```
Pergunta
   ↓
Retrieval
   ↓
Documentos recuperados
   ↓
Contexto longo
   ↓
LLM
```

Suponha que a informação necessária para responder esteja em um dos documentos do meio:

```
Contexto

Documento 1
Documento 2
Documento 3
Documento 4  ← informação necessária
Documento 5
Documento 6
Documento 7
Documento 8
```

A LLM recebe todo esse conteúdo, mas a posição da informação pode influenciar sua capacidade de utilizá-la.

Uma representação simplificada seria:

```
Atenção relativa

Início       █████████
             ███████
             █████
Meio         ███
             ██
             ███
Final        ████████
             █████████
```

A tendência observada é que o desempenho pode cair quando a informação relevante está no meio de um contexto muito longo.

Isso cria um problema interessante para RAG: **recuperar a informação correta não é suficiente**. É necessário também apresentá-la de uma forma que facilite sua utilização pela LLM.

Por isso, o pipeline pode utilizar várias estratégias para reduzir esse problema:

```
Retrieval
   ↓
Top-k
   ↓
Reranking
   ↓
Context Compression
   ↓
Organização do contexto
   ↓
LLM
```

O Reranking ajuda a colocar os documentos mais relevantes em posições prioritárias. Context Compression reduz informações desnecessárias. A organização do contexto pode evitar que informações importantes fiquem perdidas entre grandes quantidades de conteúdo.

## Um exemplo

Imagine um assistente corporativo que precisa responder:

```
"Qual é o prazo para solicitar o reembolso de uma viagem?"
```

O Retrieval encontra oito documentos:

```
D1 → Política geral de viagens
D2 → Política de hospedagem
D3 → Política de transporte
D4 → Política de despesas
D5 → Política de reembolso
D6 → Política de viagens internacionais
D7 → Política de cartão corporativo
D8 → Manual financeiro
```

A informação mais importante está em D5:

```
D5:
"Solicitações de reembolso devem ser realizadas
em até 30 dias após o retorno da viagem."
```

Se os documentos forem simplesmente concatenados:

```
D1
D2
D3
D4
D5
D6
D7
D8
```

a informação relevante pode ficar no meio de um contexto extenso.

Uma estratégia melhor pode ser utilizar o Reranking para identificar D5 como o documento mais relevante e depois reduzir o conteúdo dos demais documentos:

```
Pergunta
   ↓
Retrieval
   ↓
D1, D2, D3, D4, D5, D6, D7, D8
   ↓
Reranking
   ↓
D5, D4, D1
   ↓
Context Compression
   ↓
Trechos relevantes
   ↓
LLM
```

O resultado é um contexto mais concentrado:

```
Contexto

D5:
Prazo para solicitação de reembolso:
30 dias após o retorno da viagem.

D4:
Regras complementares para despesas.

D1:
Regras gerais de viagens.
```

Agora, a informação principal tem maior destaque e existe menos conteúdo competindo pela atenção da LLM.

## Por que é importante

Lost in the Middle é importante porque demonstra que **mais contexto não significa necessariamente melhor resposta**.

Em um sistema RAG, pode parecer vantajoso aumentar continuamente o número de documentos recuperados:

```
Top-k = 5
   ↓
Mais informação

Top-k = 20
   ↓
Ainda mais informação

Top-k = 50
   ↓
Muito mais informação
```

Porém, aumentar o contexto pode introduzir informações irrelevantes e dificultar a utilização das informações importantes.

Isso reforça a importância das etapas que já estudamos:

```
Retrieval
   ↓
Encontrar candidatos relevantes
   ↓
Top-k
   ↓
Controlar quantidade de candidatos
   ↓
Reranking
   ↓
Priorizar relevância
   ↓
Context Compression
   ↓
Reduzir conteúdo desnecessário
   ↓
Contexto bem organizado
   ↓
LLM
```

O fenômeno também ajuda a explicar por que o posicionamento dos documentos pode ser relevante. Se uma informação crítica for colocada em uma posição desfavorável dentro de um contexto muito grande, ela pode não ser utilizada tão bem quanto se estivesse em uma posição mais proeminente.

Por isso, em sistemas RAG, qualidade de contexto não significa apenas **quantidade de informação recuperada**. É necessário considerar:

```
Relevância
   +
Quantidade adequada
   +
Contexto suficiente
   +
Organização
   +
Posicionamento
```

Essa é uma das razões pelas quais técnicas como Reranking, Context Compression e seleção cuidadosa do Top-k são importantes. Elas ajudam a transformar um contexto potencialmente grande em um contexto mais focado, aumentando a probabilidade de que a LLM encontre e utilize a informação necessária.

Em resumo, Lost in the Middle mostra que o desafio de um sistema RAG não termina quando o Retrieval encontra a informação correta. É preciso também entregar essa informação à LLM de uma maneira que facilite sua identificação e utilização.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-lost-in-the-middle/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
