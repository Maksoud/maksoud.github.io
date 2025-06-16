### [Sumário](<https://maksoud.github.io/Sumário>)

# Diferença entre prompt engineering, fine-tuning e embeddings

*Entenda as principais abordagens para personalizar e melhorar os resultados de um LLM como o ChatGPT para empresas e negócios.*


## Introdução

Ao criar soluções baseadas em inteligência artificial para empresas, você vai encontrar três estratégias principais para "moldar" o comportamento de um LLM (Large Language Model):

* **Prompt Engineering**
* **Fine-tuning**
* **Embeddings**

Cada uma tem um propósito, um nível de complexidade e um custo operacional diferentes. Escolher a abordagem certa depende do problema que você quer resolver, do orçamento disponível e da experiência técnica da equipe.


## O que é Prompt Engineering?

### Definição:

**Prompt Engineering** é a arte de **escrever instruções claras, detalhadas e estratégicas** para obter do modelo a resposta desejada, sem precisar alterar o modelo em si.

### Exemplo:

> **Prompt:**
> *"Você é um assistente de atendimento de uma empresa de tecnologia. Responda de forma cordial e objetiva, usando listas numeradas quando possível."*

### Quando Usar:

* Casos rápidos e simples
* Customizações que não exigem treinamento adicional
* Quando você quer **controle total sobre a saída apenas ajustando o input**

### Vantagens:

* Rápido
* Sem custo extra de infraestrutura
* Fácil de testar e iterar

### Limitações:

* Não adapta o conhecimento do modelo (ele só "segue" o que o prompt diz)
* Em tarefas muito complexas, o prompt pode ficar longo e difícil de manter


## 🔧 O que é Fine-Tuning?

### Definição:

**Fine-tuning** é o processo de **re-treinar o modelo com um conjunto específico de dados**, ajustando os pesos da rede neural para especializar o LLM em uma tarefa, estilo ou domínio.

### Exemplo:

Treinar um GPT para escrever textos no tom jurídico usando **milhares de documentos legais** como base.

### Quando Usar:

* Quando você precisa que o modelo aprenda um **estilo de escrita**, um **vocabulário específico** ou **responda perguntas técnicas com alto grau de precisão**
* Projetos de médio a grande porte, onde há disponibilidade de dados e orçamento para o treinamento

### Vantagens:

* Respostas mais naturais dentro do contexto do domínio
* Menor necessidade de prompts complexos após o ajuste
* O modelo "aprende de verdade" os dados fornecidos

### Limitações:

* Custo elevado de treinamento
* Requer equipe técnica com experiência em IA
* Pode demorar horas ou dias para treinar
* Dificuldade de atualização constante


## O que são Embeddings?

### Definição:

**Embeddings** são **representações numéricas vetoriais de textos** (palavras, frases ou documentos) que permitem medir **similaridade semântica** entre conteúdos.

O modelo não é re-treinado, mas você consegue fornecer **contextos personalizados** para as respostas a partir de uma base de dados que você mesmo cria.

### Exemplo de Uso:

* Você tem uma base de conhecimento com 500 FAQs.
* Usa embeddings para comparar o que o usuário perguntou com as perguntas da base.
* O sistema seleciona a resposta mais parecida e envia ao ChatGPT junto com o prompt.

### Quando Usar:

* Quando precisa adicionar **conhecimento específico da empresa** (manuais, FAQ, documentos internos)
* Soluções de **RAG (Retrieval-Augmented Generation)** – geração com recuperação de contexto
* Quando o conteúdo muda com frequência, mas você não quer fazer fine-tuning toda vez

### Vantagens:

* Flexível e rápido
* Não precisa re-treinar o modelo
* Escalável para diferentes bases de conhecimento
* Barato em comparação com fine-tuning

### Limitações:

* A qualidade depende da estruturação da base de dados
* Não altera o "comportamento" do modelo, apenas adiciona contexto antes da geração da resposta


## Comparação Direta entre as Abordagens

| Fator                      | Prompt Engineering | Fine-tuning           | Embeddings (RAG)               |
| -------------------------- | ------------------ | --------------------- | ------------------------------ |
| Custo                      | Muito baixo        | Alto                  | Médio                          |
| Tempo para implementar     | Minutos            | Dias ou semanas       | Horas ou dias                  |
| Flexibilidade              | Alta               | Média                 | Alta                           |
| Personalização de Estilo   | Baixa              | Alta                  | Média                          |
| Uso de dados externos      | Via prompt manual  | Incorporado no modelo | Via recuperação dinâmica (RAG) |
| Exige conhecimento técnico | Básico             | Avançado              | Intermediário                  |

## Qual escolher para seu projeto empresarial?

| Situação                                                             | Solução sugerida   |
| -------------------------------------------------------------------- | ------------------ |
| Precisa de resultado rápido e barato                                 | Prompt Engineering |
| Tem um grande volume de dados específicos e orçamento                | Fine-tuning        |
| Quer contextualizar o modelo com documentos internos de forma rápida | Embeddings         |

## Conclusão

**Prompt Engineering**, **Fine-tuning** e **Embeddings** são três ferramentas poderosas, cada uma com seu papel. Como engenheiro de prompt focado em soluções para empresas, o seu diferencial será **saber quando aplicar cada uma**, sempre alinhado aos objetivos de negócio, orçamento e infraestrutura disponível.


<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>