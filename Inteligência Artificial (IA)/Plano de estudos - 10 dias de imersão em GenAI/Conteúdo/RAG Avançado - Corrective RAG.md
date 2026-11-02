[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Corrective RAG

## O que é

Corrective RAG, também chamado de **CRAG**, é uma abordagem de RAG que adiciona uma etapa de **avaliação e correção dos resultados recuperados** antes de gerar a resposta final.

Em um RAG tradicional, o sistema recupera documentos e normalmente passa os resultados para o LLM:

```
Pergunta
↓
Retrieval
↓
Documentos
↓
Contexto
↓
LLM
↓
Resposta
```

O problema é que o Retrieval pode retornar documentos pouco relevantes, incompletos ou até não encontrar informação suficiente.

O Corrective RAG introduz um mecanismo para avaliar os resultados:

```
Pergunta
↓
Retrieval
↓
Avaliação dos documentos
↓
Os resultados são suficientes?
├── Sim → geração da resposta
└── Não → correção / nova busca
```

A ideia central é que **o sistema não deve assumir que o Retrieval acertou**.

Ele verifica a qualidade das evidências recuperadas e, quando necessário, tenta corrigir o processo.

## Como funciona

Um fluxo simplificado de Corrective RAG pode ser representado assim:

```
Consulta
↓
Retrieval
↓
Documentos recuperados
↓
Avaliação da relevância
↓
Classificação
├── Relevante
├── Irrelevante
└── Incerto
       ↓
Correção
       ↓
Nova busca / Web Search / Query Reformulation
       ↓
Evidências adicionais
       ↓
Contexto final
       ↓
LLM
       ↓
Resposta
```

A etapa mais importante é a **avaliação dos documentos recuperados**.

O sistema pode utilizar um modelo para verificar se determinado documento realmente contém informações úteis para responder à pergunta.

Por exemplo:

```
Pergunta:
"Qual foi a receita da empresa em 2025?"

Documento A:
Receita da empresa em 2025 → relevante

Documento B:
Histórico de funcionários → irrelevante

Documento C:
Receita de 2024 → parcialmente relevante
```

O sistema pode então decidir que possui alguma evidência, mas talvez precise buscar informações adicionais.

Uma classificação conceitual poderia ser:

```
Resultados recuperados
        ↓
   Avaliador
        ↓
┌───────────────┐
│ Relevantes?   │
└───────────────┘
   ↓        ↓
  Sim      Não
   ↓        ↓
Gerar    Corrigir
         Retrieval
```

A correção pode assumir diferentes formas.

Uma delas é **reformular a consulta**. Se a pergunta original não produziu bons resultados, o sistema pode gerar uma consulta mais adequada.

Outra possibilidade é utilizar uma fonte diferente. Por exemplo, se a busca na base interna não fornecer evidências suficientes, o sistema pode consultar uma fonte externa autorizada.

```
Retrieval interno
      ↓
Resultados insuficientes
      ↓
Query Reformulation
      ↓
Nova busca
      ↓
Ainda insuficiente?
      ↓
Busca em outra fonte
      ↓
Evidências combinadas
```

Isso aproxima o Corrective RAG de sistemas mais adaptativos, mas existe uma diferença importante em relação ao Agentic RAG.

**Corrective RAG é focado especificamente em avaliar e corrigir a recuperação. Agentic RAG é uma abordagem mais ampla, na qual um agente pode planejar, escolher ferramentas, decompor tarefas e decidir quais ações executar.**

Um sistema pode inclusive combinar os dois:

```
Agentic RAG
     ↓
Planeja a investigação
     ↓
Retrieval
     ↓
Corrective RAG
     ↓
Avalia os resultados
     ↓
Resultados insuficientes
     ↓
Agente decide próxima ação
     ↓
Nova busca
     ↓
Contexto final
     ↓
LLM
```

## Um exemplo

Imagine um assistente corporativo conectado a uma base de documentos internos.

O usuário pergunta:

> "Qual é o prazo de reembolso para viagens internacionais?"

O sistema faz o Retrieval e encontra:

```
Documento A:
Política de reembolso nacional.

Documento B:
Política de viagens de 2023.

Documento C:
Manual de solicitação de despesas.
```

Nenhum dos documentos responde claramente à pergunta sobre viagens internacionais.

Um RAG tradicional poderia simplesmente enviar esses documentos ao LLM. O modelo poderia tentar inferir a resposta a partir de informações incompletas.

No Corrective RAG, os documentos são avaliados:

```
Pergunta
↓
Retrieval
↓
Documentos
↓
Avaliação

A → parcialmente relevante
B → desatualizado
C → relevante para processo, mas não para prazo
↓
Evidências insuficientes
↓
Correção
```

O sistema pode então reformular a consulta:

```
"prazo reembolso despesas viagem exterior política internacional"
```

Uma nova busca pode encontrar:

```
Política de viagens internacionais
Seção 5: Reembolso
Prazo para solicitação: 30 dias após o retorno.
```

Agora existe evidência suficiente:

```
Primeira busca
      ↓
Resultados insuficientes
      ↓
Correção
      ↓
Nova busca
      ↓
Documento relevante
      ↓
Contexto final
      ↓
LLM
      ↓
"Segundo a política de viagens internacionais,
o pedido deve ser realizado em até 30 dias após o retorno."
```

Nesse exemplo, o Corrective RAG evita que o LLM trate uma recuperação ruim como se fosse uma recuperação confiável.

## Por que é importante

Corrective RAG é importante porque **a qualidade da resposta de um sistema RAG depende diretamente da qualidade das evidências recuperadas**.

Mesmo um LLM muito bom pode produzir uma resposta inadequada se receber documentos errados ou insuficientes.

A ideia pode ser resumida assim:

```
RAG tradicional

Retrieval
↓
"Espero que os documentos estejam corretos"
↓
LLM


Corrective RAG

Retrieval
↓
"Vamos verificar os documentos"
↓
Resultados suficientes?
├── Sim → LLM
└── Não → Corrigir Retrieval
```

Isso cria uma camada de **controle de qualidade sobre o Retrieval**.

É especialmente útil quando a base contém documentos muito semelhantes, informações desatualizadas, consultas ambíguas ou quando a pergunta pode exigir fontes que não estejam na coleção principal.

Por outro lado, essa verificação adicional aumenta a complexidade, latência e custo do sistema. Também é necessário definir critérios confiáveis para determinar quando uma recuperação é suficientemente boa.

Uma forma de visualizar sua posição dentro da arquitetura RAG é:

```
Pergunta
↓
Retrieval
↓
Top-k
↓
Reranking
↓
Avaliação corretiva
↓
Contexto suficiente?
├── Sim → Contexto final → LLM
└── Não → Nova busca
              ↓
          Avaliação corretiva
```

Assim, o Corrective RAG representa uma evolução importante do RAG tradicional: **em vez de confiar cegamente no resultado do Retrieval, o sistema verifica a qualidade das evidências e pode tentar recuperar informações melhores antes de permitir que o LLM formule a resposta.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/rag-avancado-corrective-rag/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
