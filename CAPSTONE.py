from tabulate import tabulate

# ====================================
# Data awal karyawan
# ====================================
karyawan = [
    {"id_karyawan": "K001", "nama": "Muslekhan", "jabatan": "CEO", "gaji": 8500000, "status_karyawan": "Tetap"},
    {"id_karyawan": "K002", "nama": "Ulyatun Najah", "jabatan": "Finance", "gaji": 8000000, "status_karyawan": "Tetap"},
    {"id_karyawan": "K003", "nama": "Arina Zaenan", "jabatan": "HRD", "gaji": 5200000, "status_karyawan": "Kontrak"},
    {"id_karyawan": "K004", "nama": "Kuni Alfi", "jabatan": "Staff IT", "gaji": 6500000, "status_karyawan": "Kontrak"},
    {"id_karyawan": "K005", "nama": "Dian Septia", "jabatan": "Marketing", "gaji": 4800000, "status_karyawan": "Magang"}
]

# ====================================
# Fungsi bantu
# ====================================
def generate_id():
    if not karyawan:
        return "K001"
    
    last_id = karyawan[-1]["id_karyawan"]
    next_num = int(last_id[1:]) + 1
    return f"K{next_num:03d}"

def validasi_huruf(teks):
    return teks.replace(" ", "").isalpha()

# ====================================
# READ - Tampilkan Data (versi elegan tanpa format Rp)
# ====================================
def tampilkan_data():
    print("\n=== Data Karyawan ===")
    
    if not karyawan:
        print("Belum ada data karyawan.\n")
        return

    tabel = []
    for data in karyawan:
        id_karyawan = data["id_karyawan"]
        nama = data["nama"]
        jabatan = data["jabatan"]
        gaji = data["gaji"]  
        status = data["status_karyawan"]
        tabel.append([id_karyawan, nama, jabatan, gaji, status])

    print(tabulate(
        tabel,
        headers=["ID Karyawan", "Nama", "Jabatan", "Gaji", "Status"],
        tablefmt="fancy_grid"
    ))
    print()

# ====================================
# CREATE - Tambah Data
# ====================================
def tambah_data():
    print("\n=== Tambah Data Karyawan ===")
    nama = input("Masukkan nama karyawan: ").strip()
    if not validasi_huruf(nama):
        print("❌ Nama hanya boleh huruf!")
        return

    jabatan = input("Masukkan jabatan karyawan: ").strip()
    if not validasi_huruf(jabatan):
        print("❌ Jabatan hanya boleh huruf!")
        return

    try:
        gaji = int(input("Masukkan gaji karyawan: "))
    except ValueError:
        print("❌ Gaji harus berupa angka!")
        return

    print("Pilih status karyawan:")
    print("1. Tetap\n2. Kontrak\n3. Magang")

    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == "1":
        status = "Tetap"
    elif pilihan == "2":
        status = "Kontrak"
    elif pilihan == "3":
        status = "Magang"
    else:
        print("❌ Pilihan status tidak valid!")
        return 


    data_baru = {
        "id_karyawan": generate_id(),
        "nama": nama,
        "jabatan": jabatan,
        "gaji": gaji,
        "status_karyawan": status
    }

    karyawan.append(data_baru)
    print(f"✅ Data karyawan '{nama}' berhasil ditambahkan!")



# ====================================
# UPDATE - Ubah Data
# ====================================
def ubah_data():
    print("\n=== Ubah Data Karyawan ===")
    id_cari = input("Masukkan ID karyawan yang ingin diubah: ").upper()

    for k in karyawan:
        if k["id_karyawan"] == id_cari:
            print("\nData ditemukan:")
            print(tabulate([[k["id_karyawan"], k["nama"], k["jabatan"], k["gaji"], k["status_karyawan"]]],
                           headers=["ID", "Nama", "Jabatan", "Gaji", "Status"], tablefmt="fancy_grid"))

            print("\nPilih data yang ingin diubah:")
            print("1. Nama\n2. Jabatan\n3. Gaji\n4. Status")
            pilihan = input("Masukkan pilihan (1-4): ")

            if pilihan == "1":
                nama_baru = input("Masukkan nama baru: ")
                if validasi_huruf(nama_baru):
                    k["nama"] = nama_baru
                else:
                    print("❌ Nama hanya boleh huruf!")
                    return

            elif pilihan == "2":
                jabatan_baru = input("Masukkan jabatan baru: ")
                if validasi_huruf(jabatan_baru):
                    k["jabatan"] = jabatan_baru
                else:
                    print("❌ Jabatan hanya boleh huruf!")
                    return

            elif pilihan == "3":
                try:
                    k["gaji"] = int(input("Masukkan gaji baru: "))
                except ValueError:
                    print("❌ Gaji harus berupa angka!")
                    return

            elif pilihan == "4":
                print("Pilih status karyawan:")
                print("1. Tetap\n2. Kontrak\n3. Magang")
                status_pilih = input("Masukkan pilihan (1-3): ")
                if status_pilih == "1":
                    status = "Tetap"
                elif status_pilih == "2":
                    status = "Kontrak"
                elif status_pilih == "3":
                    status = "Magang"
                else:
                    print("❌ Pilihan status tidak valid!")
                    return

            else:
                print("❌ Pilihan tidak valid!")
                return

            print("✅ Data berhasil diperbarui!")
            return

    print("❌ Data tidak ditemukan.")

# ====================================
# DELETE - Hapus Data
# ====================================
def hapus_data():
    print("\n=== Hapus Data Karyawan ===")
    id_cari = input("Masukkan ID karyawan yang ingin dihapus: ").upper()

    for i, k in enumerate(karyawan):
        if k["id_karyawan"] == id_cari:
            konfirmasi = input(f"Yakin ingin menghapus data {k['nama']}? (y/n): ").lower()
            if konfirmasi == "y":
                del karyawan[i]
                print("✅ Data berhasil dihapus.")
            else:
                print("❌ Penghapusan dibatalkan.")
            return
    print("❌ Data tidak ditemukan.")

# ====================================
# SEARCH - Cari Data
# ====================================
def cari_data():
    print("\n=== Cari Data Karyawan ===")
    id_cari = input("Masukkan ID karyawan: ").upper()
    for k in karyawan:
        if k["id_karyawan"] == id_cari:
            print(tabulate([[k["id_karyawan"], k["nama"], k["jabatan"], k["gaji"], k["status_karyawan"]]],
                           headers=["ID", "Nama", "Jabatan", "Gaji", "Status"], tablefmt="fancy_grid"))
            return
    print("❌ Data tidak ditemukan.")

# ====================================
# MENU UTAMA
# ====================================
def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan data karyawan")
        print("2. Tambahkan data karyawan")
        print("3. Ubah data karyawan")
        print("4. Hapus data karyawan")
        print("5. Cari data karyawan")
        print("6. Exit")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            cari_data()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi!")

# ====================================
# Jalankan program
# ====================================
menu_utama()
