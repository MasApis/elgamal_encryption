import random

def gcd(a, b):
    """Mencari FPB untuk syarat k."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Mencari invers modular (Extended Euclidean Algorithm) - Kilat!"""
    m0, y, x = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    return x + m0 if x < 0 else x

def generate_k(p):
    """Generate k acak yang relatif prima dengan p-1."""
    while True:
        k = random.randint(2, p - 2)
        if gcd(k, p - 1) == 1:
            return k

# ==========================================
# PROSES UTAMA
# ==========================================

# Kita pakai p yang besar supaya muat nomor HP atau pesan angka panjang
p = 18446744073709551557 
g = 13

print("=== PROGRAM ENKRIPSI ELGAMAL (BRO-VERSION) ===")
print("1. Kirim Pesan Angka")
print("2. Kirim Pesan Teks")
pilihan = input("Pilih menu (1/2): ")

# Setup Kunci (Generate Private & Public Key)
x = random.randint(2, p - 2) # Private Key
y = pow(g, x, p)            # Public Key

print(f"\n[INFO] Kunci Publik Lu: (p={p}, g={g}, y={y})")
print(f"[INFO] Kunci Privat Lu (Rahasia!): x={x}")

if pilihan == "1":
    # --- MODE ANGKA ---
    m = int(input("\nMasukkan pesan angka: "))
    if m >= p:
        print(f"Waduh! Angka kegedean, maksimal {p-1}")
    else:
        k = generate_k(p)
        c1 = pow(g, k, p)
        s = pow(y, k, p)
        c2 = (m * s) % p
        
        print("\n--- HASIL ENKRIPSI (CIPHERTEXT) ---")
        print(f"c1: {c1}")
        print(f"c2: {c2}")

        # Dekripsi
        s_dec = pow(c1, x, p)
        s_inv = mod_inverse(s_dec, p)
        m_dec = (c2 * s_inv) % p
        print("\n--- HASIL DEKRIPSI ---")
        print(f"Pesan Asli: {m_dec}")

elif pilihan == "2":
    # --- MODE TEKS ---
    pesan_teks = input("\nMasukkan pesan teks: ")
    ciphertexts = []

    # Enkripsi per karakter
    for char in pesan_teks:
        m_char = ord(char)
        k = generate_k(p)
        c1 = pow(g, k, p)
        s = pow(y, k, p)
        c2 = (m_char * s) % p
        ciphertexts.append((c1, c2))

    print("\n--- HASIL ENKRIPSI (TEKS) ---")
    print(f"Jumlah Blok: {len(ciphertexts)}")
    for i in range(len(ciphertexts)):
        print(f"Blok {i+1} (c1, c2) {ciphertexts[i]}")

    # Dekripsi
    teks_pulih = ""
    for c1, c2 in ciphertexts:
        s_dec = pow(c1, x, p)
        s_inv = mod_inverse(s_dec, p)
        m_dec = (c2 * s_inv) % p
        teks_pulih += chr(m_dec)

    print("\n--- HASIL DEKRIPSI ---")
    print(f"Pesan Asli: {teks_pulih}")

else:
    print("Pilihan kagak ada, Bro!")

print("\n=== PROGRAM SELESAI ===")