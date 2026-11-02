[← Voltar para o Dia 3: Embeddings](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-03-embeddings/)

# Cosine Similarity

## O que é

**Cosine Similarity**, ou **similaridade de cosseno**, é uma medida usada para determinar o quanto dois vetores estão relacionados comparando o **ângulo entre eles**.

Ela é especialmente importante em sistemas que utilizam **embeddings**, porque permite medir a similaridade entre textos representados como vetores.

A ideia principal é simples:

> Quanto mais próximos estiverem os vetores em direção, maior será a similaridade entre eles.

A fórmula é:

$$  
\text{similaridade}(A,B)=\frac{A\cdot B}{|A||B|}  
$$

Onde:
- $A\cdot B$ é o produto escalar entre os dois vetores.
- $|A|$ é o comprimento, ou magnitude, do vetor $A$.
- $|B|$ é o comprimento do vetor $B$.

O resultado normalmente varia entre **-1 e 1**:

```
  1   → mesma direção
  0   → direções ortogonais
 -1   → direções opostas
```

Em aplicações de embeddings de texto, os valores geralmente são interpretados principalmente na região positiva, porque conteúdos semanticamente relacionados tendem a apresentar vetores com direções semelhantes.

## Como funciona

Imagine duas pessoas caminhando em um mapa.

O que importa para a similaridade de cosseno não é apenas a distância entre elas, mas principalmente **a direção em que estão caminhando**.

Se duas pessoas estão caminhando praticamente na mesma direção:

```
Pessoa A ─────────→
Pessoa B ────────→
```

O ângulo entre os vetores é pequeno e a similaridade de cosseno é alta.

Se elas caminham em direções muito diferentes:

```
Pessoa A ───────→

             ↗
          Pessoa B
```

O ângulo aumenta e a similaridade diminui.

Isso é particularmente útil para embeddings porque dois textos podem possuir vetores com **magnitudes diferentes**, mas ainda assim apontar para direções semelhantes.

A similaridade de cosseno se concentra justamente nessa orientação.

## Um exemplo

Considere dois textos:

```
A:
"Como solicitar férias?"

B:
"Qual é o procedimento para marcar férias?"
```

Depois de passar pelo modelo de embeddings, podemos obter vetores simplificados:

```
A = [0.8, 0.6]

B = [0.9, 0.7]
```

Primeiro calculamos o produto escalar:

$$  
A\cdot B=(0.8\times0.9)+(0.6\times0.7)  
$$

$$  
A\cdot B=1.14  
$$

Depois calculamos as magnitudes:

$$  
|A|=\sqrt{0.8^2+0.6^2}  
$$

$$  
|B|=\sqrt{0.9^2+0.7^2}  
$$

Aplicando esses valores à fórmula, obtemos uma similaridade próxima de **1**, indicando que os vetores apontam para direções muito semelhantes.

Em um sistema RAG, o processo seria:

```
Pergunta do usuário
        ↓
Embedding
        ↓
Vetor da pergunta
        ↓
Cosine Similarity
        ↓
Comparação com vetores dos documentos
        ↓
Documentos mais semelhantes
        ↓
Contexto
        ↓
LLM
```

Assim, se a pergunta for:

```
"Como marcar minhas férias?"
```

o sistema pode encontrar um documento que diga:

```
"Procedimento para solicitação do período de férias."
```

Mesmo que as palavras não sejam exatamente iguais, os embeddings podem posicionar os dois conteúdos em regiões próximas do espaço vetorial.

## Por que é importante

Cosine Similarity é importante porque fornece uma maneira matemática de comparar embeddings e, consequentemente, de medir a **proximidade semântica entre conteúdos**.

Ela aparece em várias aplicações:
- **RAG:** encontrar documentos relevantes para uma pergunta;
- **busca semântica:** recuperar conteúdos relacionados;
- **recomendação:** identificar itens semelhantes;
- **agrupamento:** encontrar conteúdos próximos;
- **detecção de duplicidade:** identificar textos semanticamente parecidos.

A relação com os conceitos anteriores fica mais clara quando colocamos tudo em sequência:

```
Texto
  ↓
Embedding Model
  ↓
Vector Embedding
  ↓
Cosine Similarity
  ↓
Comparação entre vetores
  ↓
Semantic Similarity
  ↓
Recuperação de informação
```

Existe uma distinção importante aqui.

**Semantic Similarity** é o conceito que queremos medir: o grau de relação semântica entre dois conteúdos.

**Cosine Similarity** é uma das técnicas matemáticas utilizadas para realizar essa comparação quando os conteúdos são representados como vetores.

Podemos resumir:

```
Semantic Similarity
"O quanto esses conteúdos são semelhantes?"

Cosine Similarity
"Como podemos calcular essa proximidade entre
seus vetores?"
```

Também é importante não interpretar o valor de similaridade como uma **probabilidade de que dois textos sejam equivalentes**.

Uma similaridade alta significa que os vetores estão próximos segundo aquela representação e aquela métrica. Isso não garante que os conteúdos sejam idênticos, corretos ou intercambiáveis.

Por isso, em um sistema RAG, a similaridade de cosseno normalmente funciona como **um mecanismo de recuperação**, e não como uma prova de que determinado documento contém a resposta correta.

Em resumo:

> **Cosine Similarity mede a proximidade entre dois vetores observando principalmente o ângulo entre eles. Em sistemas de embeddings, ela permite comparar conteúdos semanticamente relacionados e é uma das técnicas fundamentais para busca vetorial e RAG.**

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/embeddings-cosine-similarity/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
