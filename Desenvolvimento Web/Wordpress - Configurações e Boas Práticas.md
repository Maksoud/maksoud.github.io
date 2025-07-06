### [Sumário](<https://maksoud.github.io/Sumário>)

# Wordpress - Configurações e Boas Práticas

Após concluir a instalação do WordPress, é fundamental aplicar medidas básicas de segurança para proteger seu site contra acessos indevidos e vulnerabilidades comuns. Abaixo, listamos algumas boas práticas recomendadas:

## 1. Remover arquivos desnecessários da raiz do WordPress

Alguns arquivos padrões vêm com a instalação do WordPress e **não são mais necessários após a configuração inicial**. Eles podem representar riscos se permanecerem no servidor, pois podem fornecer informações técnicas sensíveis.

**Arquivos que você deve excluir:**

- `wp-config-sample.php` – Arquivo de exemplo da configuração, pode ser usado para deduzir a estrutura do seu `wp-config.php`.
- `readme.html` – Contém informações sobre a versão do WordPress, o que pode facilitar ataques direcionados.
- `license.txt` – Licença do WordPress, não é necessário no ambiente de produção.
- Arquivos `xmlrpc.php` (caso não use) – Se não utilizar aplicativos externos ou pingbacks, esse arquivo pode ser desabilitado ou bloqueado, pois é alvo comum de ataques.
- O arquivo `wp-activate.php` poderá ser removido se você **não está usando multisite** (ou seja, está em uma instalação padrão do WordPress) e **não pretende ativar esse recurso**. Se você estiver usando o **WordPress Multisite com registro de usuários habilitado**, **não remova esse arquivo**. Ele é essencial para o fluxo de ativação de novas contas via e-mail.

---
## 2. Renomear ou proteger o arquivo `wp-config.php`

Esse arquivo contém **informações sensíveis de banco de dados e configurações do site**. Algumas ações recomendadas:

- Mova o `wp-config.php` um diretório acima da raiz (se seu servidor permitir).   
- Aplique permissões restritas:
```
chmod 600 wp-config.php
```

Para garantir a segurança do seu site, algumas medidas precisam ser tomadas através da configuração do servidor Apache e através das restrições de acessos dos arquivos e diretórios do seu servidor. O artigo [Wordpress - Segurança e Correção de Falha de Acesso - Avançado](<https://maksoud.github.io/Produtos%20Digitais/Wordpress%20-%20Seguran%C3%A7a%20e%20Corre%C3%A7%C3%A3o%20de%20Falha%20de%20Acesso%20-%20Avan%C3%A7ado>) eu explico melhor sobre essas configurações.

---
## 3. Alterar o prefixo padrão das tabelas do banco de dados

Se ainda estiver em tempo de configurar o banco de dados, **evite usar o prefixo padrão `wp_`** nas tabelas, substituindo por algo personalizado, como `site123_`, para dificultar ataques de injeção de SQL.

---
## 4. Criar uma conta de administrador com nome personalizado

Evite utilizar nomes óbvios como `admin` para o usuário administrador. Crie um nome exclusivo e com senha forte.

---
## 5. Manter o WordPress, plugins e temas sempre atualizados

Atualizações corrigem falhas de segurança. **Ative as atualizações automáticas ou faça revisões periódicas** para garantir que tudo esteja em dia.

---
## 6. Alterar a rota para o WP-Admin

A URL padrão é amplamente conhecida por bots e scripts maliciosos. Ao alterá-la, você:

- **Reduz a exposição** a ataques automatizados;
- **Evita sobrecarga no servidor** por requisições indevidas;
- Adiciona uma **camada extra de proteção** (não substitui o uso de senhas fortes ou autenticação 2FA, mas complementa).

Uma forma de realizar essa alteração é através do plugin **WPS Hide Login** (leve e confiável).

1. Acesse o painel WordPress > Plugins > Adicionar novo;
2. Procure por **WPS Hide Login** e instale;
3. Após ativar, vá em **Configurações > Geral**;
4. No final da página, defina a nova URL de login (ex: `meu-painel`) e salve;
5. O acesso ao painel passará a ser por `seusite.com/meu-painel`;
6. As URLs antigas (`/wp-login.php` e `/wp-admin`) passam a exibir erro 404.

**Você pode mudar a URL a qualquer momento**, basta atualizar o campo nas configurações.

### ⚠️ Atenção:

- **Nunca apague ou renomeie arquivos do core como `wp-login.php` manualmente**, pois isso **quebra o WordPress**.
- Sempre **anote a nova URL** para não perder o acesso.
- Considere combinar essa prática com **2FA** e **limitação de tentativas de login**.

---
## 7. Plugins Recomendados

Nessa seção eu apresento uma lista de plugins recomendados que utilizo para aprimorar a segurança do site **WordPress**, assim como alguns plugins que irão aprimorar a sua criação de sites.

#### 7.1 All-In-One Security (AIOS) (Segurança)

[All-in-One Security (AIOS)](<https://br.wordpress.org/plugins/all-in-one-wp-security-and-firewall/>) é um plugin essencial para proteger sites WordPress, oferecendo recursos avançados de segurança de forma simples e eficiente.

Com ele, você protege seu site contra **ataques de força bruta**, **bloqueia bots**, ativa um **firewall inteligente (WAF)**, evita **spam em comentários** e impede o roubo de conteúdo com ferramentas como **prevenção de iFrame** e **bloqueio de cópia de texto**.

Tudo isso com uma interface intuitiva e diversas funções gratuitas, tornando-o uma solução indispensável para quem quer manter o WordPress seguro sem complicação.

#### 7.2 Google Authenticator (Segurança)

O plugin [Google Authenticator](<https://br.wordpress.org/plugins/google-authenticator/>) é um plugin de segurança para WordPress que adiciona **autenticação de dois fatores (2FA)** usando o app Google Authenticator no celular.

Com ele, mesmo que alguém descubra sua senha, **não conseguirá acessar seu site sem o código de verificação**, aumentando significativamente a proteção contra invasões.

É possível ativar o 2FA apenas para usuários específicos, como administradores, garantindo segurança sem comprometer a usabilidade.

Ideal para quem busca **reforçar a segurança do login no WordPress** com uma solução prática e confiável.

#### 7.3 Login Lockdown (Segurança)

[Login Lockdown](<https://wordpress.org/plugins/login-lockdown/>) é um plugin de segurança para WordPress que protege seu site contra **ataques de força bruta**, bloqueando automaticamente IPs após várias tentativas de login falhas.

Com recursos como **bloqueio por país**, **log detalhado de tentativas**, **integração com captchas** e **verificação por e-mail (2FA alternativa)**, ele reforça a segurança da área de login de forma prática e eficaz.

Simples de configurar, o plugin é ideal para quem quer **impedir acessos não autorizados** e manter o controle total sobre quem tenta invadir o site.

#### 7.4 Font Awesome

A forma oficial [Font Awesome](<https://br.wordpress.org/plugins/font-awesome/>) e mais prática de adicionar ícones ao seu site WordPress, seja na versão **Free** ou **Pro**.

Com ele, você pode usar ícones modernos e personalizados em **posts, páginas e templates**, incluindo estilos como **Duotone**. O plugin também oferece compatibilidade com versões antigas, resolução de conflitos entre plugins e carregamento via **CDN ou Kit oficial**.

Ideal para quem deseja **melhorar o visual e a comunicação visual do site** com ícones profissionais e atualizados.

#### 7.5 Advanced Custom Fields PRO

O [Advanced Custom Fields](<https://www.advancedcustomfields.com/>) é um plugin indispensável para desenvolvedores WordPress que desejam **personalizar a experiência de edição** no painel do site.

Com ele, é possível **criar e gerenciar campos personalizados** com facilidade, adicionando informações extras em qualquer parte do WordPress — como posts, usuários, mídias, taxonomias e páginas de opções.

Os campos podem ser exibidos em qualquer template do tema com funções práticas e intuitivas, tornando o ACF uma solução poderosa e flexível para **sites dinâmicos e bem estruturados**.

#### 7.6 Elementor Pro

O [Elementor Pro](<https://elementor.com/pro/>) é um dos construtores de páginas mais poderosos para WordPress, ideal para quem deseja criar **sites personalizados, modernos e profissionais** sem escrever uma linha de código.

Com recursos como **widgets avançados de portfólio**, **cabeçalhos e rodapés personalizados**, **efeitos visuais interativos**, **formulários personalizados** e **código/CSS sob medida**, o plugin oferece total liberdade criativa.

Perfeito para quem quer transformar ideias em sites visualmente incríveis, mantendo a **identidade da marca** e a **experiência do usuário** em destaque.

#### 7.7 WP Image Zoom

O [WP Image Zoom](<https://br.wordpress.org/plugins/wp-image-zoooom/>) é um plugin de WordPress que permite adicionar um **efeito de lupa interativo** nas imagens do seu site, realçando detalhes e melhorando a experiência visual do usuário.

Com **diversos tipos de zoom**, efeitos de animação e fade, além de **alta personalização**, o plugin é ideal para destacar produtos, portfólios ou imagens com riqueza de detalhes.

Compatível com **WooCommerce**, páginas e posts, é uma excelente ferramenta para quem busca **valorizar o conteúdo visual** e potencialmente **aumentar as conversões** no site.

#### 7.8 Wordfence

Quando falamos de segurança em WordPress, um dos plugins mais robustos e indispensáveis é o [**Wordfence**](https://br.wordpress.org/plugins/wordfence/). Ele oferece uma **camada poderosa de proteção contra ataques**, monitoramento em tempo real e ferramentas essenciais para blindar o seu site contra invasões.

Combinado com boas práticas de segurança, o Wordfence pode proteger até os pontos mais vulneráveis do WordPress.

#### Boas práticas recomendadas com o uso do Wordfence (e além)

- **Altere o prefixo padrão das tabelas do banco de dados** (`wp_`) para dificultar ataques automatizados de injeção SQL.
- **Mude a URL de login padrão (`/wp-admin`)** para algo único e imprevisível.
- **Altere o ID do primeiro usuário administrador (ID 1)**, que costuma ser o alvo primário em ataques de força bruta.
- **Ative o uso obrigatório de SSL (HTTPS)** para todas as áreas do site, especialmente o painel de login.
- **Implemente reCAPTCHA em todos os formulários**, inclusive de login e comentários, para bloquear robôs e ataques automatizados.
- **Desabilite o login por nome de usuário**, permitindo apenas via e-mail, uma prática simples que dificulta ataques de força bruta.
- **Exija o uso de senhas fortes** para todos os usuários, especialmente administradores e editores.
- **Utilize uma CDN (Content Delivery Network)** para cache de arquivos estáticos — melhora a segurança, a performance e economiza banda.
- **Implemente cache de banco de dados com Redis**, se possível, para reduzir a carga do servidor e acelerar o carregamento.
- **Instale apenas plugins confiáveis**, testados por você ou com ampla reputação. Evite plugins desconhecidos ou abandonados.
- **Ao desenvolver seus próprios plugins**, siga práticas de segurança como:
    - Escapar e sanitizar entradas (`esc_html()`, `sanitize_text_field()`, etc.)
    - Usar `prepare()` nas consultas SQL para evitar injeções
    - Validar permissões antes de executar ações sensíveis

---
### 8. E o mais importante: backups sempre em dia

Mesmo com todas as camadas de segurança aplicadas, nenhuma proteção é infalível. Por isso, **manter backups regulares e automatizados** do seu banco de dados e arquivos é essencial para garantir a recuperação do site em caso de invasão, erro humano ou falha no servidor.

> 🛠️ Dica: combine o **Wordfence** com plugins de backup como **UpdraftPlus** ou **All-in-One WP Migration** para uma estratégia de segurança completa.

---
## Extra: Alerta de falta de módulo **imagick** no WordPress

O módulo **Imagick** é essencial para o processamento avançado de imagens no WordPress. Sua ausência pode afetar funcionalidades como redimensionamento, compressão e manipulação de imagens em plugins e temas.

#### Requisitos

- **Acesso ao servidor com permissão para instalar pacotes.**  
    Caso não tenha, solicite a instalação ao seu provedor de hospedagem.
- **Versão do PHP recomendada: 7.4 ou superior.**  
    Isso garante melhor desempenho e mais segurança para seu site.

#### Como instalar o módulo Imagick no PHP

1. **Instalar o módulo:**
```
sudo apt-get install php-imagick
```

2. **Verificar se o módulo foi instalado com sucesso:**
```
php -m | grep imagick
```
Se a saída mostrar `imagick`, significa que o módulo está ativo.

3. **Reiniciar o servidor Apache para aplicar as mudanças:**
```
sudo systemctl restart apache2
```


[link de compartilhamento](<https://maksoud.github.io/Desenvolvimento%20Web/Wordpress%20-%20Configura%C3%A7%C3%B5es%20e%20Boas%20Pr%C3%A1ticas>)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>