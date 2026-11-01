[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Inference

### 1. O que é?

**Inference (inferência)** é o processo de **usar um modelo já treinado para produzir uma saída a partir de uma entrada**.

No contexto de LLMs, é o momento em que você faz uma pergunta e o modelo gera uma resposta.

A distinção fundamental é:

> **Training ensina o modelo. Inference utiliza o que ele aprendeu.**

### 2. Como funciona?

De forma simplificada:

```
Seu prompt
    ↓
Tokenização
    ↓
Tokens
    ↓
LLM já treinado
    ↓
Processamento pelo Transformer
    ↓
Previsão do próximo token
    ↓
Próximo token
    ↓
Próximo token
    ↓
...
    ↓
Resposta
```

O modelo utiliza os **parâmetros aprendidos durante o treinamento** para calcular quais tokens são mais prováveis de aparecer em seguida.

Por exemplo:

```
"Paris é a capital da"
              ↓
          previsão
              ↓
          "França"
```

Depois de gerar "França", o modelo pode continuar a sequência, dependendo do que foi solicitado.

### 3. Um exemplo simples

Imagine que você tenha um modelo treinado.

Durante o treinamento:

```
Milhões/bilhões de exemplos
          ↓
       Training
          ↓
Parâmetros ajustados
```

Depois, você pergunta:

> "Explique o que é RAG."

Isso é **inference**:

```
Pergunta
   ↓
Modelo treinado
   ↓
Processamento
   ↓
Resposta
```

O modelo **não está sendo treinado novamente** enquanto responde.

### 4. Por que é importante?

Porque inference é a etapa que efetivamente **consome o modelo em produção**.

Isso traz questões práticas como:

- **Latência**: Quanto tempo o modelo leva para responder?
- **Custo**: Quanto processamento é necessário para gerar a resposta?
- **Throughput**: Quantas requisições o sistema consegue processar?
- **Memória**: Quanto espaço é necessário para carregar o modelo e executar seus cálculos?

Essas questões são especialmente importantes quando colocamos LLMs em aplicações reais.

### Para guardar

> **Inference é a execução de um modelo treinado para transformar uma entrada em uma saída.**

A relação com o conceito anterior fica:

```
Training
   ↓
aprende os parâmetros
   ↓
Modelo treinado
   ↓
Inference
   ↓
usa os parâmetros
   ↓
gera a resposta
```

E isso também explica por que **inference** e **inference strategies** são conceitos relacionados, mas diferentes. _Inference_ é o processo de executar o modelo. _Inference strategy_ trata de **como essa execução e geração são conduzidas**.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-inference/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
