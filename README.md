# Sistem Manajemen Data Karyawan Sederhana (CRUD) dengan Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Proyek ini adalah aplikasi console sederhana berbasis Python untuk mengelola data karyawan perusahaan. Program mendukung operasi **CRUD** (Create, Read, Update, Delete) serta fitur pencarian data berdasarkan ID karyawan.

## Fitur Utama
- **Tampilkan semua data karyawan** dalam bentuk tabel yang rapi menggunakan library `tabulate`.
- **Tambah data karyawan baru** dengan ID otomatis (K001, K002, dst.).
- **Ubah data karyawan** (nama, jabatan, gaji, atau status).
- **Hapus data karyawan** dengan konfirmasi.
- **Cari data karyawan** berdasarkan ID.
- Validasi input sederhana (nama dan jabatan hanya huruf, gaji harus angka).
- Status karyawan: Tetap, Kontrak, atau Magang.

## Requirements
Program ini hanya memerlukan satu library eksternal:
- `tabulate` – untuk menampilkan data dalam format tabel yang elegan.

## Instalasi
1. Pastikan Anda memiliki Python 3.8 atau lebih baru.
2. Clone repository ini:
   ```bash
   git clone https://github.com/username-anda/manajemen-karyawan.git
   cd manajemen-karyawan
