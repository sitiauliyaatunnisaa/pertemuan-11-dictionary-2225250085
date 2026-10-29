def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM menggunakan get() agar aman dari KeyError."""
    return data.get(nim, "Data tidak ditemukan")

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa dalam dictionary."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== 1. PENCARIAN DATA MAHASISWA ===")
print(f"Pencarian A003: {cari_mahasiswa(data_mahasiswa, 'A003')}")
print(f"Pencarian A999: {cari_mahasiswa(data_mahasiswa, 'A999')}")

print("\n=== 2. PENAMBAHAN MAHASISWA BARU (A006) ===")
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 80}
print("Mahasiswa A006 berhasil ditambahkan.")

print("\n=== 3. PEMBARUAN NILAI MAHASISWA (A002) ===")
if "A002" in data_mahasiswa:
    data_mahasiswa["A002"]["nilai"] = 82
    print("Nilai mahasiswa A002 berhasil diperbarui menjadi 82.")

print("\n=== 4. REKAP SELURUH DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

print("\n=== 5. RATA-RATA NILAI KELAS ===")
print(f"Rata-rata nilai seluruh mahasiswa = {rata_rata_nilai(data_mahasiswa):.2f}")