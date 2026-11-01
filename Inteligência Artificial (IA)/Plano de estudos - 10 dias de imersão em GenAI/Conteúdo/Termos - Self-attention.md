[← Voltar para o Dia 1: LLMs de verdade](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-01-llms-de-verdade/)

# Self-attention

## O que é?

**Self-Attention** é um mecanismo pelo qual cada [token](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-token/) de uma sequência pode **analisar a relação com os outros tokens da própria sequência**.

O termo _self_ vem justamente daí. A atenção acontece dentro da própria sequência.

O conceito foi central na arquitetura [Transformer](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-transformer/) apresentada no artigo _Attention Is All You Need_, de 2017. [Google Pesquisa](https://research.google/pubs/attention-is-all-you-need/?utm_source=chatgpt.com)

## Como funciona?

Imagine:

> "O cachorro perseguiu o gato porque ele estava assustado."

Para interpretar **"ele"**, o modelo precisa avaliar quais outros tokens da frase têm relação com ele.

O Self-Attention permite fazer isso:

```
"ele"
  ↓
analisa os demais tokens
  ↓
cachorro  → relação forte
gato      → relação menor
porque    → relação menor
estava    → relação menor
```

Os valores de atenção são calculados matematicamente. O resultado é uma nova representação do token que incorpora informações relevantes do restante da sequência.

Uma característica importante é que isso permite capturar relações entre tokens que estão **distantes entre si**. [Attention Is All You Need](https://attentionisallyouneed.uk/?utm_source=chatgpt.com)

## Um exemplo simples

Considere:

> "O banco aprovou o empréstimo porque precisava avaliar o risco."

Quando o modelo processa **"banco"**, ele pode estabelecer relações com palavras como:

```
banco
 ↓
empréstimo
 ↓
avaliar
 ↓
risco
```

Essas relações ajudam a construir uma representação contextual de "banco" associada ao contexto financeiro.

Se a frase fosse:

> "Sentei no banco da praça."

as relações seriam diferentes:

```
banco
 ↓
sentei
 ↓
praça
```

Portanto, o significado representado pelo modelo depende do contexto.

## Por que é importante?

O Self-Attention é uma das principais características que tornam o Transformer tão eficiente para trabalhar com linguagem. A arquitetura consegue relacionar diferentes posições de uma sequência diretamente, em vez de depender de um processamento necessariamente sequencial como nas arquiteturas recorrentes anteriores. [Google Pesquisa](https://research.google/pubs/attention-is-all-you-need/?utm_source=chatgpt.com)

Uma forma boa de guardar:

> **[Attention](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-attention/) é o mecanismo de atenção. Self-Attention é quando essa atenção relaciona os elementos dentro da própria sequência.**

E um detalhe que será útil quando chegarmos aos próximos conceitos: **Self-Attention utiliza as chamadas Query, Key e Value para calcular essas relações**. 

---
### Complemento: Query, Key e Value no Self-Attention

O que define o Self-Attention é que **Query, Key e Value saem da mesma sequência**. Cada token gera os três ao mesmo tempo:
- **Query (Q)**: o que este token precisa entender a partir do resto da frase.
- **Key (K)**: como este token se apresenta para os outros tokens.
- **Value (V)**: o que este token tem a contribuir se for considerado relevante.

Assim, cada token faz uma pergunta para todos os outros (e para si mesmo) da própria frase. Veja um exemplo:

> "O gato subiu no telhado porque **ele** estava com medo."

```
Query de "ele"
"A quem eu me refiro?"

        ↓

Keys da mesma frase
"O" → artigo
"gato" → animal, sujeito
"telhado" → lugar
"medo" → sentimento

        ↓

Comparação
"gato" combina muito, "telhado" pouco

        ↓

Values
A nova representação de "ele" recebe principalmente a informação de "gato"
```

E isso acontece **para todos os tokens ao mesmo tempo**: "subiu" também consulta a frase e descobre que quem subiu foi o gato, "medo" se relaciona com "ele", e assim por diante. No final, cada token deixa de ter um significado isolado e passa a carregar o contexto da frase inteira.

Em modelos que geram texto, como o GPT, existe uma restrição extra: cada token só pode consultar os tokens **anteriores** a ele, nunca os futuros (isso se chama **Masked** ou **Causal Self-Attention**). Afinal, o modelo não pode "espiar" a palavra que ainda vai prever.

Você não precisa decorar as fórmulas agora. Para o seu material, basta guardar:

> **Self-Attention permite que cada token considere os outros tokens da sequência, enquanto Query, Key e Value são as representações usadas para calcular e aplicar essas relações.**


[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-self-attention/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
