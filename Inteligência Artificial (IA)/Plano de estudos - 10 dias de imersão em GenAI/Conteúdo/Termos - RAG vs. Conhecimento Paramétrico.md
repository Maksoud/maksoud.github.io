[← Voltar para o Dia 4: RAG: finalmente](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-04-rag-finalmente/)

# RAG vs. Conhecimento Paramétrico

## O que é?

Um [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/) pode responder a uma pergunta usando duas fontes de conhecimento:
1. **Conhecimento paramétrico:** o que o modelo aprendeu durante o treinamento e que ficou "guardado" nos seus [parâmetros](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-parameters/).
2. **Conhecimento não paramétrico (RAG):** informações buscadas em uma fonte externa no momento da pergunta e entregues ao modelo como contexto.

A ideia central é:

> **O conhecimento paramétrico é o que o modelo "sabe de memória". O RAG é o que o modelo "consulta" antes de responder.**

## Como funciona

### Conhecimento paramétrico

Durante o pré-treinamento, o modelo lê uma enorme quantidade de textos e ajusta bilhões de parâmetros. Parte do que ele leu fica codificada nesses parâmetros, de forma distribuída e aproximada.

Quando você pergunta algo, o modelo gera a resposta apenas a partir desse conhecimento interno:
```
Pergunta do usuário  
↓  
LLM (usa apenas o que aprendeu no treinamento)  
↓  
Resposta
```

### Conhecimento via RAG

Com [RAG](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag/), o sistema primeiro busca trechos relevantes em documentos e depois entrega esses trechos ao modelo:
```
Pergunta do usuário  
↓  
Retrieval nos documentos  
↓  
Trechos relevantes no contexto  
↓  
LLM (usa o contexto + o que aprendeu no treinamento)  
↓  
Resposta
```

Repare que, mesmo com RAG, o modelo continua usando o conhecimento paramétrico: é ele que permite entender a pergunta, interpretar os trechos e escrever a resposta. O RAG não substitui esse conhecimento, ele o **complementa** com fatos específicos.

## Um exemplo

Pergunta:

> "O que é o ITIL 4?"

Um LLM provavelmente responde bem só com o conhecimento paramétrico, porque esse assunto aparece em muitos textos públicos usados no treinamento.

Agora outra pergunta:

> "Qual é o prazo de atendimento de incidentes críticos definido no contrato da nossa empresa?"

O modelo não tem como saber isso. Essa informação é privada e nunca esteve nos dados de treinamento. Sem RAG, ele pode dizer que não sabe ou, pior, inventar um prazo ([hallucination](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-hallucination/)).

Com RAG, o sistema recupera o trecho do contrato e o modelo responde com base nele.

## Comparação

| Aspecto | Conhecimento paramétrico | RAG |
| --- | --- | --- |
| Onde fica o conhecimento | Nos parâmetros do modelo | Em documentos externos (base vetorial, banco, arquivos) |
| Atualização | Exige novo treinamento ou fine-tuning | Basta atualizar os documentos |
| Informação privada | Não conhece, a menos que tenha sido treinado nela | Acessa, se estiver na base |
| Data de corte | Limitado à data do treinamento | Pode usar informação recente |
| Rastreabilidade | Difícil saber de onde veio a resposta | Pode citar a fonte do trecho usado |
| Custo e latência | Menor: só uma chamada ao modelo | Maior: busca + contexto mais longo |
| Risco principal | Alucinar ou responder com dado desatualizado | Recuperar trecho errado ou insuficiente |

## Quando usar cada um

O conhecimento paramétrico costuma bastar para:
- conhecimento geral e conceitos amplamente documentados;
- tarefas de linguagem (resumir, traduzir, reescrever, classificar);
- raciocínio sobre informações que o próprio usuário já forneceu na pergunta.

O RAG é indicado quando a resposta depende de:
- documentos internos ou privados;
- informações que mudam com frequência;
- dados posteriores à data de corte do modelo;
- respostas que precisam citar a fonte;
- precisão em detalhes específicos (valores, prazos, regras).

## Por que é importante

Entender essa diferença ajuda a decidir **quando um sistema realmente precisa de RAG**. Nem toda aplicação de IA precisa de busca em documentos: se o modelo já sabe responder bem, o RAG só adiciona custo e complexidade.

Também ajuda a entender um problema comum: o **conflito entre as duas fontes**. Se o trecho recuperado diz uma coisa e o conhecimento interno do modelo diz outra, o modelo pode ignorar o contexto e responder "de memória". Por isso, em aplicações RAG, o prompt costuma instruir o modelo a responder **apenas com base no contexto fornecido** e a dizer quando a informação não está nele.

Por fim, vale lembrar a diferença para o **fine-tuning**:

**Fine-tuning:** altera o conhecimento paramétrico, treinando o modelo com novos dados.

**RAG:** não altera o modelo, apenas fornece conhecimento externo no momento da consulta.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-rag-vs-conhecimento-parametrico/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
