### [Sumário](<https://maksoud.github.io/Sumário>)

# Agendamento de Tarefas no Linux com CRONTAB

O **Crontab** é uma ferramenta nativa do Linux utilizada para **agendar tarefas automáticas** que são executadas em intervalos regulares ou em horários específicos. Para desenvolvedores e administradores de sistemas web, o uso do Crontab representa uma solução **eficiente, confiável e leve** para automatizar processos rotineiros — sem depender de ferramentas externas ou interfaces gráficas.

Em aplicações web, o Crontab é amplamente utilizado para:

- **Executar scripts PHP, Python ou Shell** para atualizações periódicas de dados;
- **Importar ou exportar arquivos** em horários programados (como integração com APIs, backups ou geração de relatórios);
- **Enviar e-mails automáticos** com notificações ou resumos;
- **Limpar caches, logs ou arquivos temporários**, mantendo o desempenho do servidor;
- **Monitorar serviços** e reiniciar processos em caso de falha.

Ao configurar tarefas agendadas corretamente, é possível **automatizar rotinas críticas** e garantir maior estabilidade, segurança e escalabilidade para seu ambiente web.

#### Sintaxe básica do comando CRONTAB

Para realizar um agendamento de backup ou varredura para exclusão de log ou coisa do tipo, usa-se o crontab. Segue abaixo sua forma de uso:

```
crontab [-u usuário] arquivo
crontab [-u usuário] [-e | -l | -r | -i]
```

- `-u usuário` → Define o usuário cujo crontab será manipulado (requer permissões de superusuário – `sudo`);
- `-e` → **Edita** o crontab do usuário atual (abre o editor padrão do sistema);
- `-l` → **Lista** todas as tarefas agendadas no crontab do usuário atual;
- `-r` → **Remove** o crontab do usuário atual (apaga todas as tarefas agendadas);
- `-i` → Utilizado com `-r`, **pede confirmação antes de excluir** o crontab.

#### Exemplo de uso: (crontab -e)

Abre o editor para adicionar ou modificar tarefas agendadas do usuário atual:
```
crontab -e
```

Lista as tarefas agendadas do usuário `www-data` (geralmente usado por servidores web como o Apache ou Nginx):
```
sudo crontab -u www-data -l
```

Um exemplo aplicado poderia ser a cópia dos arquivos de backup regularmente. Dessa forma você poderia plugar um pendrive no início da manhã e removê-lo ao final do dia. Conforme passos a seguir.

O HD externo será montado as 8 da manhã na pasta `/media/usbdisk`  
```
00 08 * * * mount /dev/sdb1 /media/usbdisk
```

Será copiado o arquivo de backup da pasta de backup do oracle pra o hd externo as 10 e as 16 horas
```
00 10,16 * * * cp -vRua /u01/app/oracle/backup/. /media/usbdisk/backups
```

As 11 horas será procurado o arquivo no hd externo com mais de 30 dias de salvo e será excluído  
```
00 11 * * * find /media/usbdisk/backups/. -mtime +30 -exec rm -rf {} \;
```

As 18h15 será desmontado o HD e poderá ser retirado da USB  
```
15 18 * * * umount /media/usbdisk
```


[link de compartilhamento](<https://maksoud.github.io/Produtos%20Digitais/Agendamento%20de%20Tarefas%20no%20Linux%20com%20CRONTAB>)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>