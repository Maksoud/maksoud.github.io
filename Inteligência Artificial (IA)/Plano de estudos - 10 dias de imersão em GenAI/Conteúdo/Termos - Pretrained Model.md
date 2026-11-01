[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Pretrained Model

### 1. O que é

**Pretrained Model**, ou **modelo pré-treinado**, é um modelo de IA que **já passou por uma etapa inicial de treinamento com uma grande quantidade de dados** antes de ser disponibilizado para uso ou para receber um treinamento adicional.

No contexto de LLMs, é o modelo que já aprendeu padrões de linguagem, estruturas, relações entre palavras e outros padrões presentes nos dados utilizados durante o treinamento.

### 2. Como funciona, de forma intuitiva

Imagine que queremos criar um modelo capaz de trabalhar com linguagem.

Primeiro, fornecemos enormes quantidades de textos durante o treinamento. O modelo aprende, por exemplo, que:

> "O Brasil é um país localizado na..."

provavelmente será seguido por algo relacionado à localização geográfica.

Ele não está simplesmente armazenando frases. Durante o treinamento, seus **parâmetros** são ajustados para aprender padrões presentes nos dados.

Ao final dessa etapa, temos um **pretrained model**.

Podemos então utilizá-lo diretamente ou adaptá-lo para uma tarefa específica.

Uma visão simplificada seria:

**Dados → Pré-treinamento → Pretrained Model → Adaptação/uso → Aplicação**

### 3. Um exemplo

Imagine um modelo que foi pré-treinado com uma enorme quantidade de textos.

Esse modelo pode ter conhecimento geral de:

- linguagem
- gramática
- programação
- matemática
- conceitos científicos
- relações entre conceitos

Mas isso não significa que ele esteja necessariamente otimizado para uma tarefa específica.

Podemos então adaptá-lo para, por exemplo, **seguir instruções**, responder perguntas ou atuar como assistente.

É aqui que aparecem conceitos como **fine-tuning** e **instruction tuning**, que são formas de adaptar um modelo pré-treinado.

### 4. Por que é importante

O conceito é importante porque **treinar um LLM do zero é extremamente caro e complexo**.

Em vez de cada empresa precisar criar um modelo desde o início, ela pode partir de um modelo pré-treinado e adaptá-lo às suas necessidades.

Por exemplo:

> **Modelo pré-treinado → fine-tuning → modelo especializado**

ou:

> **Modelo pré-treinado → RAG → aplicação com conhecimento específico**

Isso é uma das razões pelas quais os modelos pré-treinados são tão importantes no ecossistema de IA generativa.

**Distinção essencial:** um _pretrained model_ já passou pelo treinamento inicial, mas isso não significa que esteja pronto para qualquer aplicação ou que tenha sido treinado especificamente para seguir instruções.


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-pretrained-model/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
