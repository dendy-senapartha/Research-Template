# Research Template

Template repository penelitian generik dengan pemisahan **research governance**, protokol, evidence, artefak, manuskrip LaTeX, dan publikasi ilmiah.

Template ini **tidak** berisi data partisipan, hasil penelitian, keputusan ilmiah suatu studi, atau artikel yang sudah disubmit. Seluruh konten penelitian harus ditambahkan dan diverifikasi oleh pemilik proyek.

## Struktur utama

- `agents/research/`: instruksi Research Agent untuk validitas klaim dan tata kelola penelitian.
- `agents/writing/`: instruksi Writing Agent dan modul penulisan akademik.
- `research/governance/`: research canon, decision log, open questions, research log.
- `research/protocols/`: protokol literature review, studi, pengembangan artefak, eksperimen, dan evaluasi.
- `research/evidence/`: sumber dan bukti penelitian yang aman disimpan.
- `research/artifacts/`: luaran working, validated, dan frozen.
- `manuscript/latex/`: template naskah berformat proposal atau disertasi/laporan penelitian.
- `publications/`: register publikasi dan template artikel jurnal/prosiding.
- `references/`: bibliografi utama.
- `scripts/`: validasi dan utilitas.
- `docs/`: panduan awal, struktur, dan template ChatGPT Project Instructions.
- `archive/`: catatan lama yang bukan keputusan aktif.

## Mulai menggunakan

1. Gunakan repository ini sebagai template atau salin ke repository penelitian baru.
2. Baca `docs/getting-started.md` dan isi tata kelola penelitian terlebih dahulu.
3. Atur judul, penulis, institusi dan mode naskah di `manuscript/latex/config.tex`.
4. Tambahkan referensi terverifikasi di `references/references.bib`.
5. Untuk menghasilkan PDF, jalankan `bash manuscript/latex/compile.sh`.
6. Buat artikel baru dari `publications/_template/` dan catat di `publications/publication-register.csv`.
7. Jalankan `python3 scripts/check_structure.py` untuk pemeriksaan struktur dasar.

Panduan LaTeX tersedia di `manuscript/latex/README.md`. Panduan penggunaan sebagai ChatGPT Project ada di `docs/project-instructions-template.md`.

## Batasan

Struktur dan format adalah contoh yang dapat diadaptasi untuk bidang ilmu, jenis riset, dan ketentuan institusi. Status `validated` atau `frozen` **tidak otomatis diberikan** hanya karena sebuah file ada di folder tertentu.

Sebelum mengunggah data, periksa privasi, informed consent, izin penggunaan materi berhak cipta, dan kebijakan akses repository. Tidak ada lisensi open-source yang secara otomatis diberikan oleh template ini; pemilik repository dapat menambahkan lisensi yang sesuai.
