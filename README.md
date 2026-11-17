# Research Template

Template repository penelitian dengan pemisahan governance, protokol, evidence, artefak, manuskrip LaTeX, dan publikasi jurnal/prosiding.

## Struktur

- \`agents/research/\` dan \`agents/writing/\`: arahan asisten penelitian dan penulisan.
- \`research/governance/\`: research canon, decision log, open questions, research log.
- \`research/protocols/\`, \`research/evidence/\`, \`research/artifacts/\`: prosedur, data, serta luaran penelitian.
- \`manuscript/latex/\`: template Universitas Udayana berbasis repository \`dendy-senapartha/disertation\`, branch \`proposal\`.
- \`publications/\`: Publication ID, metadata, dan workspace artikel.
- \`references/a7-pustaka.bib\`: bibliografi bersama.
- \`scripts/\`, \`docs/\`, \`archive/\`: utilitas, panduan, dan arsip.

## Cara memulai

1. Isi \`research/governance/research-canon.md\` setelah keputusan penelitian ditetapkan.
2. Gunakan \`docs/getting-started.md\` untuk menyesuaikan proyek baru.
3. Ganti placeholder penulis, judul, promotor, tanggal pada \`manuscript/latex/a0-identitas.tex\`. Nama Universitas Udayana sengaja dipertahankan dan dapat diubah jika proyek digunakan di institusi lain.
4. Pilih mode \`praproposal\`, \`proposal\`, atau \`disertasi\` pada \`manuscript/latex/laporan.tex\`.
5. Tambahkan rujukan terverifikasi di \`references/a7-pustaka.bib\`.
6. Untuk kompilasi, jalankan:

\`\`\`bash
cd manuscript/latex
bash compile.sh --skip-deps
\`\`\`

7. Untuk publikasi, gunakan \`publications/_template/\`, \`publication-register.csv\`, dan \`python3 scripts/new_publication.py PUB-001\`.
8. Validasi struktur melalui \`python3 scripts/check_structure.py\`.

## Ruang lingkup template

Komponen LaTeX mempertahankan tata letak dan script kompilasi sumber, tetapi seluruh isi riset, nama individu, data, dan lampiran spesifik dihapus. Berkas gambar dari penelitian sumber tidak ikut disalin selain logo Universitas Udayana.

Ini bukan template resmi universitas, dan tidak memuat keputusan ilmiah maupun data penelitian yang telah divalidasi.
