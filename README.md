```markdown
# Pertemuan 11 - Dictionary/Map

Nama: Siti Auliya Atunnisaa
NIM: 2225250085
Kelas: 3A

## Tujuan 
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value di Python.

## Struktur Data 
- **Key Utama:** NIM Mahasiswa (contoh: `"A001"`, `"A002"`, dst.) yang bersifat unik dan bertipe string.
- **Value:** Berupa *nested dictionary* (dictionary bersarang) yang menyimpan atribut informasi mahasiswa meliputi `"nama"`, `"kelas"`, dan `"nilai"`.

## Cara Menjalankan 
Jalankan file praktik melalui terminal VS Code dengan perintah berikut:
```bash
python3 praktik/data_mahasiswa.py

```

## Test Case

| Kasus Pengujian | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- | --- |
| Pencarian tersedia | `A003` | Data Citra ditampilkan | Data Citra tampil | Lolos |
| Pencarian tidak tersedia | `A999` | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' | Lolos |
| Pembaruan nilai | `A002` diubah ke 82 | Nilai A002 menjadi 82 | Nilai A002 menjadi 82 | Lolos |
| Penambahan data | Tambah `A006` | Key A006 tersedia | Key A006 tersedia | Lolos |
| Rekap | Menggunakan `items()` | Semua NIM dan data tampil | Tampil lengkap | Lolos |

## Refleksi

Kesalahan akses key yang sering ditemukan adalah mencoba mengakses key menggunakan kurung siku (misalnya `data['kelas']`) saat key tersebut tidak ada di dalam dictionary, sehingga memicu error `KeyError` dan menghentikan program. Hal ini diatasi dengan menggunakan method `.get()` (contoh: `data.get('kelas', 'Default')`) atau melakukan pengecekan keamanan terlebih dahulu menggunakan operator `in` sebelum mengaksesnya.

```

```