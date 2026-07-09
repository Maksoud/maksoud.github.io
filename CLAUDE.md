# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project**. It is a personal [Obsidian](https://obsidian.md) vault of study notes (in **Brazilian Portuguese**) that is published as a static site to GitHub Pages at https://maksoud.github.io. There is no build step, no test suite, and no application code — the content is Markdown, rendered directly by GitHub Pages.

Content is organized into top-level folders by subject area (e.g. `ITIL 4`, `Data Analyst`, `Estatística`, `Gestão de Projetos`, `Inteligência Artificial (IA)`, `Desenvolvimento Web`, `Produtos Digitais`, `Finanças`, `Criptomoedas`). `Sumário.md` is the hand-maintained table of contents / index linking to notes across all folders.

## Working with the content

- **Language**: Write and edit notes in Brazilian Portuguese to match existing content. Folder and file names are also in Portuguese.
- **Format**: Notes use Obsidian-flavored Markdown. `Markdown Instructions.md` documents the conventions used here, including Obsidian extras like `==highlight==` (marcado), `~~~lang` fenced code blocks, and image sizing syntax `![alt|250x65](url)`.
- **Images**: Store per-topic images in an `imgs/` subfolder within each subject folder (e.g. `Data Analyst/imgs/1.png`) and reference them with relative paths.
- **Links & internal references**: Notes cross-link with Obsidian wikilinks and standard Markdown links. When adding a new note, also add a link to it from `Sumário.md` so it is discoverable from the published index.
- `.obsidian/` holds Obsidian editor config (plugins, appearance, workspace). Do not treat it as site content; changes there affect the local editor, not the published site.

## Publishing workflow

Publishing is just git — pushing to `main` updates the live GitHub Pages site. Two helper batch scripts wrap this (run from the repo root on Windows):

- `save.bat` — stages everything, commits with the message `"Atualizacao automatica de notas"`, and pushes to `origin main`.
- `get.bat` — pulls the latest from `origin main`.

Commit history is dominated by these automated `"Atualizacao automatica de notas"` commits. When committing on the user's behalf, prefer a descriptive message unless matching that convention is intended.

## Important notes

- The repo is intentionally **public** and may contain third-party study material gathered from the web/AI (see `README.md` disclaimer). It is for personal study use.
- The vault lives inside a OneDrive-synced path, so files may be touched by OneDrive sync in addition to git.
