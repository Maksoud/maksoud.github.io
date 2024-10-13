Um **modelo generativo** é um tipo de modelo de aprendizado de máquina projetado para **gerar novos exemplos de dados** que seguem a mesma distribuição do conjunto de dados de treinamento. Em vez de simplesmente classificar ou fazer previsões sobre os dados (como um modelo discriminativo), o objetivo principal dos modelos generativos é **aprender a distribuição dos dados** e, em seguida, **amostrar novos dados** dessa distribuição.

### Como funciona um modelo generativo?

Esses modelos tentam **modelar a distribuição conjunta** entre os dados de entrada (X) e os rótulos (Y) (se existirem), ou apenas a distribuição dos dados (no caso de aprendizado não supervisionado). Assim, a ideia principal é estimar a probabilidade \( P(X) \), ou \( P(X, Y) \) em casos supervisionados, que reflete a probabilidade de que um determinado conjunto de dados possa ser gerado por um determinado processo.

Um exemplo intuitivo seria um modelo que, após ser treinado em um grande conjunto de dados de imagens de gatos, é capaz de gerar imagens realistas de gatos que não existem no mundo real, mas que parecem seguir o padrão dos gatos no conjunto de dados de treinamento.

### Principais tipos de Modelos Generativos

1. **Redes Geradoras Adversárias (Generative Adversarial Networks - GANs)**
   - **Como funciona:** As GANs consistem em duas redes: uma **geradora** (G) e uma **discriminadora** (D). A rede geradora tenta criar exemplos realistas (dados falsos), enquanto a rede discriminadora tenta distinguir entre exemplos reais e gerados. Essas redes competem entre si em um processo de aprendizado adversarial. A rede geradora melhora ao longo do tempo, criando dados cada vez mais realistas, enquanto a discriminadora se torna mais eficaz em detectar falsificações.
   - **Exemplo:** Um GAN treinado em imagens de rostos humanos pode gerar novos rostos que não pertencem a nenhuma pessoa real, mas parecem humanos.

2. **Modelos Variacionais de Autoencoders (Variational Autoencoders - VAEs)**
   - **Como funciona:** O VAE é um tipo de autoencoder que força a **representação latente** (uma