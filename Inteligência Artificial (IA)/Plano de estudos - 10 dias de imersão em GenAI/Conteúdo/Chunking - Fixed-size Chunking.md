# Fixed-size Chunking
## O que é

**Fixed-size Chunking** é uma estratégia de chunking em que o conteúdo é dividido em partes com tamanho predefinido.

Em vez de tentar identificar semanticamente onde uma ideia começa ou termina, o sistema estabelece um limite, como determinado número de caracteres ou tokens, e divide o documento de acordo com esse tamanho.

Por exemplo, um documento poderia ser dividido em chunks de 500 tokens:

```
Documento
   ↓
┌─────────────────────┐
│ Chunk 1             │
│ 0 a 500 tokens      │
└─────────────────────┘
          ↓
┌─────────────────────┐
│ Chunk 2             │
│ 501 a 1000 tokens  │
└─────────────────────┘
          ↓
┌─────────────────────┐
│ Chunk 3             │
│ 1001 a 1500 tokens │
└─────────────────────┘
```

É uma das formas mais simples de implementar chunking e pode ser útil quando não existe uma estrutura clara no conteúdo ou quando se deseja uma estratégia previsível.

## Como funciona

Imagine cortar uma fita métrica em pedaços de exatamente 50 centímetros.

Você não verifica o que existe em cada trecho. Apenas aplica uma regra de tamanho:

```
Documento
──────────────────────────────────────────────→

|-------- 500 tokens --------|
                              |-------- 500 tokens --------|
                                                            |-------- 500 tokens --------|
```

O mesmo princípio pode ser aplicado ao texto.

O tamanho pode ser definido em:
- caracteres;
- palavras;
- tokens.

Em sistemas de RAG, tokens são especialmente relevantes porque o LLM trabalha com tokens e possui limites de contexto baseados neles.

Uma estratégia de **Fixed-size Chunking** também pode utilizar **overlap**, fazendo com que parte de um chunk seja repetida no seguinte:

```
Chunk 1: [1 2 3 4 5 6 7 8]
Chunk 2:             [7 8 9 10 11 12 13 14]
                         ↑
                       overlap
```

Isso ajuda a preservar contexto quando uma informação importante está próxima da fronteira entre dois chunks.

## Um exemplo

Considere um documento sobre uma política de reembolso:

```
A empresa permite solicitações de reembolso em até 30 dias
após a compra. O cliente deve apresentar o comprovante da
transação e preencher o formulário disponível no portal.

Solicitações relacionadas a produtos com defeito devem ser
encaminhadas ao departamento de suporte. Após a análise,
o reembolso poderá ser realizado pelo mesmo meio de pagamento.
```

Suponha que o sistema esteja configurado para criar chunks de aproximadamente 25 palavras.

O resultado poderia ser algo semelhante a:

```
Chunk 1:
"A empresa permite solicitações de reembolso em até 30 dias
após a compra. O cliente deve apresentar o comprovante da"

Chunk 2:
"transação e preencher o formulário disponível no portal.
Solicitações relacionadas a produtos com defeito devem ser
encaminhadas ao departamento de suporte."

Chunk 3:
"Após a análise, o reembolso poderá ser realizado pelo
mesmo meio de pagamento."
```

Perceba o problema: o primeiro chunk termina no meio de uma informação, enquanto o segundo começa continuando a frase anterior.

Esse é justamente o principal trade-off do Fixed-size Chunking. **A divisão é previsível, mas não necessariamente respeita a estrutura ou o significado do conteúdo.**

## Por que é importante

O Fixed-size Chunking é importante porque oferece uma estratégia simples, previsível e fácil de implementar para preparar grandes volumes de documentos para um sistema RAG.

Suas principais vantagens são:
- implementação simples;
- tamanho previsível dos chunks;
- processamento consistente;
- facilidade para controlar o consumo de tokens;
- bom funcionamento em conteúdos pouco estruturados.

Por outro lado, a simplicidade pode gerar problemas quando o conteúdo possui uma estrutura semântica importante. Uma divisão pode acontecer no meio de uma frase, parágrafo, tabela ou seção, separando informações que deveriam permanecer juntas.

Por isso, Fixed-size Chunking costuma ser mais adequado quando **a previsibilidade do tamanho é mais importante do que preservar a estrutura semântica do documento**.

A relação com o conceito anterior fica assim:

```
Chunking
   ↓
Estratégia para dividir documentos

Fixed-size Chunking
   ↓
Divide pelo tamanho definido

Semantic Chunking
   ↓
Divide considerando significado e estrutura
```

O ponto central é: **Fixed-size Chunking transforma um documento em chunks de tamanho controlado, mas não necessariamente em unidades completas de significado.**