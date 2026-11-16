# Template Manuskrip LaTeX

Template ini menggunakan kelas LaTeX `report`, ukuran A4, dan paket umum. Tidak mengklaim kesesuaian dengan pedoman universitas tertentu.

## Konfigurasi

1. Isi judul, penulis, institusi, dan pembimbing pada `config.tex`.
2. Pilih `\\DocumentMode` bernilai `proposal` (Bab 1-3) atau `dissertation` (Bab 1-6).
3. Tulis isi pada `chapters/`, abstrak pada `frontmatter/abstract.tex`, dan lampiran pada `appendices/`.
4. Periksa citation key dan tambahkan pustaka ke `../../references/references.bib`.
5. Jalankan `bash compile.sh` dari folder ini, atau `bash manuscript/latex/compile.sh` dari root repository.

Perintah memerlukan `pdflatex` dan `bibtex`. Keluaran PDF `laporan.pdf` tidak dilacak Git.

## Catatan

- `flows/proposal.tex` dan `flows/dissertation.tex` memisahkan susunan bab.
- Komponen format utama ada di `preamble.tex`, bukan file penelitian.
- Perubahan `\\DocumentMode` hanya mengubah alur penyusunan, bukan status penelitian.
- Adaptasikan margin, halaman persetujuan, penomoran, font, dan gaya pustaka sesuai ketentuan institusi atau penerbit.
