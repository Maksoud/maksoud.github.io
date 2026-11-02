[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Memory

## O que é

Memory (memória) é o mecanismo que permite ao agente **lembrar informações** além de uma única chamada ao modelo.

LLMs são **stateless**: cada chamada começa do zero. Tudo o que o modelo "lembra" precisa ser enviado de novo no contexto. A memória é a forma organizada de fazer isso.

## Como funciona

Costuma-se dividir em dois tipos:

```
Memória de curto prazo
→ o histórico da conversa/tarefa atual
→ vive dentro da Context Window
→ some quando a sessão termina

Memória de longo prazo
→ informações guardadas entre sessões
→ fica fora do modelo (banco, base vetorial, arquivos)
→ é recuperada quando relevante
```

A memória de longo prazo pode ser dividida ainda em:
- **episódica**: o que aconteceu antes ("na semana passada o usuário pediu o relatório X");
- **semântica**: fatos e preferências ("o usuário prefere respostas curtas");
- **procedural**: como fazer as coisas ("para este cliente, sempre copiar o gerente").

Fluxo típico de memória de longo prazo:

```
Conversa
   ↓
Extrair fatos importantes
   ↓
Salvar (banco ou base vetorial)
   ↓
Nova sessão
   ↓
Buscar memórias relevantes (como no RAG)
   ↓
Inserir no contexto
```

## Um exemplo

Sessão 1:

> "Meu nome é Renée e trabalho com ServiceNow."

O agente salva: `{nome: "Renée", area: "ServiceNow"}`.

Sessão 2 (dias depois):

> "Me sugira um projeto para estudar."

O agente recupera a memória e responde:

> "Que tal um agente que classifica incidentes do ServiceNow?"

## Por que é importante

Sem memória, o agente:
- repete perguntas;
- perde o fio em tarefas longas;
- não personaliza respostas.

Desafios:
- **o que guardar**: guardar tudo gera ruído;
- **contexto limitado**: históricos longos precisam ser resumidos ou comprimidos;
- **privacidade**: memórias podem conter dados pessoais (LGPD);
- **memórias erradas**: um fato incorreto salvo contamina sessões futuras.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-memory/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
