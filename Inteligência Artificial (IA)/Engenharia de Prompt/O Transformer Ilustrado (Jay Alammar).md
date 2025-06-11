### [Sumário](<https://maksoud.github.io/Sumário>)

# 🧠 **Resumo: O Transformer Ilustrado (Jay Alammar)**

🔗 [Artigo original](https://jalammar.github.io/illustrated-transformer/)

### 🔹 **O que é o Transformer?**

O **Transformer** é uma arquitetura de rede neural introduzida no artigo _“Attention is All You Need”_ (2017), que revolucionou o campo do Processamento de Linguagem Natural (NLP). Diferente de modelos anteriores, como RNNs e LSTMs, ele não depende de processamento sequencial – permitindo **paralelismo, maior velocidade e melhor desempenho em tarefas linguísticas.**

### 🔹 **Principais Componentes do Transformer**

#### 1. **Embedding**

As palavras são convertidas em vetores (números) para que possam ser entendidas pelo modelo.  
➡ Exemplo: “gato” → `[0.12, -0.34, ...]`

#### 2. **Positional Encoding**

Como o Transformer processa tudo ao mesmo tempo (não em sequência), ele precisa saber **a posição de cada palavra na frase**. Isso é feito com _codificações posicionais_ que são somadas ao embedding.

#### 3. **Atenção (Attention)**

O coração do Transformer. A ideia é:  
**"Para cada palavra, qual é a importância das outras palavras no contexto?"**

A fórmula de atenção básica:

```
Attention(Q, K, V) = softmax(Q × Kᵗ / √dₖ) × V
```

Onde:

- **Q (Query)**: O que estamos procurando
- **K (Key)**: As palavras disponíveis
- **V (Value)**: A informação a ser usada

Essa técnica permite que o modelo **"preste atenção" em partes relevantes da frase** ao tomar decisões.

#### 4. **Multi-Head Attention**

O modelo usa múltiplas "cabeças de atenção" que analisam diferentes partes da frase de maneira paralela e combinam os resultados.

#### 5. **Feed Forward Layer**

Após a atenção, os dados passam por uma rede neural tradicional para mais processamento.

#### 6. **Camadas e Normalização**

Cada etapa tem uma **normalização** (layer norm) e uma **conexão residual** (skip connection), ajudando no aprendizado e estabilidade.

### 🔹 **Arquitetura Geral**

O Transformer completo é formado por dois blocos principais:

- **Codificador (Encoder)**: Lê o texto de entrada
- **Decodificador (Decoder)**: Gera o texto de saída

No caso do GPT, **apenas o decodificador é usado**, pois ele é treinado para prever a próxima palavra.

### 🔹 **Aplicações**

O Transformer é a base de modelos como:

- **BERT** (usa só o encoder)
- **GPT-2 / GPT-3 / GPT-4** (usam só o decoder)
- **T5, BART** (usam encoder + decoder)


### 🧠 **Conceitos Fundamentais Aprendidos**

- A arquitetura Transformer é baseada em atenção, não em sequência
- O modelo aprende a focar em palavras relevantes no contexto
- Permite paralelismo, o que acelera o treinamento
- É altamente escalável e adaptável a várias tarefas de linguagem
