# Funcionalidades de um Sistema de Rastreamento Completo

> Catálogo de referência do que um software de rastreamento veicular completo precisa ter — serve tanto de checklist de construção quanto de roteiro do que citar numa conversa de venda.
>
> A marcação **[MVP]** indica o que precisa existir na primeira versão vendável; o restante é evolução planejada. O corte do MVP está justificado em [[Estrutura]].
>
> Notas relacionadas: [[Estrutura]] · [[Custos de Infraestrutura]] · [[Requisitos para vendas]]

## Gestão de clientes e contratos

- **Cadastro completo do cliente** **[MVP]**: dados pessoais/empresariais, documentos, endereço, contatos e vínculo com um ou mais veículos, com busca por nome, CPF/CNPJ ou placa.
- **Gestão de contratos e planos** **[MVP]**: plano contratado, valor, dia de vencimento, data de adesão, status (ativo, suspenso, cancelado) e histórico de alterações.
- **Visão 360 do cliente**: numa tela só, veículos, situação financeira, últimos atendimentos e comandos executados — para o atendente resolver qualquer ligação sem trocar de sistema.

## Gestão de rastreadores e chips

- **Inventário de equipamentos** **[MVP]**: modelo, IMEI, firmware, status (estoque, instalado, manutenção, defeito) e histórico de qual veículo/cliente cada aparelho já atendeu.
- **Gestão de chips M2M** **[MVP]**: ICCID, número, operadora, APN e vínculo chip-rastreador, com controle de troca e reposição.
- **Alerta de dispositivo silencioso** **[MVP]**: painel de aparelhos sem reportar há mais de X horas — detectar o problema antes do cliente ligar. ==Argumento forte de pitch: reduz churn e chamados.==

## Operação e monitoramento

- **Mapa da frota completa** **[MVP]**: todos os veículos da carteira em tela única, com filtros por status, cliente e região.
- **Bloqueio e desbloqueio remoto** **[MVP]**: com registro de quem executou, quando e por quê (trilha de auditoria — importante juridicamente em caso de contestação).
- **Histórico de posições e trajetos** por veículo e período, com exportação.
- **Alertas configuráveis**: ignição fora de horário, velocidade excedida, saída de área (geofence/cerca eletrônica), bateria desconectada.

## Financeiro

- **Cobrança recorrente automatizada** **[MVP]**: geração de boleto/Pix por cliente, baixa automática via webhook do banco, segunda via pelo próprio portal do cliente (menos ligação de cobrança).
- **Régua de inadimplência**: visão de quem está em atraso, há quantos dias, com ações graduais configuráveis (lembrete → suspensão de acesso ao portal → tratativa comercial).
- **Relatório de receita**: faturamento mensal, inadimplência, cancelamentos e projeção da carteira.

> [!warning] Decisão comercial e jurídica antes de técnica
> Até onde vai a régua: suspender o acesso ao portal é uma coisa; bloquear o veículo por inadimplência é outra, com implicações no CDC. Definir isso com o cliente antes de implementar.

## Comunicação com o cliente

- **Notificações automáticas**: aviso de vencimento, confirmação de pagamento e alertas do veículo por push no app e/ou WhatsApp.
- **Canal de suporte integrado** **[MVP]**: botão de WhatsApp no portal do cliente, direcionado para o atendimento da empresa.

## Segurança e administração

- **Perfis de acesso**: administrador, atendente e financeiro, cada um vendo só o que precisa.
- **Log de auditoria** **[MVP]**: toda ação sensível (bloqueio, alteração cadastral, cancelamento) registrada com usuário e data/hora.
- **Dados operacionais protegidos** **[MVP]**: APN, ICCID e configurações técnicas visíveis só no admin, nunca no portal do cliente — argumento de segurança contra sequestro de rastreador.
