# Instalando e Configurando o Apache no CentOS

#### 1. Atualizar pacotes:
`sudo yum -y update` 

#### 2. Instalar e iniciar o firewall (firewalld):
```bash
yum -y install firewalld
systemctl enable --now firewalld
systemctl status firewalld --no-pager -l
```

#### 3. Liberar HTTP e HTTPS no firewall:
```bash
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --reload
```

#### 4. Instalar o Apache e o módulo SSL:
```bash
sudo yum -y install httpd mod_ssl
```

#### 5. Habilitar e iniciar o serviço do Apache:
```bash
sudo systemctl enable --now httpd
sudo systemctl status httpd --no-pager -l
```

#### 6. Validar que está rodando:
```bash
ss -tulpn | grep -E ':80|:443'
```

#### 7. Teste no navegador:
- Acesse: http://SEU_IP
- Deve aparecer a página padrão do Apache.

```bash
curl -I http://127.0.0.1
```

### Observações rápidas:

- Se você usa o Firewall da Vultr (além do firewalld do servidor), libere também as portas 80 e 443 lá.
- Se “yum” não existir na sua imagem, use “dnf” (veja equivalentes abaixo).

```
sudo dnf -y update
sudo dnf -y install firewalld
sudo systemctl enable --now firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
sudo dnf -y install httpd mod_ssl
sudo systemctl enable --now httpd
sudo systemctl status httpd --no-pager -l
sudo ss -tulpn | grep :80
```

### Arquivo de configuração de segurança (.htaccess)
Coloque esse arquivo na raiz do seu site para proteger de acessos indevidos e manter seu código seguro.

```
# index.html primeiro: o PHP-FPM responde "File not found" para index.php inexistente
DirectoryIndex index.html index.php
Options -Indexes

<IfModule mod_rewrite.c>
	RewriteEngine On

	## 1. BLOQUEIOS (sempre primeiro) ##
	# Dotfiles e dotdirs (.env, .git, .svn, .hg, .htaccess...), exceto .well-known (SSL/ACME)
	RewriteRule (^|/)\.(?!well-known/) - [F,L]
	# Extensões sensíveis
	RewriteRule \.(sql|gz|zip|tar|rar|7z|xlsx|md|lock|log|bak|ini|sh)$ - [F,L,NC]
	# Manifestos e código do servidor Node
	RewriteRule (^|/)(package(-lock)?|composer)\.json$ - [F,L,NC]
	RewriteRule (^|/)(src|node_modules|vendor)(/|$) - [F,L,NC]
	RewriteRule ^js/index\.js$ - [F,L,NC]

	## 2. BASE AUTOMÁTICA (localhost/seu-site ou raiz) ##
	RewriteCond %{REQUEST_URI}::$1 ^(.*?/)(.*)::\2$
	RewriteRule ^(.*)$ - [E=MKP_BASE:%1]

	## 3. URL SEM .php (/contato -> contato.php) ##
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteCond %{REQUEST_FILENAME}.php -f
	RewriteRule ^(.+?)/?$ $1.php [L]

	## 4. FRONT CONTROLLER ##
	RewriteRule ^index\.php$ - [L]
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule . %{ENV:MKP_BASE}index.php [L]
</IfModule>

# Camada independente do mod_rewrite (Apache 2.4+)
<FilesMatch "(^\.|\.(sql|gz|zip|tar|rar|7z|xlsx|md|lock|log|bak|ini|sh)$|^(package(-lock)?|composer)\.json$)">
	Require all denied
</FilesMatch>

# Fallback para dotdirs se mod_rewrite não estiver ativo
<IfModule !mod_rewrite.c>
	RedirectMatch 404 /\.(git|svn|hg|env)(/|$)
</IfModule>
```


[link de compartilhamento](https://correiarodrigues.com.br/notas/desenvolvimento-web/instalando-e-configurando-o-apache/)

<sup><sub>
Renée Maksoud - setembro de 2025
</sub></sup>