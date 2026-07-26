# Custos de Infraestrutura: Mapa e Endereços

> Os dois custos variáveis que decidem a margem de uma plataforma de rastreamento são **exibir o mapa** e **transformar coordenada em endereço**. Ambos crescem com a base de veículos, e é onde quem não planeja perde dinheiro.
>
> Notas relacionadas: [[Estrutura]] · [[Funcionalidades]] · [[Requisitos para vendas]]

## Custo 1: exibir o mapa (tiles)

Se usar Google Maps, a estrutura atual é assim: o crédito universal de US$ 200/mês acabou em março de 2025; foi substituído por limites gratuitos por SKU, e o Dynamic Maps (mapa interativo em JavaScript) tem 10.000 carregamentos gratuitos por mês, cobrando US$ 7 por 1.000 carregamentos acima disso. [Scrap + 2](https://scrap.io/google-maps-api-pricing-calculator-alternatives-2025)

Detalhe técnico importante para a sua conta: o "map load" é cobrado **por inicialização do mapa na página**, não por atualização de posição. Mover o marcador do veículo a cada 30 segundos não gera custo — o custo é cada vez que o cliente abre o portal/app. Numa carteira de 200 clientes abrindo o app algumas vezes por dia, você passa de 10 mil loads/mês com folga e a fatura vira US$ 100–200 mensais, crescendo com a base.

**A alternativa padrão do setor**: praticamente todas as plataformas de rastreamento (incluindo o Traccar, que já vem assim) usam **Leaflet ou OpenLayers com tiles de OpenStreetMap** — bibliotecas open source com provedores de tiles gratuitos ou muito baratos. Os tiles públicos do OSM têm política de uso que desaconselha volume comercial pesado, então o arranjo profissional é Leaflet + um provedor como **MapTiler ou LocationIQ** (planos gratuitos generosos, pagos a partir de ~US$ 25/mês com volume que atende milhares de veículos) ou tiles self-hosted no seu próprio VPS se quiser custo fixo zero variável. Visualmente, para o caso de uso "onde está meu carro", a diferença para o Google Maps é irrelevante para o cliente final.

## Custo 2: transformar coordenada em endereço (reverse geocoding)

Este é o custo escondido que derruba quem não planeja. O rastreador manda só lat/lng; o "Antares, Maceió – AL" do seu mockup exige uma chamada de geocoding. No Google, são 10.000 requisições gratuitas/mês e US$ 5 por 1.000 depois disso. [Woosmap](https://www.woosmap.com/blog/is-google-maps-api-free) · [Woosmap](https://www.woosmap.com/blog/google-maps-api-key-free)

A matemática que importa: 200 veículos reportando a cada 30 segundos geram mais de meio milhão de posições por dia. Geocodificar cada posição recebida seria financeiramente absurdo em qualquer provedor pago. A arquitetura correta é:

- **Geocodificar sob demanda**: só quando alguém está olhando a tela, não a cada pacote recebido.
- **Cachear agressivamente**: veículo parado ou andando na mesma rua não precisa de nova consulta — só geocodifique quando a posição mudar mais que ~200 m do último endereço resolvido.
- **Provedor barato ou próprio**: LocationIQ dá 5.000 consultas/dia no plano gratuito, ou você sobe um **Nominatim self-hosted** (o geocoder do OSM) só com os dados do Brasil no seu VPS — custo marginal zero, que é o que várias plataformas de rastreamento fazem.

Com essas três medidas, o custo de geocoding de uma operação de centenas de veículos cabe no plano gratuito de um provedor ou num container no seu servidor.

## Conclusão: custo estrutural vira argumento de venda

Com Leaflet + tiles baratos + geocoding cacheado, o custo de infraestrutura por veículo fica em **centavos**, e praticamente fixo em vez de crescer com a base. O desdobramento disso na conversa comercial está em [[Requisitos para vendas]] — resumindo: o mapa deixa de ser risco de margem e vira diferencial de custo estrutural contra concorrentes construídos em cima do Google.
