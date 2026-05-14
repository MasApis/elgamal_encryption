# 🔐 Enkripsi ElGamal — BRO-VERSION

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/Lisensi-MIT-green)
![Status](https://img.shields.io/badge/Status-Stabil-brightgreen)
![Kriptografi](https://img.shields.io/badge/Algoritma-ElGamal-orange)

Program enkripsi dan dekripsi berbasis algoritma **ElGamal** yang ditulis dalam Python. Mendukung dua mode: enkripsi **pesan angka** dan enkripsi **pesan teks** (per karakter). Cocok sebagai bahan belajar kriptografi kunci publik.

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Penjelasan Rumus ElGamal](#-penjelasan-rumus-elgamal)
- [Cara Kerja Program](#-cara-kerja-program)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Cara Penggunaan](#-cara-penggunaan)
  - [Windows](#windows)
  - [Linux (Ubuntu / Fedora)](#linux-ubuntu--fedora)
  - [macOS](#macos)
- [Contoh Output](#-contoh-output)
- [Struktur Kode](#-struktur-kode)
- [Kekurangan Proyek](#-kekurangan-proyek)
- [Rencana Pengembangan](#-rencana-pengembangan)
- [Lisensi](#-lisensi)

---

## 📖 Tentang Proyek

ElGamal adalah sistem kriptografi **kunci publik** yang dirancang oleh Taher Elgamal pada tahun 1985. Keamanannya didasarkan pada sulitnya memecahkan **Discrete Logarithm Problem (DLP)** — sebuah problem matematika yang hingga kini belum ada solusi efisiennya untuk bilangan prima yang cukup besar.

Program ini mengimplementasikan ElGamal dari nol menggunakan Python murni tanpa library kriptografi eksternal, sehingga ideal untuk keperluan **edukasi dan pembelajaran**.

---

## 📐 Penjelasan Rumus ElGamal

### Parameter Sistem

| Simbol | Keterangan |
|--------|-----------|
| `p`    | Bilangan prima besar (modulus) |
| `g`    | Generator / akar primitif dari grup ℤₚ* |
| `x`    | **Kunci privat** — bilangan acak rahasia, `2 ≤ x ≤ p-2` |
| `y`    | **Kunci publik** — dihitung dari `x` |
| `k`    | Bilangan acak sementara (ephemeral key), baru tiap enkripsi |
| `m`    | Pesan asli (plaintext) dalam bentuk angka |
| `(c1, c2)` | Ciphertext (hasil enkripsi) |

---

### 1. Pembangkitan Kunci (Key Generation)

**Kunci Privat:**
```
x  ←  random(2, p-2)
```

**Kunci Publik:**
```
y = g^x mod p
```

> Kunci publik yang disebarkan adalah tuple `(p, g, y)`.  
> Kunci privat `x` **tidak boleh diketahui siapa pun**.

---

### 2. Enkripsi (Encryption)

Sebelum mengenkripsi, pengirim membangkitkan bilangan acak `k` yang **relatif prima** dengan `p-1`, artinya:
```
gcd(k, p-1) = 1
```

Kemudian dihitung dua komponen ciphertext:

```
c1 = g^k mod p
s  = y^k mod p       ← shared secret
c2 = (m × s) mod p
```

Ciphertext yang dikirim adalah pasangan `(c1, c2)`.

---

### 3. Dekripsi (Decryption)

Penerima yang mengetahui kunci privat `x` dapat menghitung ulang *shared secret* `s`:

```
s_dec = c1^x mod p
```

Kenapa ini benar? Karena:
```
c1^x = (g^k)^x = g^(kx) mod p
y^k  = (g^x)^k = g^(xk) mod p
→ c1^x ≡ y^k (mod p)
```

Setelah mendapat `s_dec`, hitung **invers modular**-nya:
```
s_inv = s_dec^(-1) mod p   ← menggunakan Extended Euclidean Algorithm
```

Lalu pulihkan pesan asli:
```
m = (c2 × s_inv) mod p
```

---

### 4. Invers Modular (Extended Euclidean Algorithm)

Invers modular `a^(-1) mod m` adalah nilai `x` sedemikian sehingga:
```
a × x ≡ 1 (mod m)
```

Program ini menggunakan **Algoritma Euclidean Diperluas** untuk mencarinya secara efisien — tanpa algoritma ini, dekripsi tidak dapat dilakukan.

---

### 5. Syarat Keamanan Kunci `k`

```
gcd(k, p-1) = 1   →  k harus relatif prima dengan p-1
```

Jika syarat ini tidak dipenuhi, invers modular tidak dapat dihitung dan enkripsi gagal.

---

## ⚙️ Cara Kerja Program

```
┌─────────────────────────────────────────────────────┐
│                  ALUR PROGRAM                       │
│                                                     │
│  Generate Kunci  →  Pilih Mode  →  Input Pesan      │
│         ↓               ↓               ↓           │
│   (p, g, x, y)    Angka / Teks    m atau teks       │
│                                        ↓            │
│                              Enkripsi → (c1, c2)    │
│                                        ↓            │
│                              Dekripsi → m asli      │
└─────────────────────────────────────────────────────┘
```

1. Program membangkitkan kunci privat `x` dan kunci publik `y` secara acak.
2. Pengguna memilih mode: **angka** atau **teks**.
3. Pesan dienkripsi menggunakan rumus ElGamal menjadi pasangan `(c1, c2)`.
4. Ciphertext langsung didekripsi dan pesan asli ditampilkan sebagai verifikasi.

---

## 💻 Persyaratan Sistem

- **Python versi 3.6 ke atas**
- Tidak memerlukan library eksternal — hanya menggunakan modul bawaan `random`
- Berjalan di semua sistem operasi utama

---

## 🚀 Cara Penggunaan

### Windows

1. **Pastikan Python sudah terinstall**

   Buka Command Prompt dan cek versi Python:
   ```cmd
   python --version
   ```
   Jika belum terinstall, unduh dari [python.org](https://www.python.org/downloads/) dan centang opsi **"Add Python to PATH"** saat instalasi.

2. **Clone repositori ini**
   ```cmd
   git clone https://github.com/username/nama-repo.git
   cd nama-repo
   ```

3. **Jalankan program**
   ```cmd
   python elgamal.py
   ```

4. **Ikuti instruksi di layar** — pilih menu `1` untuk pesan angka atau `2` untuk pesan teks.

---

### Linux (Ubuntu / Fedora)

1. **Cek versi Python**
   ```bash
   python3 --version
   ```

2. **Install Python jika belum ada**

   **Ubuntu / Debian:**
   ```bash
   sudo apt update
   sudo apt install python3 -y
   ```

   **Fedora:**
   ```bash
   sudo dnf install python3 -y
   ```

3. **Clone repositori ini**
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd nama-repo
   ```

4. **Jalankan program**
   ```bash
   python3 elgamal.py
   ```

---

### macOS

1. **Cek versi Python**
   ```bash
   python3 --version
   ```

2. **Install Python jika belum ada**

   Menggunakan Homebrew (direkomendasikan):
   ```bash
   # Install Homebrew jika belum ada
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install Python
   brew install python
   ```

   Atau unduh langsung dari [python.org](https://www.python.org/downloads/macos/).

3. **Clone repositori ini**
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd nama-repo
   ```

4. **Jalankan program**
   ```bash
   python3 elgamal.py
   ```

---

## 📟 Contoh Output

### Mode 1 — Pesan Angka

```
=== PROGRAM ENKRIPSI ELGAMAL (BRO-VERSION) ===
1. Kirim Pesan Angka
2. Kirim Pesan Teks
Pilih menu (1/2): 1

[INFO] Kunci Publik Lu: (p=83146949379, g=2, y=47291038201)
[INFO] Kunci Privat Lu (Rahasia!): x=39182746105

Masukkan pesan angka: 12345678

--- HASIL ENKRIPSI (CIPHERTEXT) ---
c1: 29183746502
c2: 58273649102

--- HASIL DEKRIPSI ---
Pesan Asli: 12345678
```

### Mode 2 — Pesan Teks

```
=== PROGRAM ENKRIPSI ELGAMAL (BRO-VERSION) ===
Pilih menu (1/2): 2

Masukkan pesan teks: Halo

--- HASIL ENKRIPSI (TEKS) ---
Jumlah Blok: 4
Blok 1 (c1, c2) (39182746502, 72938164052)
Blok 2 (c1, c2) (18273640921, 49201837465)
...

--- HASIL DEKRIPSI ---
Pesan Asli: Halo
```

---

## 🗂️ Struktur Kode

```
elgamal.py
│
├── gcd(a, b)              → Mencari FPB dengan algoritma Euclidean
├── mod_inverse(a, m)      → Mencari invers modular (Extended Euclidean)
├── generate_k(p)          → Membangkitkan k acak yang relatif prima dengan p-1
│
└── main()
    ├── Setup kunci (x, y)
    ├── Mode 1: Enkripsi & dekripsi pesan angka
    └── Mode 2: Enkripsi & dekripsi pesan teks per karakter
```

---

## ⚠️ Kekurangan Proyek

Proyek ini dibuat untuk tujuan **edukasi**, sehingga ada beberapa keterbatasan penting yang perlu diketahui:

### 🔴 Keamanan

| Masalah | Penjelasan |
|---------|------------|
| **Nilai `p` tidak terverifikasi primanya** | Program mengasumsikan `p = 83146949379` adalah prima, namun tidak ada pengecekan otomatis. Jika `p` bukan prima, seluruh sistem kriptografi runtuh. |
| **`p` terlalu kecil** | Untuk keamanan nyata, `p` harus minimal 2048-bit. Nilai yang digunakan hanya ~37-bit, sangat mudah dipecahkan. |
| **Tidak ada padding** | ElGamal standar memerlukan skema padding (seperti OAEP) agar aman. Tanpa padding, enkripsi rentan terhadap beberapa serangan. |
| **k tidak di-hash** | Kunci sementara `k` dibangkitkan dengan `random` biasa, bukan CSPRNG (Cryptographically Secure Pseudo-Random Number Generator). |
| **Kunci tidak disimpan** | Setiap kali program dijalankan, kunci baru dibangkitkan. Tidak ada mekanisme penyimpanan kunci yang aman. |

### 🟡 Fungsionalitas

| Masalah | Penjelasan |
|---------|------------|
| **Enkripsi teks per karakter** | Mode teks mengenkripsi tiap karakter secara terpisah, bukan blok penuh. Ini membocorkan frekuensi karakter (frequency analysis attack). |
| **Tidak ada antarmuka pengguna** | Program hanya berjalan di terminal. Belum ada GUI atau antarmuka web. |
| **Tidak ada penyimpanan ciphertext** | Hasil enkripsi hanya ditampilkan di layar, tidak disimpan ke file. |
| **Tidak ada pertukaran kunci antar pengguna** | Simulasi dilakukan di satu mesin. Tidak ada mekanisme berbagi kunci publik secara nyata. |
| **Enkripsi dan dekripsi di program yang sama** | Dalam skenario nyata, enkripsi dan dekripsi dilakukan oleh dua pihak berbeda. |

### 🟢 Performa

| Masalah | Penjelasan |
|---------|------------|
| **Lambat untuk pesan panjang** | Enkripsi per karakter menghasilkan overhead besar untuk teks yang panjang. |
| **Tidak menggunakan parallelism** | Semua operasi berjalan sekuensial, tidak memanfaatkan multi-core processor. |

> **Kesimpulan:** Program ini **TIDAK aman untuk digunakan di lingkungan produksi**. Gunakan hanya sebagai media belajar konsep kriptografi ElGamal.

---

## 🔭 Rencana Pengembangan

- [ ] Validasi otomatis apakah `p` adalah bilangan prima (uji Miller-Rabin)
- [ ] Pembangkitan bilangan prima besar secara otomatis
- [ ] Enkripsi berbasis blok, bukan per karakter
- [ ] Simpan dan muat kunci dari file
- [ ] Ekspor ciphertext ke file `.txt` atau `.json`
- [ ] Antarmuka grafis (GUI) berbasis Tkinter atau web

---

## 📚 Referensi

- ElGamal, T. (1985). *A public key cryptosystem and a signature scheme based on discrete logarithms*. IEEE Transactions on Information Theory.
- [Wikipedia — ElGamal Encryption](https://en.wikipedia.org/wiki/ElGamal_encryption)
- [Khan Academy — Modular Arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography)

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License** — bebas digunakan, dimodifikasi, dan didistribusikan untuk keperluan apapun, termasuk komersial, selama menyertakan atribusi.

```
MIT License © 2025 — Abdul Hafidz, Adib Farhan Shiombing, Vito Hendriansyah
```

---

<div align="center">
  <sub>Dibuat dengan ☕ dan semangat belajar kriptografi.</sub>
</div>
