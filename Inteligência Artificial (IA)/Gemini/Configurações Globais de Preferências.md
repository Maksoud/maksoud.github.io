O arquivo `settings.json` precisa de algumas tags para ajudar nas permissões automáticas, assim como o método `ctrl+tab` no Claude Code faz.

Segue exemplo de arquivo:

```json
{
    "workbench.colorTheme": "Dark+",
    "git.confirmSync": false,
    "workbench.editor.enablePreview": false,
    "git.autofetch": true,
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "github.copilot.enable": {
        "*": false,
        "plaintext": false,
        "markdown": false,
        "scminput": false,
        "php": true
    },
    "diffEditor.ignoreTrimWhitespace": false,
    "diffEditor.maxComputationTime": 0,
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "chat.disableAIFeatures": true,
    "claudeCode.preferredLocation": "panel",
    "diffEditor.codeLens": true,
    "chat.tools.terminal.enableAutoApprove": true,
    "chat.tools.terminal.autoApprove": {
        "php": true,
        "/^php\\b/": true,
        "/^.*php\\.exe\\b/": true,
        "/^vendor\\\\bin\\\\phpunit/": true
    }
}
```

Os comandos `chat.tools.terminal.enableAutoApprove` e `chat.tools.terminal.autoApprove` são os comandos necessários para aprovar as execuções automáticas, note que há uma lista predefinida para isso. Para mim, que estou usando o PHP instalado pelo Laragon, adicionei o comando: 
`"/^.*\\\\laragon\\\\bin\\\\php\\\\php-.*\\\\php\\.exe\\b/": true,` nessa lista.

Outros arquivos que também podem ser alterados são: 

- C:\Users\[seu-usuário-windows]\AppData\Roaming\Code\User\settings.json
- C:\Users\[seu-usuário-windows]\AppData\Roaming\Antigravity IDE\User\settings.json
- .vscode\settings.json (dentro do seu projeto)

O conteúdo do arquivo `.vscode\settings.json` do meu projeto está assim:
```json
{
    "workbench.colorTheme": "Dark+",
    "git.confirmSync": false,
    "workbench.editor.enablePreview": false,
    "git.autofetch": true,
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "github.copilot.enable": {
        "*": false,
        "plaintext": false,
        "markdown": false,
        "scminput": false,
        "php": true
    },
    "diffEditor.ignoreTrimWhitespace": false,
    "diffEditor.maxComputationTime": 0,
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "chat.disableAIFeatures": true,
    "claudeCode.preferredLocation": "panel",
    "chat.tools.terminal.enableAutoApprove": true,
    "chat.tools.terminal.autoApprove": {
        "git diff": true,
        "git status": true,
        "git log": true,
        "git branch": true,
        "/^git\\s+.*$/": true,
		"/^php\\s+.*$/": true,
        "/^.*\\\\php\\.exe\\s+.*$/": true,
        "/^powershell\\s+.*$/": true,
        "/^.*[Pp]ower[Sh]ell(\\s+.*)?$/": true
    },
    "php.validate.executablePath": "php"
}
```

Mesmo com todas as configurações, a melhor forma de resolver isso foi utilizando a IDE Antigravity do Google.