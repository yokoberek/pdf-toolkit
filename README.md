# PDF Toolkit

Alat komprehensif untuk manipulasi file PDF dengan Python. Program ini menggabungkan fitur penghapusan halaman dan penggabungan PDF dalam satu file yang mudah digunakan.

## 📋 Fitur

- **Remove Pages**: Hapus halaman tertentu dari PDF
- **Append**: Tambahkan halaman PDF di akhir dokumen lain
- **Prepend**: Tambahkan halaman PDF di awal dokumen lain
- **Insert**: Sisipkan halaman PDF pada posisi tertentu
- **Merge Multiple**: Gabungkan beberapa file PDF menjadi satu
- **PDF Info**: Lihat informasi file PDF (jumlah halaman, metadata)

## 🚀 Instalasi

### 1. Install uv (Package Manager)

**Linux & macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Atau install via pip:
```bash
pip install uv
```

### 2. Clone Repository

```bash
git clone https://github.com/yokoberek/pdf-toolkit.git
cd pdf-toolkit
```

### 3. Install Dependencies dengan uv

```bash
uv init
```

Atau install dependencies secara langsung:
```bash
uv add PyPDF2
```

## 📖 Cara Penggunaan

### Syntax Umum


```bash
uv run main.py <command> [arguments]
```

---

## 🔧 Perintah-Perintah

### 1. Remove - Hapus Halaman

Hapus halaman tertentu dari PDF.

**Syntax:**
```bash
uv run main.py remove <input.pdf> <output.pdf> <pages>
```

**Contoh:**
```bash
# Hapus halaman 1, 3, dan 5
uv run main.py remove document.pdf cleaned.pdf 1,3,5

# Hapus halaman 2 saja
uv run main.py remove document.pdf cleaned.pdf 2
```

**Keterangan:**
- `input.pdf`: File PDF asli
- `output.pdf`: File PDF hasil (tanpa halaman yang dihapus)
- `pages`: Nomor halaman yang akan dihapus (dipisah koma, tanpa spasi)

---

### 2. Append - Tambah di Akhir

Tambahkan halaman PDF di akhir dokumen lain.

**Syntax:**
```bash
uv run main.py append <base.pdf> <add.pdf> <output.pdf>
```

**Contoh:**
```bash
uv run main.py append document1.pdf document2.pdf merged.pdf
```

**Keterangan:**
- `base.pdf`: File PDF dasar
- `add.pdf`: File PDF yang akan ditambahkan di akhir
- `output.pdf`: File PDF hasil gabungan

---

### 3. Prepend - Tambah di Awal

Tambahkan halaman PDF di awal dokumen lain.

**Syntax:**
```bash
uv run main.py prepend <base.pdf> <add.pdf> <output.pdf>
```

**Contoh:**
```bash
uv run main.py prepend document1.pdf cover.pdf with_cover.pdf
```

**Keterangan:**
- File `add.pdf` akan ditempatkan di awal sebelum `base.pdf`

---

### 4. Insert - Sisipkan di Posisi Tertentu

Sisipkan halaman PDF pada posisi tertentu.

**Syntax:**
```bash
uv run main.py insert <base.pdf> <add.pdf> <output.pdf> <position>
```

**Contoh:**
```bash
# Sisipkan di halaman ke-3
uv run main.py insert document.pdf insert.pdf result.pdf 3
```

**Keterangan:**
- `position`: Nomor halaman dimana file akan disisipkan (mulai dari 1)
- File `add.pdf` akan disisipkan sebelum halaman tersebut

---

### 5. Multiple - Gabungkan Banyak File

Gabungkan beberapa file PDF menjadi satu.

**Syntax:**
```bash
uv run main.py multiple <output.pdf> <file1.pdf> <file2.pdf> <file3.pdf> ...
```

**Contoh:**
```bash
uv run main.py multiple final.pdf doc1.pdf doc2.pdf doc3.pdf doc4.pdf
```

**Keterangan:**
- File akan digabungkan sesuai urutan yang diberikan
- Bisa menggabungkan 2 file atau lebih

---

### 6. Info - Lihat Informasi PDF

Tampilkan informasi tentang file PDF.

**Syntax:**
```bash
uv run main.py info <input.pdf>
```

**Contoh:**
```bash
uv run main.py info document.pdf
```

**Output:**
```
PDF Information
==================================================
Filename: document.pdf
Pages: 25

Metadata:
  /Title: My Document
  /Author: John Doe
  /CreationDate: D:20240101120000
```

---

### 7. Help - Bantuan

Tampilkan bantuan dan daftar perintah.

**Syntax:**
```bash
uv run main.py help
```

---

## 💡 Contoh Penggunaan Lengkap

### Skenario 1: Membersihkan Dokumen
```bash
# Hapus halaman kosong (halaman 5, 8, 12)
uv run main.py remove laporan.pdf laporan_bersih.pdf 5,8,12
```

### Skenario 2: Membuat Laporan Lengkap
```bash
# 1. Tambahkan cover di awal
uv run main.py prepend isi_laporan.pdf cover.pdf temp1.pdf

# 2. Tambahkan lampiran di akhir
uv run main.py append temp1.pdf lampiran.pdf temp2.pdf

# 3. Sisipkan daftar isi di posisi 2
uv run main.py insert temp2.pdf daftar_isi.pdf laporan_final.pdf 2
```

### Skenario 3: Menggabungkan Beberapa Bab
```bash
uv run main.py multiple buku_lengkap.pdf \
    cover.pdf \
    kata_pengantar.pdf \
    bab1.pdf \
    bab2.pdf \
    bab3.pdf \
    penutup.pdf
```

### Skenario 4: Workflow Kompleks
```bash
# 1. Cek info file asli
uv run main.py info dokumen_asli.pdf

# 2. Hapus halaman yang tidak perlu
uv run main.py remove dokumen_asli.pdf dokumen_edited.pdf 1,5,10

# 3. Tambahkan halaman baru
uv run main.py append dokumen_edited.pdf halaman_baru.pdf dokumen_final.pdf
```

---

## 🐍 Penggunaan sebagai Module Python

Anda juga bisa menggunakan script ini sebagai module dalam kode Python Anda:

```python
from main import PDFToolkit

# Inisialisasi toolkit
toolkit = PDFToolkit()

# Hapus halaman
toolkit.remove_pages('input.pdf', 'output.pdf', [1, 3, 5])

# Gabungkan PDF (append)
toolkit.merge_pdfs('doc1.pdf', 'doc2.pdf', 'merged.pdf', position='append')

# Sisipkan PDF
toolkit.merge_pdfs('base.pdf', 'insert.pdf', 'result.pdf', 
                   position='insert', page_number=3)

# Gabungkan banyak file
toolkit.merge_multiple(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'output.pdf')

# Lihat info PDF
info = toolkit.get_pdf_info('document.pdf')
print(f"Total halaman: {info['pages']}")
```

---

## 🎯 Tips & Trik

### 1. Penomoran Halaman
- Halaman dimulai dari **1** (bukan 0)
- Halaman 1 adalah halaman pertama dalam PDF

### 2. Format Nomor Halaman untuk Remove
```bash
# Benar ✓
python main.py remove doc.pdf out.pdf 1,3,5,7

# Salah ✗
python main.py remove doc.pdf out.pdf 1, 3, 5, 7  # Ada spasi
```

### 3. Backup File Asli
Selalu backup file PDF asli sebelum melakukan manipulasi:
```bash
cp dokumen_asli.pdf dokumen_asli_backup.pdf
```

### 4. Periksa File Output
Gunakan perintah `info` untuk memverifikasi hasil:
```bash
python main.py info output.pdf
```

### 5. Batch Processing
Untuk memproses banyak file, buat script bash:
```bash
#!/bin/bash
for file in *.pdf; do
    python main.py remove "$file" "cleaned_$file" 1
done
```

### 6. Menggunakan uv run
Untuk environment yang terisolasi, gunakan `uv run`:
```bash
uv run main.py remove document.pdf cleaned.pdf 1,3,5
```

---

## ⚠️ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'PyPDF2'"
**Solusi:**
```bash
# Dengan uv
uv add PyPDF2

# Atau dengan pip biasa
pip install PyPDF2
```

### Error: "uv: command not found"
**Solusi:**
Install uv terlebih dahulu:
```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# atau via pip
pip install uv
```

### Error: "File not found"
**Solusi:**
- Pastikan nama file dan path benar
- Gunakan path lengkap jika file ada di folder lain
```bash
uv run main.py remove /home/user/docs/file.pdf output.pdf 1
```

### Error: "Permission denied"
**Solusi:**
- Pastikan file tidak sedang dibuka di aplikasi lain
- Periksa permission file dengan `ls -l`

### Output PDF Kosong atau Error
**Kemungkinan Penyebab:**
1. PDF input terproteksi/encrypted
2. Nomor halaman melebihi total halaman
3. PDF corrupt atau rusak

### Error: "git: command not found"
**Solusi:**
Install Git terlebih dahulu:
```bash
# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# Windows
# Download dari https://git-scm.com/
```

---

## 📝 Catatan Penting

1. **Enkripsi**: Script ini tidak dapat memproses PDF yang dienkripsi/dilindungi password
2. **Ukuran File**: Untuk file PDF sangat besar (>100MB), proses mungkin memakan waktu
3. **Metadata**: Metadata dari PDF asli akan dipertahankan setelah proses
4. **Format**: Script mendukung semua jenis PDF standar (v1.3 - v1.7)

---

## 🤝 Kontribusi

Jika Anda menemukan bug atau punya saran untuk fitur baru:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📄 Lisensi

Script ini berbasis [MIT License](./LICENSE) sehingga bebas digunakan untuk keperluan pribadi maupun komersial.

---

## 👨‍💻 Developer

Dibuat untuk mempermudah manipulasi file PDF dalam workflow sehari-hari.

**Repository:** [https://github.com/yokoberek/pdf-toolkit](https://github.com/yokoberek/pdf-toolkit)

**Requirements:**
- Python 3.8+
- uv (Package Manager)
- PyPDF2

**Versi:** 1.0.0

---

## 📚 Referensi

- [uv Documentation](https://docs.astral.sh/uv/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [PDF Specification](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/PDF32000_2008.pdf)

---

## 🔄 Update Log

### Version 1.0.0 (2024)
- ✅ Fitur remove pages
- ✅ Fitur merge (append, prepend, insert)
- ✅ Fitur merge multiple files
- ✅ Fitur info PDF
- ✅ Command-line interface
- ✅ Python module support

---

**Happy PDF Processing! 📄✨**