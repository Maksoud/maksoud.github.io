### [Sumário](<https://maksoud.github.io/Sumário>)

# Hospedando um Site - Avançado

Relacionei a lista de comandos e uma breve explicação da função do comando. Essa configuração foi realizada no **Linux Ubuntu** no servidor da **DigitalOcean** para adicionar novos sites (domínios) em uma máquina virtual contratada.

Não esqueça de registrar o domínio para chamar no IP do seu servidor. Para atribuir o domínio ao projeto no **DigitalOcean**, acesse o menu **Networking** e adicione um registro do tipo **A** com os dados do seu domínio.

Note que no exemplo abaixo eu registrei dois domínios: `site-exemplo` e `site-exemplo2`. Troque os nomes pelo [domínio] do seu site.

---
## Arquivo de configurações

#### /etc/apache2/sites-available/000-default-le-ssl.conf

```
<IfModule mod_ssl.c>
<VirtualHost *:443>
	ServerAdmin webmaster@localhost

	ServerName site-exemplo.com.br
	ServerAlias www.site-exemplo.com.br

	DocumentRoot /var/www/html/site-exemplo

	<Directory /var/www/html/site-exemplo>
		Options FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	 ErrorLog ${APACHE_LOG_DIR}/error_site-exemplo.log
	 CustomLog ${APACHE_LOG_DIR}/access_site-exemplo.log combined

	 ServerAlias site-exemplo.com.br
	 ServerAlias www.site-exemplo.com.br
</VirtualHost>

<VirtualHost *:443>
	ServerAdmin webmaster@localhost

	ServerName site-exemplo2.com.br
	ServerAlias www.site-exemplo2.com.br

	DocumentRoot /var/www/html/site-exemplo2

	<Directory /var/www/html/site-exemplo2>
		Options FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	 ErrorLog ${APACHE_LOG_DIR}/error_site-exemplo2.log              
	 CustomLog ${APACHE_LOG_DIR}/access_site-exemplo2.log combined

	 ServerAlias site-exemplo2.com.br
	 ServerAlias www.site-exemplo2.com.br
</VirtualHost>
</IfModule>
```

#### /etc/apache2/sites-available/000-default.conf

```
# Added to mitigate ABC-2020-1234 vulnerability
UseCanonicalName On

<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	
	ServerName site-exemplo.com.br
	ServerAlias www.site-exemplo.com.br

	DocumentRoot /var/www/html/site-exemplo
	
	<Directory /var/www/html/site-exemplo>
		Options FollowSymLinks
		AllowOverride All
		Require all granted
   </Directory>

	ErrorLog ${APACHE_LOG_DIR}/error_site-exemplo.log
	CustomLog ${APACHE_LOG_DIR}/access_site-exemplo.log combined
	RewriteEngine on
	RewriteCond %{SERVER_NAME} =www.site-exemplo.com.br [OR]
	RewriteCond %{SERVER_NAME} =site-exemplo.com.br
	RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName site-exemplo2.com.br
	ServerAlias www.site-exemplo2.com.br
	DocumentRoot /var/www/html/site-exemplo2

	<Directory /var/www/html/site-exemplo2>
		Options FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error_site-exemplo2.log
	CustomLog ${APACHE_LOG_DIR}/access_site-exemplo2.log combined
	 RewriteEngine on
	 RewriteCond %{SERVER_NAME} =www.site-exemplo2.com.br [OR]
	 RewriteCond %{SERVER_NAME} =site-exemplo2.com.br
	 RewriteRule ˆ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

---
## Gerando o certificado HTTPS

Comando para gerar certificado SSL para HTTPS:

```
sudo certbot --apache -d [domínio] -d www.[domínio]
```

Diretório dos arquivos de validação do certificado:

```
/etc/letsencrypt/live/[domínio]
```

As seguintes linhas serão adicionadas dentro das tags `<VirtualHost>` no seu arquivo `000-default-le-ssl.conf`:

```
 Include /etc/letsencrypt/options-ssl-apache.conf
 SSLCertificateFile /etc/letsencrypt/live/site-exemplo.com.br/fullchain.pem
 SSLCertificateKeyFile /etc/letsencrypt/live/site-exemplo.com.br/privkey.pem
```

---
## Criando os sites

Não se esqueça de criar os diretórios `/var/www/html/site-exemplo` e `/var/www/html/site-exemplo2` com as permissões `755` para diretórios e `644` para arquivos.

Comando para criar e redefinir permissões de pastas:

```
mkdir /var/www/html/site-exemplo
echo "Hello World" | tee /var/www/html/site-exemplo/index.html

sudo chown -R www-data:www-data /var/www/html/site-exemplo/
sudo find /var/www/html/site-exemplo -type d -exec chmod 755 {} \;
sudo find /var/www/html/site-exemplo -type f -exec chmod 644 {} \;
```

---
## Aplicando configurações

Comando para reiniciar o servidor Apache:

```
sudo systemctl restart apache2
```

Caso você tenha alguma mensagem de erro, tente parar o servidor apache e iniciá-lo novamente. Deixe nos comentários suas dúvidas e se funcionou pra você.

> **DICA** É possível criar um arquivo para cada site, mantendo sempre as tags `<VirtualHost>` e `<IfModule>` (no caso do arquivo `000-default-le-ssl.conf`) conforme nos exemplos acima.

> Será necessário executar o comando `a2dissite 000-default.conf` e `a2dissite default-ssl-conf` para desvincular esses arquivos da pasta `/etc/apache2/sites-enabled/`. 

Não se esqueça de adicionar os novos com o comando `a2ensite site-exemplo.conf`. Os 
arquivos `.conf` da pasta `sites-available` precisam estar dentro da pasta `sites-enabled`, caso não estejam execute o seguinte comando para criar um link desses arquivos e disponibilizar o site.

```
ln -s /etc/apache2/sites-available/site-exemplo.conf /etc/apache2/sites-enabled/
``` 

Agora o gerenciamento fica muito mais simples. Para retirar um site do ar, basta remover o link da pasta `sites-enabled`.


[link de compartilhamento](<https://maksoud.github.io/Produtos%20Digitais/Hospedando%20um%20Site%20-%20Avan%C3%A7ado>)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>