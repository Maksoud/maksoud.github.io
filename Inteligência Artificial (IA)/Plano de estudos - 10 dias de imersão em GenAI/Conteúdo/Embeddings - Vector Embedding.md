[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Vector Embedding

## O que é

**Vector Embedding** é a representação de uma informação, como um texto, em um **vetor numérico** que captura características semânticas relevantes daquele conteúdo.

Na prática, os termos **embedding** e **vector embedding** são frequentemente usados como sinônimos. A expressão "vector embedding" apenas deixa explícito que o resultado de um modelo de embedding é um **vetor**.

Por exemplo, uma frase pode ser transformada em algo semelhante a:

```
"Como solicitar férias?"
        ↓
[0.21, -0.34, 0.72, 0.15, ...]
```

Esse vetor pode possuir centenas ou milhares de dimensões. Cada número representa uma coordenada em um espaço matemático, mas normalmente não existe uma interpretação humana simples para cada dimensão individual.

O que importa é a **posição do vetor em relação aos outros vetores**.

## Como funciona, de forma intuitiva

Imagine um enorme mapa no qual cada conteúdo recebe uma posição.

Conteúdos semanticamente semelhantes tendem a ocupar regiões próximas:

```
             "Como tirar férias?"
                    ●
                  ●
       "Como solicitar férias?"
                ●
      "Qual o procedimento para férias?"
```

Já conteúdos semanticamente diferentes tendem a ficar em regiões mais distantes:

```
"Como tirar férias?" ●


                         ● "Receita de bolo"
```

O modelo de embedding transforma o conteúdo original em coordenadas nesse espaço.

Por isso, quando fazemos uma busca semântica, podemos transformar tanto a pergunta quanto os documentos em vetores e comparar suas posições.

Uma das medidas mais utilizadas para isso é a **similaridade de cosseno**:

$$  
\text{similaridade}(A,B)=\frac{A\cdot B}{|A||B|}  
$$

De forma intuitiva:

```
Maior similaridade
        ↓
Vetores semanticamente mais próximos

Menor similaridade
        ↓
Vetores semanticamente menos relacionados
```

Isso permite encontrar conteúdos relacionados mesmo quando eles não utilizam exatamente as mesmas palavras.

## Um exemplo

Imagine uma base de conhecimento de uma empresa contendo este documento:

```
Para solicitar férias, o funcionário deve realizar
a solicitação pelo sistema interno com antecedência
mínima de 30 dias.
```

O usuário faz a pergunta:

```
Como faço para marcar minhas férias?
```

O sistema transforma a pergunta em um vector embedding:

```
Pergunta
   ↓
Embedding Model
   ↓
Vetor da pergunta
```

Os documentos da base já possuem seus próprios vetores:

```
Documento A → [0.21, -0.13, 0.74, ...]
Documento B → [0.67,  0.42, -0.18, ...]
Documento C → [0.19, -0.11, 0.71, ...]
```

O sistema compara o vetor da pergunta com os vetores dos documentos.

O Documento A ou C pode apresentar maior similaridade, mesmo que o usuário tenha utilizado "marcar minhas férias" e o documento utilize "solicitar férias".

O texto relevante é então recuperado e enviado ao LLM para gerar a resposta.

Esse processo é uma das bases da **busca vetorial**, muito utilizada em sistemas RAG.

## Por que é importante

Vector Embeddings são importantes porque transformam informações originalmente difíceis de comparar matematicamente, especialmente linguagem natural, em representações que permitem realizar operações como:
- calcular similaridade;
- encontrar conteúdos relacionados;
- realizar busca semântica;
- agrupar conteúdos semelhantes;
- alimentar sistemas de recomendação;
- recuperar informações para sistemas RAG.

A relação entre os conceitos que estamos estudando pode ser vista assim:

```
Texto
  ↓
Embedding Model
  ↓
Vector Embedding
  ↓
Vector Database
  ↓
Busca por similaridade
  ↓
Trechos relevantes
  ↓
Contexto
  ↓
LLM
```

Aqui aparece uma distinção importante entre **Embedding** e **Vector Embedding**.

Na prática, os termos são frequentemente utilizados para representar a mesma ideia:

> **Embedding** é a representação gerada pelo modelo.

> **Vector Embedding** enfatiza que essa representação é um vetor numérico.

Essa distinção será útil porque, ao avançarmos para **Vector Database**, veremos que o banco não armazena apenas "textos semelhantes". Ele armazena vetores e utiliza algoritmos especializados para encontrar rapidamente os vetores mais próximos de uma consulta.

Assim, o Vector Embedding funciona como uma espécie de **endereço semântico** de um conteúdo dentro de um espaço vetorial.

Quanto mais adequadamente esse espaço representar as relações de significado relevantes para a aplicação, mais útil será a busca baseada em similaridade.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-vector-embedding/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
