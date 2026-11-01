[← Voltar para o Dia 2: Prompt Engineering 2.0](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-02-prompt-engineering-2-0/)

# Guardrails

## O que é

**Guardrails**, ou **barreiras de proteção**, são regras, mecanismos e validações utilizados para controlar o comportamento de um sistema de IA.

Enquanto uma instrução diz ao modelo **o que fazer**, um guardrail define também **o que ele pode ou não fazer**, além de verificar se a entrada ou a saída está dentro dos limites esperados.

Eles podem atuar em diferentes momentos:

```
Entrada do usuário
        ↓
Guardrail de entrada
        ↓
LLM
        ↓
Guardrail de saída
        ↓
Resposta / ação
```

Guardrails não precisam estar dentro do próprio prompt. Eles podem ser implementados na aplicação que utiliza o modelo, por meio de regras, classificadores, validações, filtros, schemas ou outras verificações.

## Como funciona

Imagine um caixa eletrônico.

O sistema permite que você faça determinadas operações, mas existem várias barreiras:

```
Senha correta?
    ↓
Conta válida?
    ↓
Operação permitida?
    ↓
Saldo suficiente?
    ↓
Executar operação
```

Mesmo que alguém tente solicitar uma operação indevida, as regras do sistema impedem que ela seja executada.

Em uma aplicação com [LLM](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/termos-llm/), o princípio é semelhante.

O modelo pode receber uma solicitação e, antes de gerar uma resposta ou executar uma ação, o sistema pode verificar:

```
A solicitação é permitida?
A informação é adequada?
O formato está correto?
A resposta contém algo proibido?
A ação solicitada pode ser executada?
```

Isso é particularmente importante porque um LLM é um sistema probabilístico. Uma instrução como:

```
Nunca forneça informações confidenciais.
```

pode ser importante, mas não deveria necessariamente ser a **única camada de proteção** de uma aplicação crítica.

## Um exemplo

Imagine um chatbot de uma instituição financeira.

O sistema permite que o usuário consulte informações sobre sua própria conta, mas não permite que o modelo revele dados de outros clientes.

Podemos ter um guardrail de entrada:

```
Se a solicitação tentar obter dados pessoais
de outra pessoa, bloqueie a solicitação.
```

E um guardrail de saída:

```
Antes de enviar a resposta, verifique se ela
contém dados pessoais de terceiros.
Se contiver, não envie a resposta original.
```

O fluxo poderia ser:

```
Usuário
   ↓
Verificação da solicitação
   ↓
LLM
   ↓
Verificação da resposta
   ↓
Resposta segura
```

Os guardrails também podem controlar aspectos menos relacionados à segurança.

Por exemplo, uma aplicação pode exigir que o modelo sempre produza:

```
{
  "categoria": "financeiro",
  "prioridade": "alta",
  "resumo": "..."
}
```

Um **[JSON Schema](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-json-schema/)** pode funcionar como parte desse mecanismo de controle, permitindo validar se a resposta realmente possui a estrutura esperada.

Nesse caso, o guardrail não está necessariamente impedindo um comportamento perigoso. Ele está garantindo **conformidade com uma regra técnica**.

## Por que é importante

Guardrails são importantes porque permitem tratar um sistema de IA como uma aplicação que precisa de **controle e validação**, e não apenas como uma conversa com um modelo.

Eles podem ser utilizados para:
1. **Segurança:** impedir determinados comportamentos ou ações.
2. **Privacidade:** evitar exposição de informações sensíveis.
3. **Qualidade:** verificar se a resposta atende a determinados critérios.
4. **Formato:** garantir que a saída siga uma estrutura esperada.
5. **Controle de ferramentas:** impedir que o agente execute ações não autorizadas.
6. **Validação:** detectar respostas inadequadas antes que cheguem ao usuário.
7. **Conformidade:** aplicar políticas específicas da organização ou do domínio.

Existe também uma distinção importante entre **instruções e guardrails**.

Uma instrução pode dizer:

```
Responda somente com informações relacionadas ao produto.
```

Um guardrail pode verificar efetivamente se a resposta produzida está relacionada ao produto e bloquear ou corrigir uma resposta que viole essa regra.

Assim, podemos pensar:

```
Instrução
    ↓
Orienta o modelo

Guardrail
    ↓
Controla e valida o comportamento
```

Na prática, sistemas robustos normalmente combinam os dois.

Esse conceito também prepara o terreno para **[Prompt Injection](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-prompt-injection/)**. Se um usuário ou um documento externo tentar introduzir instruções que entrem em conflito com as regras do sistema, os guardrails podem atuar como uma camada adicional de proteção.

Portanto, **[Instruction Hierarchy](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-instruction-hierarchy/) define a prioridade das instruções, enquanto Guardrails ajudam a garantir que o sistema permaneça dentro dos limites estabelecidos**.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/prompt-engineering-guardrails/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
