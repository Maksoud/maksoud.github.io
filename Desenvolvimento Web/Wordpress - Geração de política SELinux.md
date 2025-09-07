### [Sumário](<https://maksoud.github.io/Sumário>)

# Geração de política SELinux a partir de negações de AVC (Access Vector Cache)

O "loop" de limpar o log, testar, coletar negações e gerar a política é a metodologia padrão para criar políticas customizadas para aplicações que não são totalmente cobertas pelas políticas padrão do SELinux ou que têm requisitos específicos (como o WordPress). É um processo de tentativa e erro, mas muito eficaz.

Para cada um dos seus sites WordPress hospedados no seu servidor, siga os passos a seguir. Acesse seu servidor Linux via SSH e na raiz dos seus sites execute os comandos conforme explicação.

Limpe o log de auditoria: Isso remove as negações antigas, focando nas novas. 

```
sudo cat /dev/null > /var/log/audit/audit.log
```

Reinicie os serviços: Garanta um estado limpo para a próxima rodada de testes. 

```
sudo systemctl restart httpd 
sudo systemctl restart php-fpm
```

Simule uso intensivo no seu site: Acesse https://[seu-site.com.br]. Faça login, navegue por várias páginas, edite um post, tente subir uma imagem, mexa nas configurações de um plugin, etc. O objetivo é acionar o máximo de operações possíveis.

Gere e instale as novas regras no módulo existente: Este comando vai adicionar as novas negações ao seu arquivo .te existente. 

```
sudo ausearch -c "php-fpm" --raw | audit2allow -M wordpress_final_perms 
```

(Confirme se o arquivo wordpress_final_perms.te e wordpress_final_perms.pp existem e são os que você quer complementar).

Em seguida, instale o módulo atualizado: 

```
sudo semodule -i wordpress_final_perms.pp
```

Verifique o log de auditoria para novas negações: Veja se ainda há AVCs. 

```
sudo ausearch -m AVC -ts today | tail -n 20
```

**Repita:** Se o comando ausearch ainda mostrar negações (type=AVC msg=audit...), volte ao passo 1 e repita todo o processo para o mesmo site. Continue até que o comando de verificação retorne `<no matches>` após o uso intenso do site.


[link de compartilhamento](<https://maksoud.github.io/Desenvolvimento%20Web/Wordpress%20-Geração%20de%20política%20SELinux>)

<sup><sub>
Renée Maksoud - setembro de 2025
</sub></sup>