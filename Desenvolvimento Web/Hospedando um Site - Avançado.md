# Hospedando um Site - Avançado

Relacionei a lista de comandos e uma breve explicação da função do comando. Essa configuração foi realizada no **Linux Ubuntu** no servidor da **DigitalOcean** para adicionar novos sites (domínios) em uma máquina virtual contratada.

Não esqueça de registrar o domínio para chamar no IP do seu servidor. Para atribuir o domínio ao projeto no **DigitalOcean**, acesse o menu **Networking** e adicione um registro do tipo **A** com os dados do seu domínio.

Note que no exemplo abaixo eu registrei dois domínios: `site-exemplo` e `site-exemplo2`. Troque os nomes pelo [domínio] do seu site.

---
## Arquivo de configurações do Apache

O Apache organiza os sites hospedados em seu servidor através de arquivos chamados **Virtual Hosts**, que ficam localizados no diretório:

```
/etc/apache2/sites-available/
```

Dois dos arquivos mais comuns nesse diretório são:

- **`000-default.conf`**: responsável pelas configurações do **acesso via HTTP (porta 80)**;
- **`000-default-le-ssl.conf`**: criado automaticamente pelo Certbot, responsável pelas configurações do **acesso via HTTPS (porta 443)** com certificado SSL do Let's Encrypt.

Esses arquivos definem como o servidor Apache deve responder às requisições feitas ao seu domínio, associando o domínio a um diretório específico no sistema, habilitando ou não o uso de SSL, redirecionamentos, permissões, logs, entre outros.

A seguir, mostrarei como esses arquivos devem estar configurados corretamente para garantir o **funcionamento pleno e seguro** do seu site em ambiente de produção, com suporte a HTTPS e redirecionamento automático.

#### `/etc/apache2/sites-available/000-default-le-ssl.conf`

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

#### `/etc/apache2/sites-available/000-default.conf`

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
## Gerando o certificado HTTPS com Certbot (Let's Encrypt)

A utilização de certificados SSL é essencial para garantir a segurança e a credibilidade do seu site. Com o **Certbot**, uma ferramenta oficial do Let's Encrypt, é possível gerar certificados gratuitos e automáticos para o Apache de forma prática.

### Instalação do Certbot (caso ainda não esteja instalado)

Antes de gerar o certificado, certifique-se de ter o Certbot e o plugin do Apache instalados:

```
sudo apt update
sudo apt install certbot python3-certbot-apache
```

### Comando para gerar o certificado

Execute o comando abaixo substituindo `[domínio]` pelo endereço real do seu site:
```
sudo certbot --apache -d [dominio.com.br] -d www.[dominio.com.br]
```

Este comando:

- Realiza a verificação de propriedade do domínio;    
- Ajusta automaticamente os arquivos de configuração do Apache;
- Instala o certificado SSL e configura o redirecionamento para HTTPS.

> 💡 Você pode incluir quantos subdomínios quiser com `-d subdominio.exemplo.com`.

### Onde os certificados são salvos

Após a emissão, os certificados ficam armazenados em:

```
/etc/letsencrypt/live/[dominio.com.br]/
```

Este diretório contém:

- `fullchain.pem`: o certificado completo (incluindo o certificado da autoridade).
- `privkey.pem`: a chave privada associada ao certificado.

### Configuração automática no Apache

O Certbot irá atualizar (ou criar) automaticamente o arquivo:

```
/etc/apache2/sites-available/000-default-le-ssl.conf
```

E incluirá as seguintes linhas dentro do bloco `<VirtualHost *:443>`:

```
Include /etc/letsencrypt/options-ssl-apache.conf 
SSLCertificateFile /etc/letsencrypt/live/site-exemplo.com.br/fullchain.pem 
SSLCertificateKeyFile /etc/letsencrypt/live/site-exemplo.com.br/privkey.pem
```

### Renovação automática

O Certbot já configura por padrão a renovação automática dos certificados, mas é sempre bom validar com:

```
sudo certbot renew --dry-run
```

## Redirecionamento automático de HTTP para HTTPS

Após a instalação do certificado SSL, é importante garantir que todas as requisições feitas via HTTP sejam automaticamente redirecionadas para HTTPS. Isso melhora a segurança e evita problemas com conteúdos mistos (mixed content).

### Redirecionamento via Certbot (automático)

Ao rodar o comando `certbot --apache`, o Certbot geralmente pergunta:

> "Gostaria de redirecionar todas as requisições HTTP para HTTPS?"

Se você respondeu “Sim”, ele já configura o redirecionamento automaticamente no seu arquivo de virtual host.
### Redirecionamento manual no Apache

Caso prefira configurar manualmente, edite o arquivo do Apache para o VirtualHost na porta 80 (`000-default.conf`) e adicione o seguinte bloco:

```
<VirtualHost *:80>
	ServerName www.site-exemplo.com.br
	ServerAlias site-exemplo.com.br
	Redirect permanent / https://www.site-exemplo.com.br/ 
</VirtualHost>`
```

Essa instrução envia todas as conexões HTTP diretamente para o HTTPS correspondente com código de status 301 (_permanent redirect_).

---
## Criando os sites

O Apache, por padrão, utiliza o diretório `/var/www/html/` como **raiz dos arquivos públicos da web**. Isso significa que todos os arquivos do seu site devem estar organizados dentro dessa pasta, em subdiretórios que representem cada domínio ou subdomínio configurado.

Para uma estrutura clara e organizada, é recomendável criar uma **pasta para cada site**, nomeando-a com base no domínio correspondente. Por exemplo:

- O site `site-exemplo.com.br` deve ter seus arquivos em:  
    `/var/www/html/site-exemplo.com.br/`
- Já `site-exemplo2.com.br` deve estar em:  
    `/var/www/html/site-exemplo2.com.br/`

Essa estrutura facilita a administração, manutenção e aplicação de permissões específicas por site, além de alinhar com os Virtual Hosts do Apache.

### Criando diretórios e aplicando permissões seguras

Utilize os comandos abaixo para criar o diretório do site, adicionar um arquivo de teste (`index.html`) e aplicar permissões recomendadas:

```
# Cria a pasta do site
mkdir /var/www/html/site-exemplo.com.br

# Cria um arquivo simples para teste
echo "Hello World" | tee /var/www/html/site-exemplo.com.br/index.html

# Define o dono como o usuário do Apache
sudo chown -R www-data:www-data /var/www/html/site-exemplo.com.br/

# Define permissões: 755 para pastas e 644 para arquivos
sudo find /var/www/html/site-exemplo.com.br -type d -exec chmod 755 {} \;
sudo find /var/www/html/site-exemplo.com.br -type f -exec chmod 644 {} \;
```

Essas permissões garantem que:

- O Apache possa **ler e executar os diretórios**;
- Os arquivos estejam **seguros contra modificações não autorizadas**;
- Os conteúdos estejam acessíveis via navegador, sem comprometer a segurança do servidor.

---
### Ativando os arquivos de sites (Virtual Hosts)

O Apache separa os sites disponíveis em dois diretórios:

- **`sites-available`**: onde ficam todos os arquivos `.conf` com configurações de sites;
- **`sites-enabled`**: onde ficam os links simbólicos para os sites que realmente estão **ativos** no servidor.

#### ✅ Para ativar um site:

```
sudo a2ensite site-exemplo.conf
```
#### ❌ Para desativar um site:

```
sudo a2dissite site-exemplo.conf
```

Isso cria (ou remove) automaticamente os links simbólicos de `/etc/apache2/sites-enabled/`. Mas também é possível fazer manualmente através do comando abaixo:

```
sudo ln -s /etc/apache2/sites-available/site-exemplo.conf /etc/apache2/sites-enabled/
```

---
### Reiniciando o Apache

Use o seguinte comando para reiniciar o serviço do Apache:
```
sudo systemctl restart apache2
```

Se ocorrer alguma falha ou mensagem de erro, você pode tentar **parar e iniciar novamente**:

```
sudo systemctl stop apache2 sudo systemctl start apache2
```

> 💡 Dica: utilize `sudo systemctl status apache2` para verificar o status atual do serviço e diagnosticar possíveis erros.


[link de compartilhamento](https://correiarodrigues.com.br/notas/desenvolvimento-web/hospedando-um-site-avancado/)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>