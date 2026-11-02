[← Voltar para o Dia 6: RAG avançado](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-06-rag-avancado/)

# Parent-child Retrieval

## O que é

Parent-child Retrieval é uma estratégia de Chunking e Retrieval na qual um documento é dividido em chunks de diferentes tamanhos, criando uma relação entre **chunks filhos (children)** e **chunks pais (parents)**.

A ideia é separar duas necessidades que normalmente entram em conflito no RAG:

```
Child
↓
bom para encontrar a informação

Parent
↓
bom para fornecer contexto
```

Os chunks filhos são menores e mais específicos, facilitando a localização de um trecho relevante durante o Retrieval. Depois que um child é encontrado, o sistema recupera o respectivo parent, que contém uma quantidade maior de contexto, para ser enviado à LLM.

Assim, o sistema não precisa escolher entre chunks muito pequenos ou muito grandes. Ele utiliza os dois em etapas diferentes.

## Como funciona

Primeiro, o documento é dividido em chunks maiores, que funcionam como parents. Esses parents são então subdivididos em chunks menores, que funcionam como children.

```
Documento
    ↓
Parent Chunk
    ↓
┌──────────┬──────────┬──────────┐
│ Child 1  │ Child 2  │ Child 3  │
└──────────┴──────────┴──────────┘
```

Um documento pode, por exemplo, ser organizado assim:

```
Documento
   ↓
Parent 1
   ├── Child 1
   ├── Child 2
   └── Child 3

Parent 2
   ├── Child 4
   ├── Child 5
   └── Child 6
```

Os embeddings são normalmente gerados para os children, porque eles representam unidades menores e mais específicas de informação.

Quando o usuário faz uma pergunta, o Retrieval procura primeiro entre os children:

```
Pergunta
   ↓
Embedding da pergunta
   ↓
Busca entre Children
   ↓
Child relevante
   ↓
Identificação do Parent
   ↓
Parent recuperado
   ↓
Contexto
   ↓
LLM
```

Suponha que o usuário pergunte:

```
"Qual é o prazo para solicitar reembolso de uma viagem?"
```

O sistema pode encontrar:

```
Child 27:
"O pedido deve ser realizado em até 30 dias após o retorno."
```

Esse child pertence a:

```
Parent 8:
Política de Reembolso de Viagens

Seção completa sobre solicitação,
prazos, documentação e exceções.
```

Em vez de enviar apenas o pequeno Child 27 para a LLM, o sistema pode recuperar o Parent 8 e fornecer mais contexto.

Isso resolve um problema comum do Chunking: um chunk pequeno pode ser excelente para encontrar uma informação, mas insuficiente para interpretá-la corretamente.

O processo pode ser visualizado assim:

```
                    Documento
                        ↓
                 Parent Chunks
                        ↓
                Child Chunks
                        ↓
                  Embeddings
                        ↓
                     Index
                        ↓
                    Consulta
                        ↓
               Retrieval dos Children
                        ↓
                 Child relevante
                        ↓
                Recupera o Parent
                        ↓
                    Contexto
                        ↓
                       LLM
```

Em implementações mais sofisticadas, vários children podem apontar para o mesmo parent. O sistema também pode recuperar mais de um parent quando diferentes children relevantes pertencem a partes diferentes do documento.

## Um exemplo

Imagine um manual corporativo com uma seção sobre reembolso de viagens.

A estrutura original poderia ser:

```
Manual de Despesas Corporativas

Parent:
Reembolso de viagens

    Child 1:
    Quem pode solicitar reembolso

    Child 2:
    Quais despesas são elegíveis

    Child 3:
    Prazo para solicitação

    Child 4:
    Documentação necessária

    Child 5:
    Exceções
```

O usuário pergunta:

```
"Até quando posso solicitar o reembolso?"
```

Durante o Retrieval, o sistema pode encontrar:

```
Consulta
   ↓
Child 3
"Prazo para solicitação"
   ↓
Parent
"Reembolso de viagens"
```

O Parent fornece o contexto mais amplo:

```
Parent:
Reembolso de viagens

"Os funcionários devem solicitar o reembolso
em até 30 dias após o retorno da viagem.
A solicitação deve conter os comprovantes
das despesas realizadas. Casos excepcionais
devem ser encaminhados ao gestor responsável."
```

A LLM recebe esse contexto e consegue formular uma resposta mais completa:

```
Pergunta
   ↓
Child relevante
   ↓
Parent correspondente
   ↓
Contexto
   ↓
LLM
   ↓
"Você deve solicitar o reembolso em até 30 dias
após o retorno da viagem."
```

A grande vantagem é que o sistema utiliza o **child para localizar** e o **parent para contextualizar**.

## Por que é importante

Parent-child Retrieval é importante porque ajuda a resolver uma das principais dificuldades do Chunking: encontrar o equilíbrio entre **granularidade de busca** e **preservação de contexto**.

Chunks pequenos tendem a ser mais específicos e podem facilitar o Retrieval:

```
Chunk pequeno
   ↓
Mais específico
   ↓
Boa capacidade de localização
```

Porém, podem perder informações necessárias para compreender o trecho.

Chunks grandes preservam mais contexto:

```
Chunk grande
   ↓
Mais contexto
   ↓
Melhor compreensão
```

Mas podem conter informações demais e dificultar a identificação precisa do trecho relevante.

Parent-child Retrieval combina as duas abordagens:

```
Child
↓
Granularidade para Retrieval
        +
Parent
↓
Contexto para a LLM
```

Isso também estabelece uma conexão direta com o conceito de Chunk Size. Em vez de procurar um único tamanho ideal para todos os objetivos, o sistema pode utilizar diferentes tamanhos em diferentes etapas:

```
Documento
    ↓
Parent maior
    ↓
Children menores
    ↓
Embedding dos Children
    ↓
Retrieval
    ↓
Child relevante
    ↓
Parent correspondente
    ↓
Contexto para a LLM
```

Essa estratégia é particularmente útil para documentos estruturados, como manuais, contratos, políticas corporativas e documentação técnica, nos quais um pequeno trecho pode conter a resposta, mas seu significado depende da seção maior à qual pertence.

Portanto, Parent-child Retrieval pode ser entendido como uma forma de separar duas perguntas diferentes dentro do RAG:

```
"Qual parte do documento é relevante?"
        ↓
Child

"Qual contexto devo fornecer para compreender essa parte?"
        ↓
Parent
```

Essa separação permite que o Retrieval seja preciso sem necessariamente sacrificar o contexto necessário para a resposta da LLM.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-parent-child-retrieval/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
