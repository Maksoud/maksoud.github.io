Atue como um **especialista sênior em Application Security, PHP Security, Secure Code Review e OWASP**, com experiência prática em auditoria de aplicações PHP em produção.

Sua tarefa é realizar uma **auditoria de segurança completa deste projeto PHP**, analisando o código-fonte, configurações, dependências, autenticação, APIs, banco de dados, uploads, sessões e fluxos de autorização.

## OBJETIVO

Identificar vulnerabilidades reais, falhas de implementação, configurações inseguras e riscos que possam permitir:

- acesso não autorizado;
- vazamento de informações;
- comprometimento de contas;
- alteração ou exclusão indevida de dados;
- execução de código;
- acesso ao servidor;
- comprometimento do banco de dados;
- escalada de privilégios;
- abuso de APIs;
- comprometimento de usuários ou administradores.

Não faça uma análise superficial.

Analise o projeto como se ele fosse ser publicado em **ambiente de produção acessível pela internet**.

---

# 1. RECONHECIMENTO DA APLICAÇÃO

Antes de procurar vulnerabilidades, identifique:

- versão do PHP;
- framework utilizado;
- arquitetura do projeto;
- estrutura de diretórios;
- pontos de entrada da aplicação;
- arquivos públicos;
- arquivos administrativos;
- APIs;
- endpoints;
- rotas;
- controllers;
- models;
- middlewares;
- autenticação;
- banco de dados utilizado;
- bibliotecas externas;
- dependências Composer;
- serviços externos;
- webhooks;
- sistema de upload;
- armazenamento de arquivos;
- jobs/cron;
- comandos CLI;
- integrações externas;
- arquivos de configuração;
- variáveis de ambiente.

Crie primeiro um pequeno **mapa da superfície de ataque** da aplicação.

---

# 2. INJEÇÃO SQL

Analise todas as operações envolvendo banco de dados.

Procure por:

- SQL construído através de concatenação de strings;
- parâmetros inseridos diretamente em queries;
- uso incorreto de PDO;
- uso incorreto de prepared statements;
- queries dinâmicas;
- ORDER BY dinâmico;
- LIMIT/OFFSET manipulável;
- nomes de tabelas ou colunas vindos do usuário;
- filtros construídos dinamicamente;
- consultas raw;
- stored procedures inseguras.

Para cada ocorrência suspeita, determine se existe realmente possibilidade de SQL Injection.

---

# 3. XSS

Procure vulnerabilidades de:

- Stored XSS;
- Reflected XSS;
- DOM XSS, caso exista JavaScript no projeto.

Analise dados vindos de:

- GET;
- POST;
- cookies;
- banco de dados;
- APIs;
- parâmetros de URL;
- headers;
- uploads;
- campos administrativos.

Verifique se a saída HTML está sendo escapada corretamente.

Analise especialmente:

- echo;
- print;
- printf;
- templates;
- atributos HTML;
- JavaScript inline;
- URLs;
- HTML armazenado no banco.

Não considere apenas a entrada do dado. Analise principalmente **onde o dado é renderizado**.

---

# 4. AUTENTICAÇÃO

Analise completamente o sistema de login.

Verifique:

- armazenamento de senhas;
- password_hash();
- password_verify();
- algoritmos de hash;
- redefinição de senha;
- tokens de recuperação;
- expiração de tokens;
- reutilização de tokens;
- enumeração de usuários;
- brute force;
- credential stuffing;
- rate limiting;
- bloqueio de contas;
- autenticação administrativa;
- sessões persistentes;
- logout;
- invalidação de sessões;
- remember-me;
- autenticação de APIs.

Procure maneiras pelas quais um atacante poderia:

- entrar sem senha;
- assumir uma conta;
- reutilizar token;
- manipular sessão;
- descobrir usuários existentes;
- acessar conta administrativa.

---

# 5. AUTORIZAÇÃO E CONTROLE DE ACESSO

Esta parte deve receber atenção especial.

Procure:

- IDOR / BOLA;
- Broken Access Control;
- falta de verificação de propriedade do recurso;
- acesso horizontal entre usuários;
- acesso vertical;
- privilege escalation;
- endpoints administrativos sem proteção;
- validações feitas apenas no frontend;
- alteração de IDs pela URL;
- alteração de user_id;
- account_id;
- tenant_id;
- company_id;
- organization_id;
- role;
- permission;
- admin;
- ownership.

Para cada endpoint relevante, pergunte:

> "Um usuário autenticado poderia alterar algum parâmetro e acessar ou modificar dados pertencentes a outro usuário?"

E:

> "Um usuário comum poderia executar alguma ação reservada a administradores?"

---

# 6. CSRF

Analise todas as operações que alteram estado.

Exemplos:

- criar;
- editar;
- excluir;
- alterar senha;
- alterar email;
- pagamentos;
- configurações;
- usuários;
- permissões;
- uploads.

Verifique existência e validação correta de tokens CSRF.

Considere também cookies SameSite.

---

# 7. UPLOAD DE ARQUIVOS

Faça uma análise rigorosa de qualquer funcionalidade de upload.

Verifique:

- extensão;
- MIME type;
- conteúdo real do arquivo;
- tamanho;
- nome do arquivo;
- renomeação;
- path traversal;
- double extensions;
- arquivos PHP;
- .phtml;
- .phar;
- .htaccess;
- SVG;
- HTML;
- scripts;
- arquivos executáveis.

Determine:

- onde os arquivos são armazenados;
- se ficam dentro do webroot;
- se podem ser executados;
- se podem sobrescrever arquivos;
- se o nome original é utilizado;
- se existe possibilidade de path traversal.

Avalie explicitamente risco de **Remote Code Execution através de upload**.

---

# 8. FILE INCLUSION E PATH TRAVERSAL

Procure dados controlados pelo usuário chegando a:

- include;
- include_once;
- require;
- require_once;
- fopen;
- file_get_contents;
- readfile;
- unlink;
- copy;
- rename;
- glob;
- ZipArchive;
- manipulação de caminhos.

Procure:

- LFI;
- RFI;
- directory traversal;
- leitura arbitrária de arquivos;
- escrita arbitrária;
- exclusão arbitrária.

---

# 9. COMMAND INJECTION / RCE

Procure utilização de:

- exec();
- shell_exec();
- system();
- passthru();
- popen();
- proc_open();
- backticks;
- eval();
- assert() inseguro;
- preg_replace legado com execução;
- chamadas a shell;
- scripts externos.

Faça rastreamento da origem dos parâmetros utilizados.

Determine se algum input controlável externamente pode alcançar essas funções.

---

# 10. SSRF

Procure funcionalidades que realizem requisições HTTP baseadas em parâmetros externos.

Exemplos:

- cURL;
- file_get_contents() com URL;
- Guzzle;
- webhooks;
- importadores;
- previews;
- download remoto;
- processamento de imagens;
- APIs proxy.

Avalie se um atacante poderia acessar:

- localhost;
- 127.0.0.1;
- serviços internos;
- rede privada;
- metadata services;
- portas internas;
- endpoints administrativos.

---

# 11. SESSÕES E COOKIES

Analise:

- session_start;
- regeneração de session ID;
- session fixation;
- session hijacking;
- expiração;
- logout;
- armazenamento de sessão;
- cookies.

Verifique os atributos:

- HttpOnly;
- Secure;
- SameSite.

Verifique também se informações sensíveis são armazenadas indevidamente em cookies.

---

# 12. JWT E TOKENS

Caso existam JWTs ou outros tokens, analise:

- algoritmo;
- assinatura;
- segredo;
- validação;
- expiração;
- issuer;
- audience;
- rotação;
- revogação;
- refresh tokens;
- reutilização;
- armazenamento.

Procure também possibilidade de:

- token forgery;
- token replay;
- algoritmo inadequado;
- segredo fraco;
- ausência de validação de assinatura.

---

# 13. DESSERIALIZAÇÃO

Procure:

- unserialize();
- objetos serializados;
- dados serializados armazenados em cookies;
- sessões;
- parâmetros externos;
- cache.

Avalie risco de PHP Object Injection e gadget chains.

---

# 14. MASS ASSIGNMENT

Analise endpoints de criação e atualização.

Procure código semelhante a:

- preencher objetos diretamente com $_POST;
- update($request->all());
- create($request->all());
- conversão automática de JSON para entidade/model;
- atribuição dinâmica de propriedades.

Verifique se campos sensíveis poderiam ser modificados, como:

- role;
- admin;
- permissions;
- user_id;
- owner_id;
- tenant_id;
- status;
- balance;
- price;
- credit;
- plan.

---

# 15. API SECURITY

Analise todas as APIs quanto a:

- autenticação;
- autorização;
- BOLA;
- IDOR;
- rate limiting;
- enumeração;
- mass assignment;
- exposição excessiva de dados;
- validação de parâmetros;
- paginação;
- filtros;
- endpoints administrativos;
- tokens;
- CORS.

Mapeie endpoints particularmente críticos.

---

# 16. CORS

Analise:

- Access-Control-Allow-Origin;
- Access-Control-Allow-Credentials;
- origens dinâmicas;
- reflexão do Origin;
- wildcard;
- APIs autenticadas.

Identifique configurações que permitam sites externos abusarem da sessão do usuário.

---

# 17. HEADERS HTTP

Verifique se a aplicação deveria implementar ou melhorar:

- Content-Security-Policy;
- X-Content-Type-Options;
- Referrer-Policy;
- Permissions-Policy;
- Strict-Transport-Security;
- frame-ancestors / proteção contra clickjacking.

Considere o funcionamento real da aplicação antes de recomendar políticas excessivamente restritivas.

---

# 18. EXPOSIÇÃO DE INFORMAÇÕES

Procure exposição de:

- stack traces;
- erros PHP;
- phpinfo();
- debug;
- var_dump();
- print_r();
- logs;
- SQL errors;
- caminhos do servidor;
- credenciais;
- tokens;
- API keys;
- dados pessoais;
- informações internas.

---

# 19. SEGREDOS E CREDENCIAIS

Procure por:

- senhas;
- tokens;
- API keys;
- private keys;
- JWT secrets;
- database credentials;
- SMTP credentials;
- cloud credentials;
- chaves de pagamento;
- webhook secrets.

Analise:

- arquivos PHP;
- .env;
- configs;
- backups;
- arquivos de teste;
- scripts;
- documentação;
- arquivos JSON/YAML/XML;
- histórico ou dumps presentes no projeto.

**Nunca reproduza integralmente um segredo encontrado no relatório. Mascare-o.**

---

# 20. ARQUIVOS SENSÍVEIS PUBLICAMENTE ACESSÍVEIS

Procure riscos relacionados a:

- .env;
- .git;
- composer.json;
- composer.lock;
- backups;
- .sql;
- .zip;
- .tar;
- logs;
- arquivos temporários;
- phpinfo;
- config.php;
- dumps;
- arquivos antigos;
- .bak;
- .old;
- swap files.

Determine quais deles poderiam estar dentro do diretório público.

---

# 21. CONFIGURAÇÃO PHP

Analise configurações relevantes como:

- display_errors;
- error_reporting;
- expose_php;
- allow_url_include;
- allow_url_fopen;
- session.cookie_secure;
- session.cookie_httponly;
- session.cookie_samesite;
- session.use_strict_mode;
- upload_max_filesize;
- post_max_size.

Não classifique uma configuração como vulnerabilidade sem explicar o impacto concreto naquele projeto.

---

# 22. DEPENDÊNCIAS

Analise:

- composer.json;
- composer.lock.

Identifique:

- bibliotecas desatualizadas;
- bibliotecas abandonadas;
- versões potencialmente vulneráveis;
- pacotes desnecessários;
- dependências de desenvolvimento presentes em produção.

Quando não puder confirmar se uma versão específica possui CVE conhecida, marque:

**"Necessita verificação externa de vulnerabilidades da dependência."**

Não invente CVEs.

---

# 23. CRIPTOGRAFIA

Procure:

- MD5;
- SHA1 para senhas;
- criptografia caseira;
- chaves hardcoded;
- IVs fixos;
- ECB;
- geração insegura de números aleatórios;
- rand();
- mt_rand() em contextos de segurança.

Prefira:

- random_bytes();
- random_int();
- password_hash();
- password_verify();

quando aplicável.

---

# 24. LOGS E AUDITORIA

Verifique se ações críticas deixam registros adequados.

Exemplos:

- login;
- falhas de login;
- reset de senha;
- alteração de email;
- alteração de permissões;
- exclusão;
- ações administrativas;
- alterações financeiras;
- mudanças de configuração.

Também verifique se os logs armazenam indevidamente:

- senhas;
- tokens;
- cookies;
- dados pessoais;
- cartões;
- credenciais.

---

# 25. LÓGICA DE NEGÓCIO

Não procure apenas vulnerabilidades técnicas.

Analise também possíveis abusos de lógica.

Exemplos:

- alterar preço enviado pelo frontend;
- alterar quantidade;
- reutilizar cupom;
- repetir operação;
- modificar status;
- executar ação fora de ordem;
- repetir pagamento;
- manipular plano;
- alterar saldo;
- alterar ID de usuário;
- executar endpoint diretamente.

Considere cenários em que um usuário legítimo tenta manipular o funcionamento da aplicação.

---

# 26. RACE CONDITIONS

Identifique operações críticas que possam ser executadas simultaneamente e causar:

- duplicação;
- saldo negativo;
- uso repetido de benefício;
- pagamento duplicado;
- criação duplicada;
- inconsistência de estado.

---

# 27. WEBHOOKS

Caso existam webhooks, analise:

- autenticação;
- assinatura;
- segredo;
- timestamp;
- prevenção contra replay;
- idempotência;
- validação do payload;
- origem da requisição;
- manipulação de eventos.

---

# 28. REDIRECTS

Procure open redirects em parâmetros como:

- redirect;
- return;
- return_url;
- next;
- callback;
- url;
- continue.

---

# 29. OWASP

Compare os resultados principalmente com categorias relevantes do:

- OWASP Top 10;
- OWASP API Security;
- CWE.

Utilize essas classificações como referência, mas priorize a vulnerabilidade concreta encontrada no código.

---

# METODOLOGIA OBRIGATÓRIA

Para cada possível vulnerabilidade:

1. Identifique a **fonte do dado controlável externamente**.
2. Acompanhe o fluxo desse dado.
3. Identifique validações e sanitizações existentes.
4. Identifique o ponto sensível onde o dado é utilizado.
5. Determine se as proteções existentes realmente impedem exploração.
6. Somente então classifique como vulnerabilidade.

Evite falsos positivos.

Não classifique simplesmente uma função perigosa como vulnerabilidade sem demonstrar que existe um caminho de dados explorável.

---

# CLASSIFICAÇÃO DE SEVERIDADE

Classifique cada problema como:

🔴 **CRÍTICO**
Possibilidade de comprometimento completo, RCE, takeover administrativo, SQL Injection grave, bypass completo de autenticação ou exposição massiva de dados.

🟠 **ALTO**
Acesso significativo não autorizado, IDOR relevante, privilege escalation, stored XSS privilegiado, alteração significativa de dados ou exposição relevante.

🟡 **MÉDIO**
Impacto limitado que exige condições específicas ou possui alcance reduzido.

🔵 **BAIXO**
Hardening, exposição limitada ou problema com baixo impacto direto.

⚪ **INFORMATIVO**
Melhoria recomendada sem vulnerabilidade diretamente explorável demonstrada.

---

# NÍVEL DE CONFIANÇA

Para cada achado informe também:

- **CONFIRMADO**
- **ALTA PROBABILIDADE**
- **NECESSITA VALIDAÇÃO**
- **POSSÍVEL / INCONCLUSIVO**

Não apresente uma hipótese como vulnerabilidade confirmada.

---

# FORMATO DO RELATÓRIO

Para cada vulnerabilidade utilize:

## [ID] Nome da vulnerabilidade

**Severidade:**  
Crítico / Alto / Médio / Baixo / Informativo

**Confiança:**  
Confirmado / Alta probabilidade / Necessita validação / Possível

**CWE:**  
Caso aplicável.

**OWASP:**  
Caso aplicável.

**Arquivo:**  
`caminho/do/arquivo.php`

**Linha(s):**  
Informe quando puder determinar.

**Código afetado:**
```php
// apenas o trecho estritamente necessário
```

**Descrição:**  
Explique o problema tecnicamente.

**Origem do dado:**  
Explique de onde vem o dado potencialmente controlável.

**Fluxo:**  
Entrada → processamento → ponto vulnerável.

**Cenário de exploração:**  
Descreva conceitualmente como a falha poderia ser abusada, sem realizar ações destrutivas contra sistemas reais.

**Impacto:**  
Explique o que um atacante poderia conseguir.

**Pré-requisitos:**  
Informe o que seria necessário para explorar.

**Correção recomendada:**  
Explique exatamente como corrigir.

**Exemplo seguro de implementação:**
```php
// implementação corrigida
```

**Prioridade de correção:**  
Imediata / Alta / Normal / Baixa.

---

# AO FINAL DA AUDITORIA

Produza:

## 1. RESUMO EXECUTIVO

Informe:

- quantidade de vulnerabilidades críticas;
- altas;
- médias;
- baixas;
- informativas;
- nível geral de risco da aplicação.

## 2. TOP 10 RISCOS

Liste os dez problemas que devem receber prioridade.

## 3. SUPERFÍCIES MAIS CRÍTICAS

Exemplo:

- autenticação;
- painel administrativo;
- API;
- uploads;
- pagamentos;
- banco de dados;
- integrações externas.

## 4. PLANO DE CORREÇÃO

Divida em:

### P0 — Corrigir imediatamente
Problemas críticos.

### P1 — Corrigir antes de produção
Problemas altos.

### P2 — Corrigir em curto prazo
Problemas médios.

### P3 — Hardening
Problemas baixos e melhorias.

## 5. PONTOS QUE EXIGEM TESTE DINÂMICO

Liste problemas que não podem ser confirmados somente através da análise estática do código.

## 6. PONTOS QUE PARECEM SEGUROS

Também informe mecanismos importantes que foram corretamente implementados.

Isso é necessário para evitar um relatório que mostre apenas problemas e não reconheça controles existentes.

---

# REGRAS IMPORTANTES

- Não invente vulnerabilidades.
- Não invente arquivos.
- Não invente linhas de código.
- Não invente endpoints.
- Não invente CVEs.
- Não considere toda entrada de usuário automaticamente vulnerável.
- Analise validações já existentes.
- Diferencie vulnerabilidade de melhoria de segurança.
- Diferencie vulnerabilidade confirmada de hipótese.
- Priorize impacto real.
- Considere o contexto completo da aplicação.
- Antes de concluir que existe uma vulnerabilidade, procure funções, classes, middlewares ou validações em outros arquivos que possam proteger aquele fluxo.
- Faça análise entre múltiplos arquivos quando necessário.
- Se alguma parte relevante do projeto não estiver disponível, informe exatamente o que falta.

Não execute ataques destrutivos nem tente comprometer sistemas externos ou de produção.

O objetivo é **defesa, revisão de código e correção de vulnerabilidades**.

---

# INÍCIO

Comece pela estrutura do projeto.

Primeiro apresente:

1. tecnologia e arquitetura identificadas;
2. superfície de ataque;
3. arquivos/componentes de maior risco;
4. estratégia de auditoria que será usada.

Depois faça a análise detalhada, priorizando primeiro:

**autenticação → autorização → endpoints/API → banco de dados → uploads → execução de comandos/arquivos → dados sensíveis → lógica de negócio → configurações e hardening.**

<sup><sub>
Cristian John - outubro de 2026
</sub></sup>