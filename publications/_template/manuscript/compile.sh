#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v pdflatex >/dev/null || { echo "pdflatex tidak ditemukan" >&2; exit 1; }
command -v bibtex >/dev/null || { echo "bibtex tidak ditemukan" >&2; exit 1; }
pdflatex -interaction=nonstopmode -halt-on-error article.tex
bibtex article
pdflatex -interaction=nonstopmode -halt-on-error article.tex
pdflatex -interaction=nonstopmode -halt-on-error article.tex
echo "Selesai: article.pdf"
