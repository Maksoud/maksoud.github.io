### Sumário

# **Como Funcionam os Modelos de Linguagem (LLMs)**

### **Objetivo de Aprendizado**

Compreender os conceitos fundamentais por trás de modelos como o GPT, como eles aprendem, operam e geram texto. Isso inclui:

- Tokens e embeddings
- Arquitetura Transformer
- Ajuste fino (fine-tuning) vs. engenharia de prompt
- Limitações e vantagens

## **O Que São LLMs?**

Modelos de Linguagem de Grande Escala (LLMs) como GPT-4, Claude e Gemini são algoritmos baseados em **redes neurais profundas** treinados com grandes volumes de texto. Eles **predizem a próxima palavra** em uma sequência, entendendo padrões e contextos.

## 📌 **Conteúdo de Estudo Recomendado**

### 1. **Artigos Técnicos (leitura fundamental)**

- [🔗 The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) – Visual e intuitivo ([Resumo](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/1-fundamentos-da-engenharia-de-prompt/o-transformer-ilustrado-jay-alammar/))
- [🔗 Como funciona o ChatGPT – OpenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/1-fundamentos-da-engenharia-de-prompt/como-funciona-o-chatgpt-openai/)
- [🔗 Understanding LLMs – Sebastian Raschka (GitHub)](https://sebastianraschka.com/blog/2023/llm-overview.html)

### 2. **Vídeos Explicativos**

- [📺 How ChatGPT Actually Works – Fireship (YouTube)](https://www.youtube.com/watch?v=JTxsNm9IdYU)  
    _Explicação simples e direta em 5 minutos._
- [📺 Transformers - State of the Art NLP](https://www.youtube.com/watch?v=U0s0f995w14) – Yannic Kilcher

### 3. **Conceitos-chave a entender**

|Conceito|Descrição curta|
|---|---|
|**Token**|Fragmento de texto (palavra, sílaba ou letra) que o modelo processa|
|**Embedding**|Representação vetorial de palavras em um espaço semântico|
|**Transformer**|Arquitetura usada nos LLMs baseada em _atenção_ para entender contexto|
|**Self-Attention**|Técnica que permite o modelo dar "peso" diferente para palavras no contexto|
|**Pretraining**|Fase em que o modelo aprende com bilhões de textos|
|**Fine-tuning**|Ajustes finais com dados específicos (ex: ChatGPT para diálogo)|
|**Inference**|Processo de gerar texto com base em um prompt|

### 4. **Exercício prático sugerido**

**Tarefa:** Responder com suas palavras:

> “Como um modelo como o GPT-4 gera uma resposta a partir de um prompt?”  
> **Dica:** Use as palavras: _tokens_, _contexto_, _atenção_, _probabilidade_ e _geração de texto_.

### 5. **Ferramentas úteis**

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer) – Para ver como o modelo divide textos
- [Google Colab – Transformer em Python](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/language_modeling.ipynb) – Para quem quiser ir além

## ✅ **Checklist de Conclusão**

-  Li e compreendi o funcionamento de tokens e embeddings
-  Sei explicar como funciona a arquitetura Transformer
-  Sei a diferença entre pretraining, fine-tuning e prompting
-  Fiz um resumo pessoal ou artigo explicativo
-  Testei o Tokenizer da OpenAI com textos diferentes


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/1-fundamentos-da-engenharia-de-prompt/como-funcionam-os-modelos-de-linguagem-llms/)

<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>