# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project**. It is a personal [Obsidian](https://obsidian.md) vault of study notes (in **Brazilian Portuguese**). There is no build step, no test suite, and no application code: the content is plain Markdown.

The notes are published at **https://correiarodrigues.com.br/notas/** (a WordPress site that reads the notes and images from this GitHub repo). The old GitHub Pages address (https://maksoud.github.io) is no longer the destination for links.

Content is organized into top-level folders by subject area: `Carreiras`, `Concursos`, `Criptomoedas`, `Data Analyst`, `Desenvolvimento Web`, `Estatística`, `Finanças`, `Gestão de Projetos`, `Inteligência Artificial (IA)`, `ITIL 4`, `Job Prep`, `Mente e Estudos`, `Pensamentos e Frases`, `Produtos Digitais`, `ServiceNow`, and `Vendas e Negócios`. `Sumário.md` is the hand-maintained table of contents / index linking to notes across all folders.

## Working with the content

- **Language**: Write and edit notes in Brazilian Portuguese to match existing content. Folder and file names are also in Portuguese.
- **No em dashes**: Never use "—" (or "–") as punctuation in note text, titles or the Sumário. Use a comma, colon, parentheses or a separate sentence instead. The author considers dashes a sign of AI-written text.
- **Format**: Notes use Obsidian-flavored Markdown. `Markdown Instructions.md` documents the conventions used here, including Obsidian extras like `==highlight==` (marcado), `~~~lang` fenced code blocks, and image sizing syntax `![alt|250x65](url)`.
- **Images**: Store per-topic images in an `imgs/` subfolder within each subject folder (e.g. `Data Analyst/imgs/1.png`) and reference them with relative paths.

## Standard header and footer (required in every note)

Every note starts with a breadcrumb header in **plain text, without links**:

~~~markdown
### Sumário > Conceitos Japoneses de Vida
~~~

Use `### Sumário` alone when there is no parent note. Use `### Sumário > <parent note>` when the note belongs to a hub note (e.g. `Conceitos Japoneses de Vida`, `Modelos de Inteligência Artificial`, `ITIL 4`, `Projeto de Gestão de Criptomoedas`).

Every note ends with the share link (pointing to the new site), followed by author and publication month:

~~~markdown
[link de compartilhamento](https://correiarodrigues.com.br/notas/mente-e-estudos/ganbaru/)

<sup><sub>
Renée Maksoud - maio de 2025
</sub></sup>
~~~

- The date is the month and year of publication, written out in lowercase Portuguese. If unknown, use the month of the file's first commit (`git log --diff-filter=A --follow --format=%ad --date=short -- <file>`).
- Notes under `Criptomoedas/` sign as `Criptoren - Renée Maksoud - <mês> de <ano>`.
- Do not add a link to the Sumário anywhere in the note; the only link in the header/footer area is the share link.

## Note URLs on the new site

URL = `https://correiarodrigues.com.br/notas/` + the note's path (folders + file name without `.md`), each segment lowercased, accents removed, `&` and apostrophes dropped, any other run of non-alphanumeric characters turned into `-`, ending with `/`.

Example: `Inteligência Artificial (IA)/Engenharia de Prompt/1. Fundamentos da Engenharia de Prompt/Como Funciona o ChatGPT – OpenAI.md` → `https://correiarodrigues.com.br/notas/inteligencia-artificial-ia/engenharia-de-prompt/1-fundamentos-da-engenharia-de-prompt/como-funciona-o-chatgpt-openai/`

Known exception: `Inteligência Artificial (IA)/Modelos de Inteligência Artificial.md` → `.../inteligencia-artificial-ia/modelos-de-inteligencia-artificial-2/` (the URL without `-2` is the folder index). For a new note, check with `curl` that the URL returns 200 once the site has picked it up.

## Links & internal references

- Notes cross-link with Obsidian wikilinks and standard Markdown links. Links between notes use the new-site URLs above.
- When adding a new note, also add a link to it from `Sumário.md`. Entries are grouped under a section heading per subject; each links to the note's `https://correiarodrigues.com.br/notas/...` URL followed by a hyphen and a date in italics (`- *YYYY-MM-DD*`) marking when the note was first committed. Match that format when adding an entry.
- Image links (`imgs/...`, including `![[maksoud.github.io/...]]` Obsidian embeds) stay as they are: the site reads images straight from the GitHub repo.
- `.obsidian/` holds Obsidian editor config (plugins, appearance, workspace). Do not treat it as site content; changes there affect the local editor, not the published site.

## Publishing workflow

Publishing is just git: pushing to `main` updates the repo the site reads from. Two helper batch scripts wrap this (run from the repo root on Windows):

- `save.bat`: stages everything, commits with the message `"Atualizacao automatica de notas"`, and pushes to `origin main`.
- `get.bat`: pulls the latest from `origin main`.

Commit history is dominated by these automated `"Atualizacao automatica de notas"` commits. When committing on the user's behalf, prefer a descriptive message unless matching that convention is intended.

## Important notes

- The repo is intentionally **public** and may contain third-party study material gathered from the web/AI (see `README.md` disclaimer). It is for personal study use.
- The vault lives inside a OneDrive-synced path, so files may be touched by OneDrive sync in addition to git.
