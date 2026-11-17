# Template Manuskrip LaTeX Universitas Udayana

Struktur, format, dan script kompilasi diadaptasi dari \`dendy-senapartha/disertation\` branch \`proposal\`, direktori \`manuscript/latex/\`. Template ini mempertahankan identitas institusi dan logo Universitas Udayana, tetapi seluruh isi penelitian, identitas individu, tanggal, serta lampiran khusus riset diganti dengan placeholder.

**Catatan:** ini adalah template turunan untuk memudahkan penulisan, bukan klaim bahwa format sudah disahkan Universitas Udayana.

## File utama

- \`laporan.tex\`: entry point utama, memilih alur \`praproposal\`, \`proposal\`, atau \`disertasi\`.
- \`a0-identitas.tex\`: judul, penulis, program studi, promotor, pejabat, dan tanggal.
- \`untouch/xx-preambles.tex\`: format bab, margin, caption, daftar isi, bibliografi, listing, dan TikZ.
- \`flows/\`: alur yang menggunakan komponen \`untouch/\`.
- \`a2-...\`, \`b1-...\`, \`lampiran/\`: placeholder substansi penelitian.
- \`compile.sh\`: script kompilasi dari sumber, lengkap dengan pemeriksaan dependensi dan cache, BibTeX, pengulangan kompilasi, serta opsi pembersihan.
- \`gambar/UdayanaLogo720p.png\`: logo institusi dari sumber.

## Cara menggunakan

1. Isi semua placeholder di \`a0-identitas.tex\`.
2. Pilih mode pada \`laporan.tex\`:

\`\`\`tex
\newcommand{\DocFlow}{proposal} % praproposal | proposal | disertasi
\`\`\`

3. Edit bab di \`b1-bab1.tex\` sampai \`b5-bab5.tex\` sesuai desain penelitian. \`b6-bab6.tex\` merupakan tutorial opsional.
4. Cantumkan pustaka terverifikasi di \`../../references/a7-pustaka.bib\`.
5. Dari root repository, jalankan:

\`\`\`bash
cd manuscript/latex
bash compile.sh --skip-deps
\`\`\`

Gunakan \`bash compile.sh --help\` untuk opsi lengkap. \`--skip-deps\` hanya melewati pemeriksaan dependensi, bukan menginstal paket. Gunakan tanpa opsi itu agar script memeriksa paket.

## Penyesuaian kompilasi

Sistem kompilasi tetap mengikuti script asli. Satu perbaikan kompatibilitas di \`untouch/xx-preambles.tex\` menyediakan font Times cadangan ketika paket \`newtx\` tidak terpasang.

Logo Universitas Udayana dipertahankan. File PDF hasil kompilasi, diagram penelitian lama, kuesioner riset, dan berkas personal tidak disalin karena template ini berada di repository publik.
