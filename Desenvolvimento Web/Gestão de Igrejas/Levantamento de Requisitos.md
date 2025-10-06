Início das atividades: 06/10/2025
#### Gestão de Membros

- **Status do membro:** É ativo, afastado, visitante, transferido para outra igreja
- **Funções e ministérios:** Ex: diaconia, músico, voluntário, líder de grupo
- **Crianças e Adolescentes:**
    - **Vínculo Familiar:** Como você já pensou, ligar ao responsável legal.
    - **Autorizações:** Espaço para upload de termos de consentimento para atividades específicas.
    - **Observações Médicas:** Alergias, condições de saúde relevantes para emergências.
- **Vínculo familiar:** Identificação de parentesco entre membros
- **Comunicação:** Dados de contato e endereço
- **Discipulado/Aconselhamento:**
    - **Discipulador Designado:** Quem é o discipulador de quem.
    - **Registro de Encontros:** Data e breve anotação dos encontros/temas abordados (com privacidade controlada).
    - **Andamento:** Indicadores de progresso ou fases do discipulado.

#### Gestão Financeira

- Acompanhar o fluxo financeiro de entradas e saídas (dízimos e ofertas, doações, projetos, eventos sociais, etc)
- **Relatório de fluxo de caixa:** Acompanhamentos de gastos e projeção futura
- **Categorização Detalhada:** Além de dízimos e ofertas, ter categorias para despesas (manutenção, folha de pagamento, material de limpeza, etc.). 
- **Centros de Custo/Receita:** Possibilidade de vincular transações a projetos ou ministérios específicos.
- **Contas Bancárias:** Gerenciamento de múltiplas contas (corrente, poupança, investimento).

#### Comunicação

- Avisos de eventos, notícias e voluntariados
- **Grupos de avisos:** pastores, ministérios, membros, comunidade
- **Preferência de Contato:** O membro prefere SMS, e-mail, WhatsApp?
- **LGPD/Privacidade:** Campo para consentimento de uso dos dados para comunicação interna da igreja.
- **Envio em Massa:** Possibilidade de enviar e-mails ou mensagens para grupos específicos.
- **Mídia Anexada:** Possibilidade de incluir imagens, PDFs, links.
- **Grupos de comunicação:** Membros recém-cadastrados entram automaticamente em um grupo de "Novos Membros".

#### Gestão de Usuários

- **Tipos de Membros:** Pastores, ministério, secretaria, membros e visitantes.
- **Perfis de Acesso:**
    - **Customização de Permissões:** Definir exatamente o que cada perfil pode ver, criar, editar ou excluir. Por exemplo, a secretaria pode ver todos os dados de membros, mas só pastores podem registrar anotações de aconselhamento.
    - **Hierarquia de Papéis:** Lembre-se que um líder de célula pode ver seu grupo, mas não os outros.
- **Auditoria de Ações:**
    - **Log de Atividades:** Registrar quem fez o quê, quando e onde. Importante para segurança e rastreabilidade, especialmente com dados sensíveis.

---

As tabelas financeiras foram removidas, e as tabelas de acesso (`users`, `rules`, `users_parameters`, `parameters`) serão mantidas como você as tem, mas adicionarei a camada de permissões granulares que você pediu para o futuro. A tabela `users` receberá uma FK para `membros` para vincular usuários a perfis de membros.

Aqui está a modelagem MySQL:

```sql
-- TABELAS DE SUPORTE INICIAIS

-- Tabela para as preferências de contato dos membros
CREATE TABLE preferencias_contato (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_preferencia VARCHAR(50) NOT NULL UNIQUE, -- Ex: Email, SMS, WhatsApp
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- Tabela genérica para armazenamento de arquivos (documentos, imagens, comprovantes)
CREATE TABLE arquivos (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_arquivo VARCHAR(255) NOT NULL,
    tipo_mime VARCHAR(100), -- Ex: application/pdf, image/jpeg
    caminho_armazenamento VARCHAR(500) NOT NULL, -- URL ou path no servidor
    tamanho INT, -- em bytes
    descricao TEXT,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- Tabela para definir as funções e ministérios dentro da igreja
CREATE TABLE funcoes_ministerios (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_funcao VARCHAR(100) NOT NULL UNIQUE, -- Ex: Diaconia, Músico, Líder de Célula
    descricao TEXT,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- Tabela para os tipos de vínculo familiar
CREATE TABLE tipos_vinculo_familiar (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_vinculo VARCHAR(50) NOT NULL UNIQUE, -- Ex: Pai, Mãe, Cônjuge, Filho(a), Irmão(ã)
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- Tabela para grupos de comunicação (Pastores, Ministérios, Membros Ativos, Novatos)
CREATE TABLE grupos_comunicacao (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_grupo VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT,
    tipo_grupo ENUM('Manual', 'Automatico') DEFAULT 'Manual',
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- TABELAS PRINCIPAIS E RELACIONAMENTOS

-- Tabela de Membros (integrando campos de endereço e comunicação)
CREATE TABLE membros (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    parameters_id INT(11), -- Para vincular ao "perfil" da igreja/unidade, se aplicável
    tipo_membro CHAR(1) NOT NULL DEFAULT 'M', -- Ex: M = Membro, V = Visitante, P = Pastor
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo ENUM('M', 'F', 'Outro') NOT NULL,
    estado_civil VARCHAR(50),
    cpf VARCHAR(14) UNIQUE, -- Formato comum: 000.000.000-00
    rg VARCHAR(20),
    profissao_id INT(11),
    -- Campos de endereço diretamente na tabela
    endereco VARCHAR(255),
    link_endereco VARCHAR(255), -- Para links de mapa, como na sua customers
    bairro VARCHAR(100),
    cep VARCHAR(25),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    -- Campos de contato (múltiplos telefones como em customers)
    telefone1 VARCHAR(25),
    telefone2 VARCHAR(25),
    telefone3 VARCHAR(25),
    telefone4 VARCHAR(25),
    email VARCHAR(255),
    data_batismo DATE,
    data_membro DATE, -- Data que se tornou membro da igreja
    carta_recomendacao_arquivo_id INT(11), -- FK para o arquivo de carta, se houver
    status_membro_id INT(11) NOT NULL,
    data_status DATETIME, -- Data da última mudança de status
    igreja_origem VARCHAR(255), -- Nome da igreja, se foi transferido de outra
    consentimento_lgpd TINYINT(1) DEFAULT 0, -- 0 = Não, 1 = Sim, para comunicação interna
    preferencia_contato_id INT(11),
    responsavel_legal_id INT(11), -- Auto-referência para o membro responsável (ex: pais de crianças)
    alergias TEXT,
    condicoes_saude TEXT,
    contato_emergencia_nome VARCHAR(255),
    contato_emergencia_telefone VARCHAR(20),
    referencia TEXT, -- Campo para "como conheceu a igreja" ou observações iniciais
    obs TEXT, -- Observações gerais
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (parameters_id) REFERENCES parameters(id), -- Assumindo 'parameters' como contexto da igreja
    FOREIGN KEY (carta_recomendacao_arquivo_id) REFERENCES arquivos(id),
    FOREIGN KEY (preferencia_contato_id) REFERENCES preferencias_contato(id),
    FOREIGN KEY (responsavel_legal_id) REFERENCES membros(id)
);

-- Tabela para autorizações específicas (ex: viagem de menores, atividades)
CREATE TABLE autorizacoes_membros (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    membro_id INT(11) NOT NULL,
    tipo_autorizacao VARCHAR(255) NOT NULL, -- Ex: "Autorização Viagem Infantil"
    descricao TEXT,
    arquivo_id INT(11) NOT NULL, -- FK para o documento de autorização assinado
    data_validade DATE,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membros(id),
    FOREIGN KEY (arquivo_id) REFERENCES arquivos(id)
);

-- Tabela pivot para relacionar membros a múltiplas funções/ministérios
CREATE TABLE membros_funcoes_ministerios (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    membro_id INT(11) NOT NULL,
    funcao_ministerio_id INT(11) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE, -- Nula se a função ainda estiver ativa
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membros(id),
    FOREIGN KEY (funcao_ministerio_id) REFERENCES funcoes_ministerios(id),
    UNIQUE (membro_id, funcao_ministerio_id, data_inicio) -- Garante unicidade para um membro ter uma função em uma data
);

-- Tabela para vincular membros que são parte da mesma família
CREATE TABLE vinculos_familiares (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    membro_id_1 INT(11) NOT NULL,
    membro_id_2 INT(11) NOT NULL,
    tipo_vinculo_id INT(11) NOT NULL, -- Ex: membro_id_1 é 'Pai' de membro_id_2
    observacoes TEXT,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (membro_id_1) REFERENCES membros(id),
    FOREIGN KEY (membro_id_2) REFERENCES membros(id),
    FOREIGN KEY (tipo_vinculo_id) REFERENCES tipos_vinculo_familiar(id),
    UNIQUE (membro_id_1, membro_id_2, tipo_vinculo_id) -- Evita vínculos duplicados
);

-- Tabela para registrar relações de discipulado
CREATE TABLE discipulados (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    discipulador_id INT(11) NOT NULL, -- FK para o membro que discipula
    discipulado_id INT(11) NOT NULL, -- FK para o membro que é discipulado
    data_inicio DATE NOT NULL,
    data_fim DATE,
    status ENUM('Ativo', 'Concluido', 'Pausado', 'Cancelado') DEFAULT 'Ativo',
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (discipulador_id) REFERENCES membros(id),
    FOREIGN KEY (discipulado_id) REFERENCES membros(id),
    UNIQUE (discipulador_id, discipulado_id, data_inicio)
);

-- Tabela para registrar encontros de discipulado ou aconselhamento
CREATE TABLE encontros_discipulado_aconselhamento (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    discipulado_id INT(11), -- FK para a relação de discipulado (se for formal)
    membro_id INT(11), -- FK para o membro (se for aconselhamento avulso)
    data_encontro DATETIME NOT NULL,
    resumo_anotacoes TEXT NOT NULL,
    privacidade_nivel ENUM('Privado', 'Discipulador', 'Lideranca', 'Publico') DEFAULT 'Privado',
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (discipulado_id) REFERENCES discipulados(id),
    FOREIGN KEY (membro_id) REFERENCES membros(id)
);

-- Tabela pivot para relacionar membros a grupos de comunicação
CREATE TABLE membros_grupos_comunicacao (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    membro_id INT(11) NOT NULL,
    grupo_comunicacao_id INT(11) NOT NULL,
    data_adesao DATETIME NOT NULL,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membros(id),
    FOREIGN KEY (grupo_comunicacao_id) REFERENCES grupos_comunicacao(id),
    UNIQUE (membro_id, grupo_comunicacao_id)
);

-- Tabela para permissões granulares (SUGESTÃO PARA FUTURO CRESCIMENTO)
CREATE TABLE permissoes (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_permissao VARCHAR(100) NOT NULL UNIQUE, -- Ex: 'membros_view', 'financeiro_edit'
    descricao TEXT,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL
);

-- Tabela pivot para relacionar suas 'rules' a permissões granulares (SUGESTÃO PARA FUTURO CRESCIMENTO)
CREATE TABLE rules_permissoes (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    rule_id INT(11) NOT NULL,
    permissao_id INT(11) NOT NULL,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (rule_id) REFERENCES rules(id),
    FOREIGN KEY (permissao_id) REFERENCES permissoes(id),
    UNIQUE (rule_id, permissao_id)
);

-- Tabela para comunicações (avisos, notícias, etc.)
CREATE TABLE comunicacoes (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    conteudo TEXT NOT NULL,
    data_envio DATETIME, -- Data real de envio (pode ser nula se agendado)
    agendamento_data DATETIME, -- Data para envio futuro
    remetente_usuario_id INT(11), -- FK para o usuário que criou/agendou a comunicação
    tipo_comunicacao ENUM('Aviso', 'Noticia', 'Voluntariado', 'Evento') NOT NULL,
    status_envio ENUM('Pendente', 'Agendado', 'Enviado', 'Erro') DEFAULT 'Pendente',
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (remetente_usuario_id) REFERENCES users(id)
);

-- Tabela para registrar destinatários de comunicações (membros ou grupos)
CREATE TABLE comunicacoes_destinatarios (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    comunicacao_id INT(11) NOT NULL,
    membro_id INT(11), -- Destinatário individual
    grupo_comunicacao_id INT(11), -- Destinatário de grupo
    status_leitura ENUM('NaoLido', 'Lido') DEFAULT 'NaoLido',
    data_leitura DATETIME,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (comunicacao_id) REFERENCES comunicacoes(id),
    FOREIGN KEY (membro_id) REFERENCES membros(id),
    FOREIGN KEY (grupo_comunicacao_id) REFERENCES grupos_comunicacao(id)
);

-- Tabela pivot para anexos de comunicações
CREATE TABLE comunicacoes_anexos (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    comunicacao_id INT(11) NOT NULL,
    arquivo_id INT(11) NOT NULL,
    created DATETIME NOT NULL,
    modified DATETIME NOT NULL,
    FOREIGN KEY (comunicacao_id) REFERENCES comunicacoes(id),
    FOREIGN KEY (arquivo_id) REFERENCES arquivos(id)
);
```

---

