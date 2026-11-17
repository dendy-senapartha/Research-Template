# Mulai Proyek Penelitian

1. Buat salinan repository, atur akses sesuai sensitivitas penelitian.
2. Isi \`research/governance/research-canon.md\` dan catat keputusan resmi di \`decision-log.csv\`.
3. Rancang prosedur berdasarkan \`research/protocols/protocol-template.md\`.
4. Simpan evidence berizin dan luaran yang dapat ditelusuri di \`research/\`.
5. Isi metadata pada \`manuscript/latex/a0-identitas.tex\`, termasuk placeholder penulis, judul, pembimbing, dan tanggal. Institusi default masih Universitas Udayana.
6. Atur \`\\DocFlow\` pada \`manuscript/latex/laporan.tex\` menjadi \`praproposal\`, \`proposal\`, atau \`disertasi\`.
7. Tambahkan pustaka terverifikasi ke \`references/a7-pustaka.bib\`.
8. Kompilasi dokumen:

\`\`\`bash
cd manuscript/latex
bash compile.sh --skip-deps
\`\`\`

9. Untuk publikasi jurnal/prosiding, gunakan \`publications/_template/\` dan register. Jalankan \`python3 scripts/check_structure.py\` untuk validasi dasar.

Lihat \`manuscript/latex/README.md\` untuk panduan mode naskah dan kompilasi. Data personal atau data partisipan sensitif tidak boleh diunggah ke repository publik. Penyesuaian ke pedoman resmi institusi tetap merupakan tanggung jawab proyek baru.
