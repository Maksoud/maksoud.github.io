## Disclaimer

Este repositório foi criado para armazenar material dos meus estudos, seja criado por mim ou copiado das minhas pesquisas pessoais, ou seja, é de ==uso pessoal==. Ele contém tanto conteúdo proprietário quanto informações encontradas através de IA e sites na web. O repositório é ==público== para facilitar o acesso às informações nele contidas. No entanto, **não sou responsável pela propagação ou divulgação de qualquer conteúdo proprietário que possa estar aqui.**

## [Sumário](<https://maksoud.github.io/Sumário>)

### O que é o formato .md?
>O formato de marcação `.md`, conhecido como Markdown, é uma linguagem de marcação leve e fácil de ler e escrever. Ele é usado para formatar texto simples, permitindo a criação de documentos estruturados, como artigos, documentação, e README files, que podem ser convertidos para HTML. Markdown usa símbolos simples (por exemplo, `#` para títulos, `*` para listas) para definir a estrutura e a formatação do texto.

**Dica de formatação de um arquivo .md podem ser encontradas** [aqui](<obsidian://open?vault=Obsidian%20Vault&file=maksoud.github.io%2FMarkdown%20Instructions>)
## Qual ferramenta está sendo utilizada?
A ferramenta que estou utilizando para criação desse conteúdo é a Obsidian.md. Ela oferece diversas vantagens para quem precisa organizar e interconectar notas em Markdown. Ela permite a criação de links bidirecionais entre notas, facilitando a construção de um "second brain" digital, onde informações estão interconectadas de maneira intuitiva. Além disso, Obsidian.md suporta gráficos de conhecimento, que visualizam como as notas estão relacionadas, e oferece uma ampla gama de plugins para personalização. Um outro ponto positivo que me apoiou na escolha dessa ferramenta foi o armazenamento dos arquivos .md, pois eles ficam salvos em seu computador e você poderá realizar o upload de seus arquivos para sua conta pessoa no GitHub, como eu fiz aqui.

### Como "automatizar" o upload das alterações?

Para facilitar a gravação das alterações no repositório, foi criado um arquivo chamado save.bat com o seguinte conteúdo:

```bat
@echo off
:: Define the path to your repository
set REPO_PATH="C:\\Users\\username\\OneDrive\\Documentos\\Obsidian Vault\
\\repositorio.github.io"

:: Navigate to the repository directory
cd /d %REPO_PATH%

:: Fix the Git configuration error
git config --global gc.auto 0

:: Add all changes to git
git add .

:: Commit changes with a message
git commit -m "Atualizacao automatica de notas"

:: Push changes to the remote repository
git push origin main

:: Pause to view the output
pause
```

---
---
## Projetos Pessoais
[Ver Mais](<https://maksoud.dev/projetos/>)

#### [Calculadora de ODDs](https://maksoud.dev/calculadora-odds/)

Este projeto consiste em uma ferramenta avançada para cálculo de probabilidades em apostas esportivas. A calculadora analisa duas cotações (ODDs) diferentes de casas de apostas e determina se a discrepância entre elas pode gerar um retorno financeiro positivo, independentemente do resultado do evento. Por exemplo, suponha que você possa apostar no time A com uma ODD de 2,20 em uma casa de apostas, enquanto em outra, a ODD para o time B ou empate esteja a 2,80. Neste cenário, nossa calculadora identifica uma oportunidade de surebet, onde um investimento estratégico nas duas apostas resultaria em um lucro garantido de 23,20%, independente de qual seja o resultado final do jogo. O valor ganho em uma aposta cobriria o valor perdido na outra. Por isso, surebet.

**GitHub:** [https://github.com/Maksoud/calculadora-odds](https://github.com/Maksoud/calculadora-odds)

**Projeto semelhante:**
- [https://github.com/Maksoud/calculadora-probabilidades](https://github.com/Maksoud/calculadora-probabilidades)
- [https://github.com/Maksoud/calculadora-blaze](https://github.com/Maksoud/calculadora-blaze)

---
#### [Quiz App](https://maksoud.dev/quiz-app/)

Como o nome sugere, este aplicativo é um jogo de perguntas e respostas que testa seus conhecimentos em diversos temas. Cada pergunta vem com quatro opções de resposta, e ao final do quiz, o app avalia e exibe o número de respostas corretas. Desenvolvido inicialmente como um projeto de estudo em jQuery, esta versão foi reconstruída utilizando apenas Javascript puro.

GitHub: [https://github.com/Maksoud/quiz-app](https://github.com/Maksoud/quiz-app)

---
#### [Recipe App](https://maksoud.dev/recipe-app/)

Este aplicativo dinâmico oferece uma nova receita a cada acesso, tornando cada visita uma surpresa deliciosa. Utilizando uma API, o app busca receitas reais e suas respectivas imagens, permitindo aos usuários não só descobrir novos pratos mas também explorar detalhes e instruções de preparo. Além de visualizar receitas, os usuários podem pesquisar pratos específicos e adicioná-los aos favoritos, tudo isso usando apenas Javascript. Este projeto foi desenvolvido como parte de meus estudos aprofundados em Javascript, demonstrando a capacidade do uso eficaz de APIs e a manipulação de dados em tempo real.

GitHub: [https://github.com/Maksoud/recipe-app](https://github.com/Maksoud/recipe-app)

---
#### [Recipe App jQuery](https://maksoud.dev/recipe-app-jquery/)

Este é o mesmo app anterior, porém utilizando o jQuery para criar as funcionalidades.

GitHub: [https://github.com/Maksoud/recipe-app-jquery](https://github.com/Maksoud/recipe-app-jquery)

---
#### [Reiniciando Financeiro e Estoques](<https://www.reiniciando.com.br/>)

O Reiniciando é um sistema versátil e abrangente, projetado para se adaptar às necessidades específicas do seu negócio, permitindo que você se concentre no que realmente importa: o crescimento sustentável e o controle eficiente de suas operações. Com uma abordagem centrada na facilitação da gestão empresarial, oferecemos uma gama completa de soluções para otimizar seus processos financeiros e de controle de estoques.
##### Controle Total de Receitas e Despesas com o Sistema Reiniciando

O sistema Reiniciando oferece uma solução completa e intuitiva para o gerenciamento de receitas e despesas da sua empresa. Com uma interface de fácil navegação e recursos avançados, o controle financeiro se torna uma tarefa simples e eficaz, disponível a qualquer momento, todos os dias da semana.
##### Gerenciamento Aprofundado de Finanças

- **Acompanhamento Detalhado**: Com o Reiniciando, você tem acesso a uma vasta gama de relatórios que possibilitam um acompanhamento minucioso das suas contas a pagar e receber. Isso inclui uma análise detalhada de toda a movimentação financeira por período.

- **Filtros Personalizados**: Utilize filtros de planos de contas e centros de custos para refinar sua análise financeira. Com a flexibilidade de filtrar também por tipo de documento ou evento, você ganha uma compreensão profunda do seu fluxo de caixa.

- **Relatórios Diversificados**: Oferecemos uma variedade de relatórios que são essenciais para o controle do fluxo de caixa da sua empresa. Cada relatório é projetado para fornecer insights valiosos, ajudando você a tomar decisões financeiras informadas.

Mais informações podem ser encontradas em [Reiniciando Wiki](<https://reiniciandowiki.maksoud.dev/>)