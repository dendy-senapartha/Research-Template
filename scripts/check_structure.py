#!/usr/bin/env python3
"""Lightweight, dependency-free validation for the generic repository template."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "agents/research/Agent.md",
    "agents/writing/Agent.md",
    "research/governance/research-canon.md",
    "research/governance/decision-log.csv",
    "research/governance/open-questions.csv",
    "research/governance/research-log.md",
    "research/protocols/protocol-template.md",
    "research/evidence/README.md",
    "research/artifacts/README.md",
    "research/artifacts/working/.gitkeep",
    "research/artifacts/validated/.gitkeep",
    "research/artifacts/frozen/.gitkeep",
    "manuscript/latex/laporan.tex",
    "manuscript/latex/config.tex",
    "manuscript/latex/preamble.tex",
    "manuscript/latex/compile.sh",
    "manuscript/latex/flows/proposal.tex",
    "manuscript/latex/flows/dissertation.tex",
    "manuscript/latex/flows/frontmatter.tex",
    "manuscript/latex/backmatter/references.tex",
    "publications/publication-register.csv",
    "publications/_template/publication.yml",
    "publications/_template/manuscript/article.tex",
    "references/references.bib",
    "docs/getting-started.md",
    "docs/project-instructions-template.md",
]

errors = []
for path in REQUIRED:
    if not (ROOT / path).is_file():
        errors.append(f"File tidak ditemukan: {path}")

if not errors:
    main = (ROOT / "manuscript/latex/laporan.tex").read_text(encoding="utf-8")
    config = (ROOT / "manuscript/latex/config.tex").read_text(encoding="utf-8")
    bib = (ROOT / "manuscript/latex/backmatter/references.tex").read_text(encoding="utf-8")
    article = (ROOT / "publications/_template/manuscript/article.tex").read_text(encoding="utf-8")
    if r"\input{flows/proposal}" not in main:
        errors.append("Main LaTeX tidak terhubung ke proposal.")
    if r"\input{flows/dissertation}" not in main:
        errors.append("Main LaTeX tidak terhubung ke dissertation.")
    if r"\newcommand{\DocumentMode}{proposal}" not in config:
        errors.append("Mode awal config.tex bukan proposal.")
    if r"\bibliography{../../references/references}" not in bib:
        errors.append("Path bibliography naskah tidak sesuai.")
    if r"\bibliography{../../../references/references}" not in article:
        errors.append("Path bibliography artikel tidak sesuai.")

print(f"Checked {len(REQUIRED)} required paths.")
if errors:
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    sys.exit(1)
print("PASS: repository structure and key LaTeX references.")

