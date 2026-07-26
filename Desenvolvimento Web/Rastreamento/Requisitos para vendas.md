# Requisitos para Vendas: Precificação e Pitch

> Base para a conversa comercial: quanto o mercado cobra, como estruturar o preço, o que falar e em que ordem.
>
> Notas relacionadas: [[Estrutura]] · [[Funcionalidades]] · [[Custos de Infraestrutura]]

## Valores de mercado

O que a pesquisa mostrou sobre plataformas white label B2B no Brasil (o seu comparável direto):

| Concorrente | Modelo | Preço |
| --- | --- | --- |
| [Rastreamos.APP](https://rastreamos.app/faq) | Por veículo | R$ 3,50/veículo/mês, mínimo de 20 veículos + R$ 200 de adesão (configuração da marca) |
| [SmartGPS](https://smartgps.com.br/) | Por dispositivo, plataforma pura | A partir de R$ 2,20/dispositivo |
| [Brtrak](https://brtrak.com.br/) | Fixo mensal escalonado | A partir de R$ 109/mês, escalonado por número de veículos |

Para contexto da ponta final (o que o cliente do seu cliente paga): a mensalidade média de rastreamento nas capitais gira em torno de R$ 39,90 — em Maceió, valores entre R$ 40 e R$ 80 são comuns, como o R$ 79,90 do seu próprio mockup. [Brtrak](https://brtrak.com.br/)

## Como estruturar a sua cobrança

O intervalo de mercado da plataforma pura é **R$ 2 a R$ 4 por veículo/mês**. Você não deve competir nesse piso, porque seu produto inclui o que os white labels genéricos não têm: gestão financeira com boleto/Pix integrado, régua de inadimplência e portal do cliente com segunda via. Isso justifica posicionamento acima.

> [!tip] Modelo sugerido
> **R$ 5 a R$ 7 por veículo ativo/mês**, com **piso mensal de R$ 350–500**, mais **taxa de implantação de R$ 1.500–3.000** (cobre migração dos rastreadores via SMS, importação da carteira, personalização de marca e treinamento).

A implantação é importante não só pela receita: cliente que paga setup leva a migração a sério e não abandona no meio.

**A matemática que você apresenta para ele**: numa carteira de 200 veículos a R$ 6, ele paga R$ 1.200/mês de plataforma enquanto fatura R$ 12.000+ de mensalidades — 10% da receita para eliminar planilha, inadimplência invisível e plataforma sem marca. Se a automação de cobrança recuperar dois ou três inadimplentes por mês, a plataforma se paga sozinha.

### Duas táticas de fechamento

- **Cliente fundador**: se for o primeiro cliente, ofereça desconto real (por exemplo, R$ 4/veículo travado por 12 meses) em troca de caso de sucesso e paciência com ajustes — mas ==nunca gratuidade, porque cliente que não paga não valida nada==.
- **Cobre por veículo ativo, não por cliente**: escala junto com o crescimento dele e é o padrão que o mercado já aceita, o que facilita a comparação a seu favor.

## Pitch de vendas

> "Hoje sua operação de rastreamento provavelmente roda em três lugares: uma plataforma genérica de mapa, uma planilha de cobrança e o WhatsApp do suporte. Eu entrego isso num sistema só, com a **sua marca**: o seu cliente acessa um portal e um app com o mapa do veículo, bloqueio, boleto e segunda via — e você acessa um painel administrativo que mostra quem está inadimplente, qual rastreador parou de reportar antes do cliente ligar, e todo o histórico de comandos com auditoria. Menos ligação de cobrança, menos chamado de suporte, e uma cara profissional que ajuda a vender mais planos. A plataforma é minha, a marca e o cliente são seus."

### As três dores que o pitch ataca

1. **Cobrança manual** — planilha, boleto no braço, ligação de cobrança.
2. **Rastreador silencioso** — descobrir que o aparelho parou quando o cliente liga.
3. **Plataforma sem identidade** — o cliente final vê a marca de outra empresa.

==Confirme as três dores com as palavras dele antes de abrir preço.== Se ele confirmar, o fechamento fica natural.

## Custo de mapa como argumento comercial

O detalhamento técnico está em [[Custos de Infraestrutura]]; na conversa de venda, isso vira argumento a seu favor e não item de custo repassado:

> "O mapa e os endereços já estão inclusos na mensalidade — você não paga licença de Google Maps por fora."

Concorrentes que construíram em cima do Google têm esse custo variável embutido e ele cresce com a base; o seu, com Leaflet + tiles baratos + geocoding cacheado, é quase fixo. Isso protege a sua margem no modelo de R$ 5–7/veículo: o custo de infraestrutura por veículo fica em centavos, e o mapa deixa de ser risco de margem para ser diferencial de custo estrutural.

A única situação em que valeria pagar Google Maps é se o cliente exigir explicitamente Street View ou a familiaridade visual da marca Google — e aí você cobra isso como adicional, não absorve.
