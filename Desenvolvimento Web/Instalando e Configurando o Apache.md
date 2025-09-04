### [Sumário](<https://maksoud.github.io/Sumário>)

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



[link de compartilhamento](<https://maksoud.github.io/Desenvolvimento%20Web/Instalando%20e%20Configurando%20o%20Apache>)

<sup><sub>
Renée Maksoud - setembro de 2025
</sub></sup>