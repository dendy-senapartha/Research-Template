#!/usr/bin/env python3
"""Validate reusable research repository and Udayana LaTeX skeleton."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "agents/research/Agent.md",
    "agents/writing/Agent.md",
    "research/governance/research-canon.md",
    "research/governance/decision-log.csv",
    "research/governance/open-questions.csv",
    "research/governance/research-log.md",
    "research/protocols/protocol-template.md",
    "research/artifacts/README.md",
    "manuscript/latex/laporan.tex",
    "manuscript/latex/a0-identitas.tex",
    "manuscript/latex/compile.sh",
    "manuscript/latex/untouch/xx-preambles.tex",
    "manuscript/latex/untouch/xx-daftar.tex",
    "manuscript/latex/untouch/xx-daftarpustaka.tex",
    "manuscript/latex/flows/praproposal.tex",
    "manuscript/latex/flows/proposal.tex",
    "manuscript/latex/flows/disertasi.tex",
    "manuscript/latex/b1-bab1.tex",
    "manuscript/latex/b2-bab2.tex",
    "manuscript/latex/b3-bab3.tex",
    "manuscript/latex/b4-bab4.tex",
    "manuscript/latex/b5-bab5.tex",
    "manuscript/latex/a8-lampiran.tex",
    "manuscript/latex/gambar/UdayanaLogo720p.png",
    "references/a7-pustaka.bib",
    "publications/publication-register.csv",
    "publications/_template/publication.yml",
    "publications/_template/manuscript/article.tex",
]
errors = [f"Missing: {p}" for p in REQUIRED if not (ROOT / p).is_file()]
if not errors:
    main = (ROOT / "manuscript/latex/laporan.tex").read_text(encoding="utf-8")
    bib = (ROOT / "manuscript/latex/untouch/xx-daftarpustaka.tex").read_text(encoding="utf-8")
    article = (ROOT / "publications/_template/manuscript/article.tex").read_text(encoding="utf-8")
    compiler = (ROOT / "manuscript/latex/compile.sh").read_text(encoding="utf-8")
    checks = {
        "Practical mode selection": r"\newcommand{\DocFlow}{proposal}" in main,
        "Proposal flow": r"\input{flows/proposal}" in main,
        "Praproposal flow": r"\input{flows/praproposal}" in main,
        "Dissertation flow": r"\input{flows/disertasi}" in main,
        "Manuscript BibTeX": r"\bibliography{../../references/a7-pustaka}" in bib,
        "Publication BibTeX": r"\bibliography{../../../references/a7-pustaka}" in article,
        "Original compiler features": "--skip-deps" in compiler and "check_dependencies" in compiler and "bibtex" in compiler,
    }
    errors.extend(f"Invalid link: {key}" for key, ok in checks.items() if not ok)
    for p in (ROOT / "manuscript/latex").rglob("*.tex"):
        content = p.read_text(encoding="utf-8")
        for forbidden in ["I Kadek Dendy Senapartha", "2591011009", "Tri Sandhya", "Kramaning Sembah", "Artifact Praxis Model"]:
            if forbidden.lower() in content.lower():
                errors.append(f"Research-specific text remains: {p.relative_to(ROOT)}")
print(f"Checked {len(REQUIRED)} required files.")
if errors:
    for issue in errors:
        print("FAIL:", issue, file=sys.stderr)
    sys.exit(1)
print("PASS: repository and manuscript structure.")
