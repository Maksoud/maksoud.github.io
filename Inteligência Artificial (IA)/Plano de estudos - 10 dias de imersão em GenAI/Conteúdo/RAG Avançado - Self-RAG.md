[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Self-RAG

## O que é

Self-RAG é uma abordagem de RAG na qual o próprio modelo participa ativamente da **decisão sobre quando recuperar informações, quais informações utilizar e como avaliar a resposta gerada**.

Em um RAG tradicional, o Retrieval costuma acontecer sempre:

```
Pergunta
↓
Retrieval
↓
Contexto
↓
LLM
↓
Resposta
```

Isso pode ser desnecessário para perguntas que o modelo já consegue responder com seu conhecimento interno. Também não garante que o modelo utilizará corretamente os documentos recuperados.

O Self-RAG introduz um mecanismo de **autoavaliação e controle do processo de geração**.

O modelo pode decidir, por exemplo:

```
Pergunta
↓
Preciso recuperar informações?
├── Não → Gerar resposta
└── Sim → Retrieval
              ↓
        Avaliar evidências
              ↓
        Gerar resposta
              ↓
        Avaliar resposta
              ↓
        Melhorar, se necessário
```

A ideia central é tornar o RAG **adaptativo e autocontrolado**, em vez de executar Retrieval e geração de maneira fixa.

## Como funciona

O Self-RAG utiliza mecanismos de avaliação chamados **reflection tokens**, que permitem ao modelo sinalizar diferentes aspectos do processo.

De forma simplificada, o modelo pode avaliar:

```
Retrieval necessário?
        ↓
Documentos relevantes?
        ↓
Resposta fundamentada nos documentos?
        ↓
Resposta útil para a pergunta?
```

Essas avaliações orientam o comportamento do sistema.

Por exemplo, considere:

> "O que é uma rede neural?"

O modelo pode determinar que não precisa consultar uma base externa.

Já para:

> "Qual foi a receita da empresa no terceiro trimestre de 2026?"

o modelo pode reconhecer que precisa de informações externas ou documentos corporativos.

Assim:

```
Pergunta
↓
Avaliação
↓
Necessita conhecimento externo?
├── Não → Geração direta
└── Sim → Retrieval
```

Depois da recuperação, o modelo também pode avaliar a relevância das evidências:

```
Documentos recuperados
↓
São relevantes?
├── Sim → utilizar
└── Não → buscar novamente
```

Durante a geração, o modelo pode avaliar se cada afirmação está realmente apoiada pelas evidências recuperadas.

Por exemplo:

```
Documento:
"A empresa apresentou crescimento de 12% em 2025."

Resposta:
"A empresa apresentou crescimento de 12% em 2025."
        ↓
A afirmação está apoiada?
        ↓
Sim
```

Se o modelo gerar uma afirmação que não esteja sustentada pelos documentos, pode revisar a resposta ou buscar evidências adicionais.

Isso é especialmente importante para reduzir **alucinações**, porque o sistema não considera apenas "qual resposta parece plausível", mas também "qual resposta está sustentada pelo contexto recuperado".

Uma forma simplificada de visualizar o processo é:

```
                 ┌──────────────────────┐
                 │      Pergunta        │
                 └──────────┬───────────┘
                            ↓
                  Precisa de Retrieval?
                       ↙          ↘
                     Não          Sim
                      ↓             ↓
                  Geração       Retrieval
                                    ↓
                             Avaliar relevância
                                    ↓
                              Gerar resposta
                                    ↓
                         Avaliar fundamentação
                                    ↓
                         Avaliar qualidade
                                    ↓
                         ┌──────────┴──────────┐
                         ↓                     ↓
                      Aceitar              Revisar
```

Essa capacidade de avaliação é o que diferencia Self-RAG de simplesmente adicionar um Reranker ou um Corrective RAG.

**Reranking** avalia quais documentos são mais relevantes para a consulta.

**Corrective RAG** concentra-se em detectar problemas na recuperação e corrigi-los.

**Self-RAG** amplia essa ideia para que o próprio processo de geração seja controlado por avaliações feitas pelo modelo.

## Um exemplo

Imagine um assistente corporativo conectado a uma base de políticas internas.

O usuário pergunta:

> "Posso trabalhar remotamente às sextas-feiras?"

O Self-RAG pode executar um processo semelhante a:

```
Pergunta
↓
Avaliação:
"Essa informação depende das políticas internas."
↓
Retrieval
↓
Documentos encontrados
↓
Avaliação:
"Este documento trata de trabalho remoto."
↓
Geração
↓
"Segundo a política de trabalho híbrido..."
↓
Avaliação:
"A afirmação está apoiada pelo documento?"
↓
Sim
↓
Resposta final
```

Agora imagine que o Retrieval encontre apenas um documento antigo:

```
Política de trabalho remoto, versão 2023
```

O modelo pode identificar que a evidência pode estar desatualizada:

```
Documento recuperado
↓
Relevante?
Sim
↓
Atualizado?
Não / incerto
↓
Nova busca
↓
Política de trabalho híbrido, versão 2026
↓
Geração
↓
Avaliação
↓
Resposta final
```

Nesse caso, o modelo não apenas recuperou informação. Ele **avaliou a qualidade da evidência antes de utilizá-la**.

Uma característica importante é que o Self-RAG pode decidir que o Retrieval não é necessário.

Por exemplo:

```
Pergunta:
"O que é uma embedding?"

↓
Self-RAG

Conhecimento externo necessário?
Não

↓
Resposta direta
```

Enquanto:

```
Pergunta:
"Qual foi o valor do contrato firmado pela empresa em março de 2026?"

↓
Self-RAG

Conhecimento externo necessário?
Sim

↓
Retrieval
↓
Avaliação
↓
Resposta fundamentada
```

Isso pode reduzir Retrievals desnecessários e tornar o sistema mais eficiente.

## Por que é importante

Self-RAG é importante porque tenta resolver uma limitação fundamental dos pipelines RAG tradicionais: **nem toda pergunta precisa de Retrieval, e nem todo resultado recuperado merece ser utilizado**.

Ele introduz um ciclo de avaliação:

```
Pergunta
↓
Decidir se deve recuperar
↓
Recuperar
↓
Avaliar evidências
↓
Gerar
↓
Avaliar geração
↓
Revisar quando necessário
```

Isso pode melhorar a **factualidade, relevância e controle das respostas**, especialmente em situações nas quais o sistema precisa combinar conhecimento interno do modelo com informações externas ou documentos privados.

Também é importante diferenciá-lo do Agentic RAG.

No Agentic RAG, um agente pode planejar uma sequência de ações, escolher ferramentas e realizar uma investigação mais ampla.

No Self-RAG, o foco está na **autorregulação do processo de Retrieval e geração**, incluindo decisões sobre recuperação, avaliação das evidências e qualidade da resposta.

Uma forma de posicionar os conceitos é:

```
RAG tradicional
    ↓
Retrieval sempre que o pipeline é executado

Corrective RAG
    ↓
Verifica e corrige a recuperação

Self-RAG
    ↓
Decide quando recuperar
Avalia o que recuperou
Avalia o que gerou

Agentic RAG
    ↓
Planeja e executa ações de investigação
```

Essas abordagens não são necessariamente concorrentes. Um sistema avançado pode combinar diferentes ideias. Por exemplo, um agente pode utilizar Self-RAG para avaliar suas evidências e Corrective RAG para corrigir uma recuperação insuficiente.

O ponto central do Self-RAG é, portanto, transformar o RAG de um pipeline relativamente passivo em um processo **adaptativo, avaliativo e autorregulado**, no qual o modelo não apenas responde, mas também participa da decisão sobre **quando buscar, o que confiar e quando revisar sua própria resposta**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-self-rag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
