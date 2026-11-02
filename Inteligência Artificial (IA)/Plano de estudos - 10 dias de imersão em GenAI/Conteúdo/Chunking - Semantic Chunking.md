[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# Semantic Chunking

## O que é

**Semantic Chunking** é uma estratégia de divisão de documentos que busca criar chunks com base no **significado do conteúdo**, em vez de utilizar apenas um tamanho fixo ou separadores estruturais.

A ideia é manter juntas as frases que tratam da mesma ideia e separar aquelas em que ocorre uma mudança significativa de assunto.

Por isso, um chunk pode ter tamanhos diferentes:

```
Chunk 1
→ apresenta a política de férias

Chunk 2
→ explica como solicitar férias

Chunk 3
→ explica o processo de aprovação
```

O objetivo é fazer com que cada chunk represente uma unidade de conhecimento relativamente coerente.

## Como funciona

Imagine o seguinte texto:

```
A empresa permite que funcionários tirem até 30 dias
de férias por período aquisitivo.

A solicitação deve ser realizada pelo sistema interno
com pelo menos 30 dias de antecedência.

O gestor deve analisar a solicitação e aprová-la pelo
mesmo sistema.

Em casos de afastamento médico, devem ser apresentados
os documentos necessários ao departamento de Recursos Humanos.
```

Uma estratégia baseada apenas em tamanho poderia dividir o texto em posições arbitrárias.

O Semantic Chunking tenta identificar mudanças de assunto:

```
Chunk 1
"A empresa permite que funcionários tirem até 30 dias
de férias por período aquisitivo."

          ↓ mudança de assunto

Chunk 2
"A solicitação deve ser realizada pelo sistema interno
com pelo menos 30 dias de antecedência.

O gestor deve analisar a solicitação e aprová-la pelo
mesmo sistema."

          ↓ mudança de assunto

Chunk 3
"Em casos de afastamento médico, devem ser apresentados
os documentos necessários ao departamento de Recursos Humanos."
```

Uma forma comum de fazer isso é comparar semanticamente frases ou grupos de frases usando embeddings.

Se duas partes do texto forem semanticamente próximas, elas podem permanecer no mesmo chunk. Quando a similaridade entre partes consecutivas diminui significativamente, isso pode indicar uma mudança de assunto e um possível ponto de divisão.

```
Frase 1 ── similar ── Frase 2 ── similar ── Frase 3
                                           │
                                  mudança semântica
                                           ↓
                                      Frase 4
```

Assim, o sistema não pergunta apenas **"quantos tokens existem aqui?"**, mas também **"essas partes ainda estão falando sobre a mesma coisa?"**.

## Um exemplo

Considere um documento sobre uma empresa:

```
A empresa oferece plano de saúde aos funcionários.
O benefício pode ser utilizado após o período de carência.

Para solicitar férias, o funcionário deve acessar
o sistema interno e enviar a solicitação ao gestor.

O gestor possui até cinco dias úteis para analisar
o pedido e registrar sua aprovação.
```

Um Fixed-size Chunking poderia dividir o texto independentemente dos assuntos.

O Semantic Chunking pode identificar três grupos conceituais:

```
Chunk 1:
"A empresa oferece plano de saúde aos funcionários.
O benefício pode ser utilizado após o período de carência."

Chunk 2:
"Para solicitar férias, o funcionário deve acessar
o sistema interno e enviar a solicitação ao gestor.

O gestor possui até cinco dias úteis para analisar
o pedido e registrar sua aprovação."
```

Nesse caso, a primeira parte trata de **plano de saúde**, enquanto a segunda trata de **férias**. Manter cada assunto em um chunk tende a produzir unidades mais coerentes para recuperação.

Por exemplo, diante da pergunta:

> "Quanto tempo o gestor tem para aprovar minhas férias?"

o sistema pode recuperar o segundo chunk, que contém o contexto necessário para responder.

## Por que é importante

Semantic Chunking é importante porque o chunking influencia diretamente a qualidade do **retrieval** em RAG.

Quando os chunks preservam melhor as unidades de significado, aumenta a possibilidade de que a recuperação traga um trecho que contenha não apenas a palavra relacionada à pergunta, mas também o contexto necessário para interpretá-la.

Isso pode ser especialmente útil em documentos longos e complexos, nos quais uma mudança de assunto não coincide necessariamente com uma quantidade fixa de tokens ou com uma estrutura explícita.

A principal vantagem é:

```
Documento
   ↓
Identificação de mudanças semânticas
   ↓
Chunks semanticamente coerentes
   ↓
Embeddings
   ↓
Vector Search
   ↓
Contexto mais relevante
```

Porém, existe um custo. Para determinar a relação semântica entre partes do texto, o processo pode exigir embeddings e processamento adicional durante a ingestão. Além disso, a definição de um ponto de corte semântico pode envolver heurísticas e parâmetros.

Também é importante não confundir Semantic Chunking com Recursive Chunking:

```
Fixed-size Chunking
→ divide principalmente pelo tamanho

Recursive Chunking
→ usa uma hierarquia de separadores para preservar estrutura

Semantic Chunking
→ usa relações de significado para determinar as divisões
```

Na prática, essas estratégias podem até ser combinadas. Um sistema pode usar critérios semânticos para encontrar pontos naturais de divisão e, ao mesmo tempo, impor um tamanho máximo para evitar chunks excessivamente grandes.

O ponto central é: **Semantic Chunking busca transformar um documento em unidades de significado coerentes, fazendo com que as fronteiras entre chunks acompanhem mudanças de assunto em vez de depender apenas do tamanho do texto.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/chunking-semantic-chunking/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
