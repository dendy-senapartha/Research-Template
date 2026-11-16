#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "Error: pdflatex tidak ditemukan. Instal TeX Live/MiKTeX." >&2
  exit 1
fi
if ! command -v bibtex >/dev/null 2>&1; then
  echo "Error: bibtex tidak ditemukan. Instal BibTeX bersama distribusi TeX." >&2
  exit 1
fi

pdflatex -interaction=nonstopmode -halt-on-error -file-line-error laporan.tex
bibtex laporan
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error laporan.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error laporan.tex
echo "Selesai: manuscript/latex/laporan.pdf"
