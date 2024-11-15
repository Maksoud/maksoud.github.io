### [Sumário](<https://maksoud.github.io/Sumário>) > [Modelos de Inteligência Artificial](<https://maksoud.github.io/Inteligência%20Artificial%20(IA)/Modelos%20de%20Inteligência%20Artificial>)

# Técnica Dropout

A técnica **Dropout** é uma abordagem usada em redes neurais profundas para **prevenir o overfitting** (sobreajuste) durante o treinamento. Foi introduzida por Geoffrey Hinton e seus colaboradores em 2012 e se tornou uma das estratégias mais eficazes para regularizar redes neurais, melhorando sua **generalização** em novos dados.

### Overfitting: O Problema que Dropout Resolve

O **overfitting** ocorre quando uma rede neural aprende os detalhes e o ruído dos dados de treinamento tão bem que se ajusta excessivamente a esses dados, mas falha em generalizar para dados que não viu durante o treinamento. Isso acontece porque a rede se torna muito dependente de padrões específicos, levando a um desempenho pobre em novos exemplos.

A técnica **Dropout** atua como uma forma de **regularização** para evitar esse problema.

### Como Dropout Funciona

Durante o treinamento, **dropout desativa aleatoriamente uma fração dos neurônios em cada camada**, removendo temporariamente suas conexões. Em outras palavras, em cada iteração de treinamento, certos neurônios são **ignorados** no cálculo da ativação, como se tivessem sido "apagados" ou "desligados". Esse processo força a rede a não depender de neurônios específicos, evitando que ela se adapte excessivamente a padrões de treinamento específicos.

- **Taxa de Dropout (Dropout Rate):** A taxa de dropout é o hiperparâmetro que define a **fração dos neurônios a serem desativados**. Por exemplo, uma taxa de dropout de 0.5 significa que, a cada iteração, 50% dos neurônios em uma camada são desativados aleatoriamente.
- **Durante o treinamento:** Neurônios selecionados aleatoriamente em uma camada são "apagados" em cada passo do treinamento, o que força a rede a aprender representações mais robustas e distribuídas.
- **Durante a inferência (teste):** No momento da inferência (ou teste), todos os neurônios são usados, mas os pesos das conexões dos neurônios são **escalados** para compensar a ausência de dropout. Isso é feito multiplicando os pesos pelo inverso da taxa de dropout para manter a média das ativações.

### Benefícios do Dropout

1. **Melhora a Generalização:**
   - Dropout força a rede neural a não depender de combinações específicas de neurônios, forçando-a a aprender representações mais robustas que generalizam melhor para dados que não fazem parte do conjunto de treinamento.

2. **Reduz Dependência Excessiva (Co-adaptação):**
   - Sem dropout, as redes neurais podem desenvolver dependências entre neurônios, o que pode levar ao overfitting. Dropout desativa aleatoriamente neurônios, quebrando essas dependências e garantindo que a rede dependa de várias combinações de neurônios para realizar previsões.

3. **Regularização Efetiva:**
   - Assim como outras formas de regularização (como L2 ou L1), dropout reduz o risco de overfitting, mas de uma maneira mais direta ao desativar neurônios durante o treinamento. Ao fazer isso, evita-se que o modelo fique muito complexo.

4. **Efeito de Ensemble Implícito:**
   - O dropout pode ser visto como uma forma de **ensemble implícito**, onde diferentes subconjuntos de neurônios são usados durante o treinamento, criando efetivamente várias "sub-redes". Na inferência, essas "sub-redes" são combinadas, o que tem um efeito similar ao de combinar múltiplos modelos em aprendizado de máquina, melhorando a robustez do modelo.

### Implementação de Dropout

O dropout é simples de implementar e foi incorporado na maioria dos frameworks de deep learning, como TensorFlow, PyTorch e Keras. Ele é usado principalmente nas **camadas ocultas** da rede e, às vezes, na **camada de entrada** (embora isso seja menos comum).

Aqui está um exemplo simples de implementação de dropout em uma camada de rede usando **Keras**:

```python
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Definir o modelo
model = Sequential()

# Adicionar camadas com dropout
model.add(Dense(128, activation='relu', input_shape=(input_dim,)))
model.add(Dropout(0.5))  # 50% dos neurônios serão desativados aleatoriamente

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))  # Aplicar dropout novamente

model.add(Dense(num_classes, activation='softmax'))

# Compilar o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

### Quando Usar Dropout

- **Grandes Redes Neurais:** Dropout é especialmente útil para redes neurais profundas com um grande número de parâmetros, onde o risco de overfitting é maior.
- **Pequenos Conjuntos de Dados:** Em conjuntos de dados pequenos ou medianos, onde há um maior risco de overfitting, o dropout pode melhorar a capacidade do modelo de generalizar.
- **Antes de Overfitting:** Dropout deve ser aplicado durante o treinamento, especialmente quando você começar a notar uma grande diferença entre a precisão de treinamento e a precisão de validação, indicando que o modelo está sobreajustando ao conjunto de dados de treinamento.

### Limitações do Dropout

1. **Custo Computacional Adicional:**
   - O uso de dropout pode aumentar o tempo de treinamento, pois a rede precisa ser treinada em diferentes subconjuntos de neurônios em cada iteração.

2. **Não é Ideal para Redes Pequenas:** 
   - Em redes menores ou menos profundas, o uso de dropout pode não ser necessário ou pode prejudicar o desempenho, pois já existem poucos parâmetros para ajustar.

3. **Não Necessariamente Adequado para Modelos de Visão Computacional:** 
   - Embora dropout funcione bem em redes fully-connected, em redes convolucionais (CNNs), ele pode não ser tão eficaz quanto outras formas de regularização, como batch normalization. Isso ocorre porque nas CNNs, a estrutura espacial dos dados é importante, e desativar neurônios pode prejudicar essa estrutura.

### Conclusão

**Dropout** é uma técnica poderosa e simples para melhorar a **generalização** de redes neurais profundas, combatendo o **overfitting**. Ele funciona desativando aleatoriamente neurônios durante o treinamento, obrigando a rede a aprender representações mais robustas. Embora tenha algumas limitações, especialmente em termos de custo computacional e sua aplicação em redes menores, é amplamente utilizado em redes totalmente conectadas e em muitas arquiteturas de aprendizado profundo.

<sup><sub>
Renée Maksoud - outubro de 2024
</sub></sup>