### [Sumário](<https://maksoud.github.io/Sumário>)

# Registrando um Domínio (.com.br)

O [Registro BR](<https://registro.br/>) é o **órgão oficial responsável pelo registro de domínios com final `.br` no Brasil**. Ele é operado pelo **NIC.br** (Núcleo de Informação e Coordenação do Ponto BR), que é vinculado ao Comitê Gestor da Internet no Brasil (CGI.br).

### 🔧 **Como funciona o registro de um domínio no Registro.br**

1. **Acesse o site:**  
    [https://registro.br](https://registro.br)
2. **Pesquise o domínio desejado:**  
    Você digita o nome que deseja registrar (ex: `meusite.com.br`) e o sistema verifica se está disponível.
3. **Crie uma conta ou acesse com seu CPF/CNPJ:**  
    Para registrar um domínio, você precisa ter um **ID no Registro.br**, vinculado a um CPF ou CNPJ válido.
4. **Escolha o tempo de registro:**  
    Você pode registrar o domínio por 1 até 10 anos.
5. **Realize o pagamento:**  
    Após o pagamento (boleto ou cartão), o domínio passa a ser seu e você pode configurá-lo com os servidores DNS da sua preferência.
6. **Gerenciamento:**  
    Você pode configurar **DNS**, **contatos administrativos**, **servidores de e-mail**, entre outras opções diretamente no painel do Registro.br.

---
## **O que é a tabela CNAME no DNS**

#### **CNAME (Canonical Name)**

O **CNAME** é um tipo de **registro DNS** que funciona como um **apelido para outro domínio**. Em vez de apontar diretamente para um endereço IP (como um A Record), ele aponta para **outro nome de domínio**, que por sua vez resolve para um IP.

#### **Como funciona:**

Imagine que você tem um domínio principal:

```
www.seusite.com.br → CNAME → seusite.com.br
```

Isso significa que **`www.seusite.com.br` herda todas as configurações de DNS de `seusite.com.br`**. Se `seusite.com.br` for alterado para apontar para outro IP, `www.seusite.com.br` seguirá automaticamente.

#### **Quando usar um CNAME?**

- Para **criar subdomínios que apontem para um serviço externo**, como:
```   
blog.seusite.com.br → CNAME → hosting.plataforma.com
```
- Para facilitar a manutenção: qualquer alteração feita no destino do CNAME será refletida automaticamente nos aliases.

#### **Boas práticas e limitações do CNAME**

- **Nunca use CNAME no domínio raiz (ex: seusite.com.br)** — apenas para subdomínios. No domínio raiz, você deve usar registros **A** (para IPv4) ou **AAAA** (para IPv6).
- CNAMEs **não podem coexistir com outros registros no mesmo nome**, como MX (e-mail).

---
## **Registro de domínios `.com` com o Google Domains via cloud.google.com**

O **Google Domains**, acessível via cloud.google.com, é uma **solução confiável e moderna** para o registro e gerenciamento de domínios, especialmente voltada para quem já utiliza os serviços da **Google Cloud Platform (GCP)**.

#### **Vantagens de registrar um domínio `.com` com o Google**

1. **Interface simples e integrada com o Google Cloud**
    - Você pode registrar e gerenciar domínios diretamente pelo console da GCP, ideal para desenvolvedores e empresas que já usam os serviços da nuvem do Google.
2. **Domínios internacionais**
    - O Google Domains permite registrar **domínios genéricos** como `.com`, `.net`, `.org`, entre outros TLDs.
3. **Privacidade WHOIS incluída**
    - A proteção de privacidade do domínio (para ocultar seus dados pessoais no WHOIS) está **inclusa sem custo extra**, ao contrário de muitos outros registradores.
4. **Integração com serviços do Google**
    - Fácil integração com **Google Workspace (e-mail profissional)**, **App Engine**, **Firebase**, **Cloud Run** e outros serviços da Google Cloud.
5. **Gerenciamento de DNS avançado**
    - Suporte a registros A, AAAA, CNAME, MX, TXT, NS, entre outros.
    - Propagação rápida com servidores DNS do Google, reconhecidos por sua velocidade e estabilidade.

#### **Como registrar um domínio `.com` pelo Google Cloud**

1. Acesse: https://cloud.google.com/domains
2. Clique em **"Buy a domain"**;
3. Pesquise o nome desejado e veja se o domínio está disponível;
4. Escolha o domínio `.com` e prossiga com o registro;
5. Vincule ao seu projeto do Google Cloud, se desejar;
6. Complete o pagamento com uma conta Google;
7. Configure DNS, zona gerenciada, ou vincule diretamente a algum serviço do Google.

> Mesmo que você **não utilize GCP** como hospedagem, ainda assim pode registrar seu domínio `.com` com o Google e apontar o DNS para outro provedor (como Hostinger, Cloudflare, DigitalOcean, etc).

---

## Outras Soluções

Você também pode registrar um domínio por meio de parceiros como **Hostinger**, **KingHost** ou **HostGator**. Essas plataformas costumam oferecer **cupons de desconto**, frequentemente divulgados em **vídeos tutoriais no YouTube**. Além disso, a configuração é bastante intuitiva, com **instalação facilitada de serviços como o WordPress**, o que torna todo o processo de publicação e gerenciamento do seu site ainda mais simples e acessível.


[link de compartilhamento](<https://maksoud.github.io/Produtos%20Digitais/Registrando%20um%20Dom%C3%ADnio%20BR>)

<sup><sub>
Renée Maksoud - abril de 2025
</sub></sup>