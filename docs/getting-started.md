# Panduan Memulai Penelitian Baru

## 1. Buat repository proyek

Salin template ke repository penelitian baru. Atur visibility sesuai sensitivitas data. Jika repository ini dipakai sebagai GitHub Template, pengaturan **Template repository** perlu diaktifkan secara manual di GitHub Settings.

## 2. Tentukan tata kelola

1. Isi `research/governance/research-canon.md` dengan scope, RQ, serta keputusan yang memang sudah disepakati.
2. Setiap keputusan baru ditulis di `decision-log.csv`.
3. Pertanyaan yang belum terjawab masuk ke `open-questions.csv`.
4. Catat progres nyata pada `research-log.md`.
5. Simpan bibliografi terverifikasi ke `references/references.bib`.

Jangan menyatakan sebuah keputusan **fixed** hanya karena template menyediakan bagian untuk itu.

## 3. Susun protokol dan bukti

Duplikasi `research/protocols/protocol-template.md` sesuai jenis kegiatan. Tambahkan data yang aman dibagikan pada `research/evidence/`. Simpan data identitas, formulir persetujuan, serta data mentah sensitif pada penyimpanan privat yang diatur oleh institusi dan izin partisipan.

Gunakan `research/artifacts/working/` untuk draft, `validated/` hanya untuk output yang lolos pemeriksaan, dan `frozen/` untuk versi yang dikunci dengan bukti provenance.

## 4. Sesuaikan manuskrip

Edit `manuscript/latex/config.tex` untuk judul, identitas, institusi, dan mode. Pilih `proposal` atau `dissertation`. Isi bab di `manuscript/latex/chapters/`, dan jalankan:

    bash manuscript/latex/compile.sh

Dibutuhkan instalasi TeX Live atau MiKTeX dengan pdflatex, bibtex, dan paket di `preamble.tex`. Sesuaikan format dengan pedoman kampus, karena ini bukan template resmi sebuah institusi.

## 5. Buat publikasi

Salin `publications/_template/` ke `publications/PUB-001/` dan seterusnya. Isi metadata, lalu tambahkan entri yang benar pada `publications/publication-register.csv`. Hubungkan evidence dengan ID artefak dan commit sumber, bukan menduplikasi hasil yang tidak terlacak.

## 6. Pemeriksaan

    python3 scripts/check_structure.py
    bash -n manuscript/latex/compile.sh
    bash -n publications/_template/manuscript/compile.sh

Pemeriksaan tersebut tidak menggantikan validasi ilmiah dan uji kompilasi PDF.

## 7. Hubungkan ChatGPT Project

Salin dan sesuaikan `docs/project-instructions-template.md`. Isi repository, branch aktif, dan aturan spesifik proyek. Gunakan GitHub connector untuk membaca isi branch aktual, bukan mengandalkan file yang mungkin sudah kedaluwarsa.
