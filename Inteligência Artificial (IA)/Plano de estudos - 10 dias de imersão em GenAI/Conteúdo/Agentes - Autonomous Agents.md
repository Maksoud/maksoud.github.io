[← Voltar para o Dia 7: Agentes](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-07-agentes/)

# Autonomous Agents

## O que é

Autonomous Agents (agentes autônomos) são agentes que **perseguem um objetivo por conta própria, com pouca ou nenhuma intervenção humana**, decidindo sozinhos as etapas, as ferramentas e quando a tarefa está concluída.

O termo ficou famoso em 2023 com projetos como **AutoGPT** e **BabyAGI**, que recebiam um objetivo amplo ("crie um negócio online") e tentavam executá-lo sozinhos.

Hoje, exemplos mais maduros são os agentes de programação (como Claude Code, Codex e Devin) e os agentes que usam o computador (computer use / browser agents).

## Como funciona

A autonomia é um **nível**, não um sim ou não:

```
Nível 1 → Assistente: sugere, humano executa
Nível 2 → Executa com aprovação a cada passo
Nível 3 → Executa sozinho, pede aprovação em ações críticas
Nível 4 → Executa sozinho dentro de limites definidos
Nível 5 → Autonomia total (raro e arriscado)
```

Um agente autônomo costuma ter:
- objetivo de alto nível;
- capacidade de criar e revisar o próprio plano;
- conjunto amplo de ferramentas;
- memória para tarefas longas;
- critério próprio de conclusão;
- execução por horas, às vezes em segundo plano.

## Um exemplo

Agente de programação recebendo:

> "Corrija o bug que faz o login falhar com e-mails em maiúsculas e abra um pull request."

```
Lê o código do login
   ↓
Reproduz o bug escrevendo um teste
   ↓
Teste falha (bug confirmado)
   ↓
Altera o código para normalizar o e-mail
   ↓
Roda os testes → todos passam
   ↓
Abre o pull request com a descrição da mudança
```

O humano só revisa o resultado final.

## Por que é importante

Agentes autônomos mostram o potencial máximo da tecnologia, mas também seus limites:
- **erros se acumulam**: em tarefas longas, pequenos desvios viram grandes problemas;
- **custo imprevisível**: muitas iterações, muitos tokens;
- **segurança**: acesso amplo a ferramentas aumenta o impacto de erros e de Prompt Injection.

Por isso, autonomia costuma vir acompanhada de **sandbox** (ambiente isolado), permissões restritas, limites de orçamento e logs detalhados.

Na maioria dos projetos corporativos, o ideal ainda é **autonomia limitada**, com Human-in-the-loop nos pontos críticos.

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/conteudo/agentes-autonomous-agents/)

<sup><sub>
Renée Maksoud - novembro de 2026
</sub></sup>
