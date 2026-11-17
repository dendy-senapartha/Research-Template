# Struktur Repository Penelitian

\`\`\`text
/
├── agents/{research/,writing/}
├── research/
│   ├── governance/
│   ├── protocols/
│   ├── evidence/
│   └── artifacts/{working/,validated/,frozen/}
├── manuscript/
│   └── latex/
│       ├── laporan.tex
│       ├── compile.sh
│       ├── a0-identitas.tex
│       ├── a1-database.hyphenate.tex
│       ├── a2-abstrak.tex ... a8-lampiran.tex
│       ├── b1-bab1.tex ... b6-bab6.tex
│       ├── flows/{praproposal,proposal,disertasi}.tex
│       ├── untouch/
│       ├── gambar/
│       ├── lampiran/
│       └── kode/
├── publications/{_template/,PUB-001/,publication-register.csv}
├── references/a7-pustaka.bib
├── scripts/
├── docs/
└── archive/
\`\`\`

Tata kelola menetapkan keputusan, protokol menetapkan tindakan, evidence menyimpan sumber, dan artifacts menyimpan luaran. Manuskrip serta publikasi **bukan** tempat utama data mentah. Berkas LaTeX menggunakan struktur sumber dari repository disertasi, tetapi konten diisi placeholder.
