[← Voltar para o Plano de estudos: 10 dias de imersão em GenAI](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai-2/)

# Dia 8: Construir um agente

Faça algo pequeno.

Por exemplo:

### Agente de análise de vagas

Você fornece:

```
Descrição da vaga
+
Seu currículo
```

O agente pode possuir ferramentas como:

```
search_web()
calculate_match()
retrieve_documents()
analyze_skill()
```

Fluxo:

```
           VAGA
             ↓
          AGENTE
             ↓
       ┌─────┼─────┐
       ↓     ↓     ↓
    RAG   Search  Calculator
       ↓     ↓     ↓
       └─────┼─────┘
             ↓
          Análise
```

Isso seria especialmente interessante porque conecta **GenAI com seu próprio contexto profissional**.

---

[link de compartilhamento](https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/plano-de-estudos-10-dias-de-imersao-em-genai/dia-08-construir-um-agente/)

<sup><sub>
Renée Maksoud - outubro de 2026
</sub></sup>
