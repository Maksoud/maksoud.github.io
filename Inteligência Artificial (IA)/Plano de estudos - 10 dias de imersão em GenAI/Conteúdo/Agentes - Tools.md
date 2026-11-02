[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Tools

## O que é

Tools (ferramentas) são as **capacidades externas** que um agente pode usar para obter informações ou agir no mundo. São as "mãos" do agente.

Exemplos comuns:
- busca na web;
- consulta a banco de dados (SQL);
- chamadas a APIs (CRM, ERP, ServiceNow, e-mail);
- busca em base vetorial (Retrieval do RAG);
- interpretador de código (Python);
- leitura e escrita de arquivos;
- calculadora.

## Como funciona

Toda ferramenta é apresentada ao modelo com três elementos:

```
Nome         → buscar_cliente
Descrição    → "Busca dados de um cliente pelo CPF"
Parâmetros   → { "cpf": string }
```

O modelo lê essas descrições e decide **quando** e **como** usar cada ferramenta. Por isso, a descrição funciona como um prompt: é ela que orienta a escolha.

Uma classificação útil:

```
Tools de leitura   → consultam informação (baixo risco)
                     ex.: buscar_pedido, pesquisar_web

Tools de escrita   → alteram o mundo (maior risco)
                     ex.: enviar_email, cancelar_pedido, pagar_fatura
```

Ferramentas de escrita costumam exigir mais validação, permissões restritas e, às vezes, aprovação humana.

## Um exemplo

Um agente de suporte de TI pode ter:

```
Tools:
- buscar_artigo_kb(pergunta)
- consultar_chamado(numero)
- abrir_chamado(descricao, prioridade)
- resetar_senha(usuario)        ← exige confirmação
```

Pedido: "Esqueci minha senha e não consigo entrar no e-mail."

```
Agente → buscar_artigo_kb("reset de senha")
Agente → resetar_senha("joao.silva")  (após confirmação)
Agente → "Sua senha foi redefinida. Verifique o SMS."
```

## Por que é importante

As ferramentas definem **o que o agente consegue fazer**. Um LLM excelente com ferramentas ruins entrega um agente ruim.

Boas práticas:
- poucas ferramentas, bem descritas (muitas ferramentas confundem o modelo);
- nomes e parâmetros autoexplicativos;
- retornos claros e concisos (o resultado volta para o contexto e consome tokens);
- mensagens de erro úteis, para o agente conseguir se corrigir;
- princípio do menor privilégio em ferramentas de escrita.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-tools/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
