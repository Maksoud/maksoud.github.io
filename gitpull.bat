@echo off
:: Define the path to your repository
set REPO_PATH="C:\Users\renee\OneDrive\Documentos\Obsidian Vault\maksoud.github.io"

:: Navigate to the repository directory
cd /d %REPO_PATH%

:: Fix the Git configuration error
git config --global gc.auto 0

:: Add all changes to git
git add .

:: Commit changes with a message
git commit -m "Atualização automática de notas"

:: Push changes to the remote repository
git push origin main

:: Pause to view the output
pause
