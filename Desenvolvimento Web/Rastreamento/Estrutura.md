# Estrutura Técnica da Plataforma de Rastreamento

> **Contexto**: notas de apoio ao projeto de uma plataforma de rastreamento veicular *white label* — o cliente é a empresa de rastreamento, e os motoristas/proprietários são os clientes dela. A interface já está prototipada (mockup navegável em `mczsat.maksoud.dev`) e o objetivo destas notas é dimensionar o que falta para virar sistema real.
>
> Notas relacionadas: [[Funcionalidades]] · [[Custos de Infraestrutura]] · [[Requisitos para vendas]]

## Visão geral da arquitetura

A plataforma se divide em quatro camadas, e a decisão mais importante é **não construir a camada de telemetria do zero**:

| Camada | O que faz | Como resolver |
| --- | --- | --- |
| Telemetria | Recebe os pacotes dos rastreadores (protocolo binário/TCP), decodifica e armazena posições | **Traccar** (open source, suporta os protocolos de mercado, incluindo os aparelhos J16) |
| Backend próprio | Autenticação, multi-tenancy, regras de negócio, financeiro, comandos | Desenvolvimento — é aqui que mora o produto |
| Portal do cliente | Mapa, histórico, bloqueio, boleto e segunda via | Front já desenhado no mockup |
| Painel administrativo | Cadastros, inventário de equipamentos, cobrança, auditoria | Back-office clássico |

O ponto de arquitetura que sustenta tudo: **o Traccar nunca é exposto ao cliente final**. Ele fica atrás do backend próprio, que fala com ele por um único token administrativo. Isso é o que garante isolamento entre clientes e permite trocar a camada de telemetria depois, se necessário.

## Migração dos rastreadores: reconfiguração por SMS

Os aparelhos já instalados em campo apontam para a plataforma antiga. Para trazê-los, basta reconfigurar o servidor de destino por SMS — não é preciso ir até o veículo.

Com o telefone do chip de cada rastreador (que você já tem cadastrado), você envia os comandos de qualquer celular — geralmente exigem a senha do dispositivo no comando, padrão de fábrica `123456`. A sequência típica do J16:

```
APN,zap.vivo.com.br,vivo,vivo#
SERVER,1,rastreio.seudominio.com.br,5023#
RESET#
```

Três ressalvas práticas:

1. **Teste com um dispositivo antes de migrar a frota** — lotes diferentes de J16 vêm com firmwares que variam a sintaxe (alguns usam `SERVER,0,IP,porta#` com IP em vez de domínio).
2. **Chips M2M corporativos podem bloquear SMS recebido** de números não autorizados — verifique com a operadora se o chip aceita SMS de um celular comum.
3. **O histórico fica na plataforma antiga** — se os rastreadores hoje apontam para outra plataforma, exporte os dados antes de virar a chave, caso precise deles.

## Complexidade por componente

Assumindo a rota Traccar, o esforço se distribui assim:

**Telemetria (baixa).** Subir Traccar via Docker num VPS, abrir a porta 5023, cadastrar os dispositivos por IMEI. É configuração, não desenvolvimento — um fim de semana incluindo testes com o primeiro rastreador migrado.

**Autenticação dos clientes (baixa-média).** Aqui tem uma decisão de arquitetura importante: ==não use o login do Traccar para os clientes==. Crie sua própria base de usuários no seu backend, e o backend fala com o Traccar usando um único token administrativo. A tabela de vínculo é simples: `cliente → veículos → device_id do Traccar`. Isso te dá multi-tenancy de verdade — o cliente nunca toca a API do Traccar diretamente, então não há risco de ele enxergar veículo de outro. Login com e-mail/CPF + senha, JWT ou sessão, recuperação por WhatsApp ou e-mail. Você já fez isso no Reiniciando Sistemas; é o mesmo padrão.

**Portal do cliente (média).** O front você já desenhou. O trabalho é a camada de integração: seu backend expõe `/api/veiculos/:id/posicao` que internamente consulta o Traccar e devolve só o que aquele cliente pode ver, mais o reverse geocoding do endereço. Posição em tempo real via polling a cada 15-30s já resolve para rastreamento veicular comum — WebSocket é refinamento, não requisito do MVP.

**Painel administrativo (média).** CRUD de clientes, veículos e rastreadores (IMEI, ICCID, APN — os dados que hoje estão indevidamente na tela do cliente vêm para cá), status de pagamento, botão de bloqueio/desbloqueio que dispara comando via API do Traccar, e log de comandos enviados. É um back-office clássico, sem complexidade algorítmica — só volume de telas.

**Financeiro (média).** Integração com Asaas ou Cora: gerar cobrança recorrente, receber webhook de pagamento, atualizar status do boleto. A regra de negócio delicada é a régua de inadimplência — depois de quantos dias sem pagar você bloqueia o rastreamento (ou o veículo?). Isso é decisão comercial e jurídica antes de ser técnica; bloquear veículo por inadimplência tem implicações no CDC.

**App (baixa, se PWA).** O rascunho em `/app/` vira PWA instalável com manifest + service worker. Push notification via web push funciona em Android sem loja; iOS suporta desde o 16.4 mas exige instalação à tela inicial. Alternativa pragmática: alertas por WhatsApp, que você já domina do contexto corporativo.

## Escopo do MVP

O corte mínimo que já sustenta um cliente pagante:

- Traccar no ar com os dispositivos migrados;
- login próprio com vínculo cliente → veículos;
- portal consumindo posição real (mapa + endereço);
- admin básico (cadastros, bloqueio/desbloqueio com log);
- cobrança recorrente via Asaas com baixa automática.

Tudo o que estiver além disso está catalogado em [[Funcionalidades]] como evolução.

## Dimensionamento honesto

Para o seu perfil — você mantém sozinho um SaaS com financeiro e estoque há anos — isso é um projeto de **4 a 8 semanas em ritmo parcial** para o MVP acima. A parte genuinamente nova para você é só o ecossistema de rastreamento (protocolo, comportamento dos dispositivos, gestão de chips); todo o resto é padrão de CRUD + billing que você já construiu antes.

## Risco principal: operação, não código

O risco real do projeto não é técnico, é operacional: gestão da frota de chips (recarga, chip queimado, dispositivo que para de reportar) e suporte a cliente com rastreador offline.

Vale desenhar desde o início um alerta no admin de **"dispositivos sem reportar há X horas"** — é o que separa uma operação de rastreamento saudável de uma que descobre o problema quando o cliente liga. Esse mesmo recurso é um dos argumentos mais fortes do pitch (ver [[Requisitos para vendas]]).
