[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Metadata Filtering

## O que é

**Metadata Filtering** é o uso dos **metadados associados aos chunks** para restringir quais informações podem ser consideradas durante o Retrieval.

Enquanto a busca vetorial pergunta:

```
"Quais conteúdos são semanticamente semelhantes à minha pergunta?"
```

o Metadata Filtering pode acrescentar:

```
"Quais conteúdos podem ser considerados antes mesmo de avaliar a similaridade?"
```

Os metadados podem representar características como:

```
documento
página
seção
categoria
autor
departamento
idioma
data
versão
permissão de acesso
```

Por exemplo, um chunk pode possuir:

```
Conteúdo:
"Funcionários devem solicitar férias com 30 dias de antecedência."

Metadata:
{
  "documento": "politica_ferias.pdf",
  "departamento": "RH",
  "ano": 2026,
  "idioma": "pt-BR"
}
```

O filtro permite selecionar apenas chunks que atendam a determinadas condições.

## Como funciona

Imagine uma base com políticas de uma empresa de vários anos:

```
Política de férias 2024
Política de férias 2025
Política de férias 2026
Política de benefícios 2026
Política de viagens 2026
```

O usuário pergunta:

```
"Qual é a política de férias vigente em 2026?"
```

Uma busca puramente semântica poderia encontrar documentos de 2024, 2025 e 2026, porque todos tratam de férias.

Podemos utilizar metadata filtering para restringir a busca:

```
Filtro:
categoria = "férias"
ano = 2026
```

Somente depois disso o sistema realiza a busca entre os documentos permitidos:

```
Base de conhecimento
        ↓
Metadata Filtering
        ↓
Documentos de férias de 2026
        ↓
Busca semântica
        ↓
Resultados relevantes
        ↓
LLM
```

Em algumas arquiteturas, o filtro pode ser aplicado antes ou durante a busca vetorial, dependendo da tecnologia utilizada e de como os índices foram configurados.

O ponto principal é que o filtro atua como uma **restrição estruturada**, enquanto a busca vetorial atua como um **critério de relevância semântica**.

Isso permite combinar os dois:

```
Consulta
   ↓
┌──────────────────────────────┐
│ Metadata Filtering            │
│ ano = 2026                   │
│ departamento = RH            │
└──────────────┬───────────────┘
               ↓
       Conjunto permitido
               ↓
      Vector / Keyword Search
               ↓
         Top-K resultados
               ↓
              LLM
```

## Um exemplo

Imagine que uma empresa tenha documentos de diferentes departamentos e anos.

Cada chunk possui metadados:

```
Chunk 1
departamento = RH
ano = 2025
categoria = férias

Chunk 2
departamento = RH
ano = 2026
categoria = férias

Chunk 3
departamento = Financeiro
ano = 2026
categoria = reembolso

Chunk 4
departamento = RH
ano = 2026
categoria = benefícios
```

O usuário pergunta:

```
"Quantos dias de antecedência preciso para solicitar férias?"
```

Sem filtro, o sistema poderia pesquisar em todos os chunks.

Com Metadata Filtering:

```
departamento = RH
categoria = férias
ano = 2026
```

A busca fica restrita ao Chunk 2.

Depois, a similaridade semântica determina se aquele chunk realmente responde à pergunta.

O resultado é:

```
Metadata Filter
      ↓
Candidatos relevantes
      ↓
Semantic Search
      ↓
Melhores chunks
      ↓
LLM
```

Esse mecanismo também pode ser usado para **controle de acesso**.

Por exemplo:

```
usuário = funcionário
departamento = Financeiro
```

O sistema poderia restringir a busca aos documentos que aquele usuário tem permissão para consultar.

Nesse caso, o Metadata Filtering deixa de ser apenas uma otimização de busca e passa a participar da **segurança do sistema**.

Ainda assim, filtros de metadados não devem ser considerados, sozinhos, um mecanismo completo de autorização. O controle de acesso precisa estar corretamente implementado na aplicação e na infraestrutura.

## Por que é importante

Metadata Filtering é importante porque permite combinar **relevância semântica com restrições estruturadas**.

A diferença pode ser resumida assim:

|Mecanismo|Pergunta que responde|
|---|---|
|Sparse Retrieval|"Quais conteúdos contêm termos relevantes?"|
|Dense Retrieval|"Quais conteúdos possuem significado semelhante?"|
|Metadata Filtering|"Quais conteúdos podem participar da busca?"|
|Hybrid Search|"Como combinar diferentes sinais de busca?"|

Isso é especialmente útil quando a base contém muitos documentos semelhantes.

Por exemplo, uma pergunta sobre:

```
"política de férias"
```

pode encontrar dezenas de documentos semanticamente relacionados.

Mas se sabemos que precisamos de:

```
ano = 2026
departamento = RH
idioma = pt-BR
```

podemos eliminar grande parte dos candidatos antes ou durante a busca.

Em sistemas RAG, isso pode trazer três benefícios importantes:

**Precisão:** reduz resultados semanticamente parecidos, mas inadequados.

**Eficiência:** diminui o conjunto de informações que precisa ser pesquisado.

**Controle:** permite restringir resultados por características estruturadas, como data, categoria, departamento ou versão.

Podemos visualizar a combinação com os conceitos estudados:

```
                 Pergunta
                    ↓
          Metadata Filtering
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
  Dense Retrieval      Sparse Retrieval
          └─────────┬─────────┘
                    ↓
              Ranking / Top-K
                    ↓
                 Contexto
                    ↓
                   LLM
```

A ideia central é: **Metadata Filtering utiliza informações estruturadas associadas aos chunks para restringir e orientar o Retrieval, permitindo combinar filtros objetivos com busca por relevância.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/retrieval-metadata-filtering/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
