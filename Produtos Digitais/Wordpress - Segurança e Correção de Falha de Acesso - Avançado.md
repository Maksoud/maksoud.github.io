### [Sumário](<https://maksoud.github.io/Sumário>)

# Wordpress - Segurança e Correção de Falha de Acesso - Avançado

Nesse artigo eu vou apresentar uma possível solução para a falha *"The requested URL was not found on this server"*. Esse artigo também irá apresentar soluções de segurança dos seus arquivos, ajudando a prevenir invasões e alterações dos seus arquivos na sua instalação do **Wordpress**,

### Alterando o seu arquivo de acessos

Vamos configurar o **Apache2** para garantir a segurança dos seus arquivos. Para isso, abra o arquivo **"/etc/apache2/apache2.conf"** e altere o seu conteúdo como mostrado abaixo:  

```
# Protege a raiz do sistema
<Directory />
	Options None
	AllowOverride None
	Require all denied
</Directory>

# Protege o /usr/share, permitindo acesso somente ao necessário
<Directory /usr/share>
	Options None
	AllowOverride None
	Require all denied
</Directory>

# Libera acesso apenas ao diretório específico onde estão os arquivos públicos
<Directory /var/www/>
	Options -Indexes +FollowSymLinks
	AllowOverride All
	Require all granted
</Directory>

# Adicionar proteção contra execução de scripts fora do diretório web
<FilesMatch "\.(htaccess|htpasswd|ini|phps|fla|psd|log|sh)$">
  Require all denied
</FilesMatch>

# Bloquear acesso a wp-config.php
<Files wp-config.php>
  Require all denied
</Files>

# Bloquear acesso a arquivos .ht*
<FilesMatch "^\.ht">
  Require all denied
</FilesMatch>

# Bloquear execução de PHP em uploads
<Directory "/wp-content/uploads/">
  <FilesMatch "\.php$">
    Require all denied
  </FilesMatch>
</Directory>

# Bloquear XML-RPC (se não usar Jetpack ou apps móveis)
<Files xmlrpc.php>
  Require all denied
</Files>
```

### O que significa:

- **`<Directory />`**: Refere-se ao diretório **raiz do sistema (`/`)**. É uma **medida de segurança** para garantir que ninguém consiga acessar a raiz `/` do sistema via web.
- O diretório **`/usr/share`** pode conter arquivos públicos, como documentações, páginas de exemplo etc. É um local padrão em algumas distros Linux para arquivos estáticos.
- **`Options None`**: Remove _todas_ as permissões, inclusive `FollowSymLinks`, para ser ainda mais restritivo.
- **`Options FollowSymLinks`**: Permite que o Apache siga **links simbólicos**.
- **`Options -Indexes +FollowSymLinks`**:
	- `-Indexes`: desativa listagem de diretórios (muito importante!);
	- `+FollowSymLinks`: necessário para o WordPress e muitos frameworks.
- **`AllowOverride None`**: **Não permite que arquivos `.htaccess`** sobrescrevam configurações neste diretório.
- **`AllowOverride All`**: Aqui está o **ponto mais importante para o WordPress**:
	- Permite que **arquivos `.htaccess` sobrescrevam configurações**, necessário para **URLs amigáveis (permalinks)** e outras regras do WP.
- **`Require all granted`**: Concede acesso a qualquer visitante.
- **`Require all denied`**: **Nega acesso total** a esse diretório para qualquer visitante.

### Importância:

Esse é o **diretório onde seu WordPress está instalado** (ex: `/var/www/html/`). Essa configuração garante que:

- O Apache vai **ler o `.htaccess`** (que o WordPress usa para redirecionamentos, rewrites etc.);
- O acesso ao site via navegador será permitido.

### Remover banners e versões do Apache:

No **`/etc/apache2/conf-enabled/security.conf`**, adicione ou edite:
```
ServerTokens Prod 
ServerSignature Off
```

### Verifique módulos desnecessários com **`apache2ctl -M`**

Desabilite módulos não usados, como:

```
a2dismod autoindex status cgi
```

### Headers de segurança (opcional, mas recomendado)

No seu **`apache2.conf`**, **`000-default.conf`** ou **`.htaccess`**, adicione:
```
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-XSS-Protection "1; mode=block"
Header always set Referrer-Policy "no-referrer-when-downgrade"
Header always set Permissions-Policy "geolocation=(), microphone=()"
```

> Obs: É necessário que o módulo `headers` esteja habilitado:  
> `sudo a2enmod headers`

---

### Criando o arquivo **`.htaccess`**

Esse arquivo fica oculto, por isso o "." no início do seu nome. Ele é responsável por informar ao seu servidor sobre o comportamento de acesso dos diretórios e precisamos alterá-lo ou criá-lo para corrigir a falha e aprimorar a segurança do seu site. Para isso, siga as instruções conforme descrito nos passos a seguir.

Agora nós vamos criar o arquivo. Navegue até a raiz do diretório que está instalado o **Wordpress**, crie um arquivo **'.htaccess'** e preencha o seu conteúdo, conforme sugestão abaixo:

```
# INÍCIO DAS REGRAS DO WORDPRESS

<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]

# Qualquer requisição que não seja para um arquivo ou diretório existente
# será redirecionada para index.php, onde o WP decide o que fazer
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>

# FIM DAS REGRAS DO WORDPRESS
```

---
### Alterando as permissões de acesso dos arquivos e pastas

Nesse passo, precisamos restringir os acessos aos diretórios. Assim como alterar a propriedade dos arquivos e diretórios da instalação do **Wordpress**. Para isso, é necessário digitar os seguintes comandos na raiz da sua instalação:

```
sudo chown -R www-data:www-data wp-admin/
sudo chown -R www-data:www-data wp-includes/
sudo chown -R www-data:www-data wp-content/
sudo chown -R www-data:www-data *.php
sudo chown -R www-data:www-data *.html
sudo chown -R www-data:www-data *.txt
sudo chown -R www-data:www-data .htaccess

sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;

sudo chmod 600 wp-config.php
sudo chmod 775 .htaccess
```

> Para realizar alterações e atualizações no ambiente administrativo do seu Wordpress, é necessário realizar a alteração dessas restrições de acesso dos arquivos e pastas. Não esqueça de configurar novamente após a atualização, garantindo a segurança do seu ambiente.

---
### Corrigindo possíveis falhas de encontrar páginas no Wordpress

Para corrigir esse problema, é necessário apenas alterar entre as opções `"Plain"` e `"Post name"`. Dessa forma, o seu **Wordpress** irá reconfigurar o arquivo de rotas e corrigir o problema. O padrão sugerido para usar é a opção `"Post name"`, os as suas páginas ficarão com uma URL amigável para compartilhamento futuro.

![](https://correiarodrigues.com.br/wp-content/uploads/2021/11/Screen-Shot-2021-11-08-at-20.08.11.png)

--- 
### Conclusão

Agora, esperamos que a segurança do seu site no **Wordpress** esteja ainda mais garantida. É claro que ainda existem plugins como o **Google Authenticator** que irá apoiar na restrição do acesso ao painel administrativo e o plugin **Login Lockdown** que irá bloquear endereços que realizem múltiplas tentativas de acesso.

A segurança é uma preocupação constante e esses passos sugeridos visam te apoiar em um ambiente seguro e disponível para seus sites. Espero ter ajudado!


[link de compartilhamento](<https://maksoud.github.io/Produtos%20Digitais/Wordpress%20-%20Seguran%C3%A7a%20e%20Corre%C3%A7%C3%A3o%20de%20Falha%20de%20Acesso%20-%20Avan%C3%A7ado>)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>