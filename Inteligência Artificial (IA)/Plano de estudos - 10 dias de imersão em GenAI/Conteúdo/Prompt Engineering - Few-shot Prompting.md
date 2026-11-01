[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Few-shot Prompting

## O que é

**Few-shot prompting** é uma técnica de engenharia de prompts na qual fornecemos ao modelo **alguns exemplos da tarefa antes de pedir que ele processe uma nova entrada**.

Diferentemente do [zero-shot prompting](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-zero-shot-prompting/), que apresenta somente a instrução, o few-shot mostra ao modelo exemplos de **entrada e saída esperada**. Esses exemplos ajudam o modelo a identificar o padrão que deve seguir.

O termo _few-shot_ significa literalmente "poucos exemplos".

## Como funciona

Imagine que você queira ensinar alguém a classificar frases como positivas ou negativas. Em vez de apenas dizer "classifique esta frase", você poderia mostrar:

```
"Esse produto é excelente." → Positivo
"O atendimento foi péssimo." → Negativo
"Gostei muito da experiência." → Positivo
```

Depois, apresenta uma nova frase:

```
"O produto chegou rapidamente e superou minhas expectativas."
```

A pessoa consegue perceber o padrão e classificá-la como **Positivo**.

Com um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), o princípio é semelhante. Os exemplos funcionam como uma espécie de **demonstração do comportamento desejado**.

O modelo não está necessariamente "aprendendo" esses exemplos como faria durante o treinamento. Ele está usando as informações presentes no próprio prompt para inferir o padrão que deve aplicar à nova entrada.

## Um exemplo

Suponha que queremos transformar frases em uma estrutura padronizada.

Um prompt few-shot poderia ser:

```
Extraia o produto e o sentimento de cada frase.

Exemplo 1:
Frase: "O notebook é excelente."
Produto: notebook
Sentimento: positivo

Exemplo 2:
Frase: "O celular apresentou muitos problemas."
Produto: celular
Sentimento: negativo

Agora processe:
Frase: "O tablet tem uma tela fantástica."
```

O modelo pode produzir:

```
Produto: tablet
Sentimento: positivo
```

Observe que os exemplos não são apenas informações adicionais. Eles **demonstram como a tarefa deve ser executada e como a resposta deve ser estruturada**.

Isso é particularmente útil quando a instrução sozinha não deixa suficientemente claro o comportamento esperado.

## Por que é importante

Few-shot prompting é importante porque permite **orientar o comportamento do modelo sem precisar alterar ou treinar novamente o modelo**.

Ele é especialmente útil quando:
1. A tarefa possui regras específicas.
2. O formato da resposta precisa ser consistente.
3. A instrução em linguagem natural pode gerar interpretações diferentes.
4. Queremos demonstrar um padrão que seria difícil explicar apenas com palavras.
5. Precisamos adaptar um modelo geral para uma tarefa mais específica.

Uma vantagem importante é que os exemplos podem ensinar **padrões**, não apenas conteúdo. Podemos demonstrar como classificar, resumir, extrair informações, transformar textos ou estruturar respostas.

Por outro lado, existe um custo: **cada exemplo ocupa espaço na [Context Window](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-context-window/) e aumenta a quantidade de [tokens](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) processados**. Por isso, adicionar muitos exemplos nem sempre é melhor.

**Em uma frase:** few-shot prompting é **ensinar ao modelo o comportamento esperado por meio de alguns exemplos incluídos no próprio prompt**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-few-shot-prompting/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
