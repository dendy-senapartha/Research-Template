# Repository Structure

```text
/
├── agents/
│   ├── research/Agent.md
│   └── writing/
│       ├── Agent.md
│       ├── core/
│       ├── sections/
│       ├── few-shot/
│       └── quality/
├── research/
│   ├── governance/
│   ├── protocols/
│   │   ├── slr/
│   │   ├── study-design/
│   │   ├── experimental-manipulation/
│   │   ├── artifact-development/
│   │   └── evaluation/
│   ├── evidence/
│   └── artifacts/
│       ├── working/
│       ├── validated/
│       └── frozen/
├── manuscript/
│   └── latex/
│       ├── laporan.tex
│       ├── config.tex
│       ├── preamble.tex
│       ├── compile.sh
│       ├── flows/
│       ├── frontmatter/
│       ├── chapters/
│       ├── backmatter/
│       ├── appendices/
│       └── figures/
├── publications/
│   ├── publication-register.csv
│   ├── _template/
│   └── PUB-001/
├── references/references.bib
├── scripts/
├── docs/
└── archive/
```

## Otoritas dan alur

`governance` menetapkan arah, `protocols` menentukan tindakan, `evidence` menyimpan sumber, `artifacts` mengelola luaran, sedangkan `manuscript` dan `publications` menyajikan hasil penelitian.

Artikel ilmiah dan naskah penelitian tidak menjadi tempat penyimpanan data mentah utama. Perubahan substansi harus dicatat dalam governance dan tidak boleh timbul dari penyuntingan kalimat semata.

## Konvensi ID yang disarankan

- `RQ-001`: research question.
- `DEC-001`: keputusan penelitian.
- `OQ-001`: pertanyaan terbuka.
- `PROT-001`: protokol.
- `EVD-001`: evidence record.
- `ART-001`: artefak.
- `PUB-001`: luaran publikasi.

Pola ID hanya contoh. Pilih skema sesuai kebutuhan studi, lalu jaga konsistensinya.
