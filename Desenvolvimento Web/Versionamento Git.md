### [Sumário](<https://maksoud.github.io/Sumário>)

# Versionamento Git

#### Criando uma nova chave SSH

Para gerar uma nova chave de acesso SSH, digite isso em seu prompt de comandos, substituindo o [usuário] pelo seu e-mail do GitHub:

```shell
ssh-keygen -t rsa -C "[usuário]" -b 4096
```

Caso a chave já exista, basta copiar a chave existente e gravar no Git.
Criando a chave pública e adicionando na pasta de chaves do autorizadas (Linux):

```shell
ssh-keygen -f ~/.ssh/id_rsa -y > ~/.ssh/id_rsa.pub
ssh-keygen -f ~/.ssh/id_rsa -y -e -m pem > ~/.ssh/id_rsa.pem
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

Agora você já pode copiar a chave para criar o seu arquivo `id_rsa` localmente:

```shell
cat ~/.ssh/id_rsa.pub      # (linux)
type ~\.ssh\id_rsa.pub     # (windows)
```

Copie o texto da chave dentro de um novo arquivo na pasta “.ssh”, que encontra-se na pasta raiz do seu usuário na sua máquina local. _Não esqueça de excluir as quebras de linhas do código._

> Também será necessário informar essa chave na lista de chaves autorizadas na ferramenta que você utiliza para hospedar o servidor, exemplo: Google Cloud, Bitbucket, etc.

#### Adicionando uma chave SSH no GitHub

Acesse o GitHub na página de [Configuração de chaves SSH](<https://github.com/settings/ssh/new>) para vincular o seu computador/servidor ao repositório Git.

Adicione a chave criada seguindo o exemplo da imagem abaixo:

![[2025-07-06_18h29_45.png]]

Uma chave corretamente configurada e validada, deverá exibir dessa forma na lista:

![[2025-07-06_18h32_43.png]]

#### Clonando um Repositório

![[2025-07-06_18h37_57.png]]

Para clonar o seu repositório do GitHub, basta seguir o exemplo da imagem acima, e digitar o seguinte comando na raiz do seu servidor local:

![[2025-07-06_18h41_01.png]]

A raiz dos meus projetos locais ficam em `C:\Projetos`, assim como configurei em meu XAMPP. Isso poderá mudar em seu computador.

#### Falha de Formato Inválido

Caso você esteja acessando o serviço SSH e esteja recebendo uma mensagem de formato inválido (invalid format), execute os seguintes passos.

Execute o seguinte comando no terminal do servidor para criar uma chave no formato privado OpenSSH:  

`puttygen <arquivo-de-origem> -O <formato> -o <arquivo-de-destino>`

```shell
puttygen id_rsa -O private-openssh -o id_rsa_private
```

> Talvez seja necessário executar o comando de instalação do puttygen: _sudo apt-get install putty-tools_

> Adicionar o texto —–BEGIN OPENSSH PRIVATE KEY—– no início e —–END OPENSSH PRIVATE KEY—– no final do arquivo não funcionou para mim.

Execute o comando abaixo no servidor para exibir a chave privada. Agora copie o texto e crie o arquivo “id_rsa_private” dentro da pasta “.ssh”, localizado na pasta raiz do seu usuário na sua máquina local.

```shell
cat ~/.ssh/id_rsa_private
```

> Esse formato de chave possui quebra de linhas, diferente do formato da primeira chave que geramos e removemos as quebras de linha criar o nosso arquivo local ‘id_rsa’.

Agora você pode acessar o servidor com o arquivo de senha no formato correto, usando o comando abaixo na sua máquina local:

```shell
ssh -i ~/.ssh/id_rsa_private [usuário]@[ip-do-servidor]
```

> O usuário do comando acima deverá ser o mesmo que foi utilizado na criação da chave, conforme explicação nos primeiros passos.

> Caso seja exibido a mensagem “too open”, então execute a mudança de permissão de acesso do arquivo de chave: “_chmod 600 ~/.ssh/id_rsa_private_“.


[link de compartilhamento](<https://maksoud.github.io/Desenvolvimento%20Web/Versionamento%20Git>)

<sup><sub>
Renée Maksoud - julho de 2025
</sub></sup>