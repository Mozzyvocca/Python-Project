print("=" * 50)
print("           GEROBAK FRIED CHICKEN")
print("=" * 50)

print("Kode   Jenis Potong   Harga")
print("-" * 35)
print("D      Dada           Rp 2500")
print("P      Paha           Rp 2000")
print("S      Sayap          Rp 1500")
print("-" * 35)

# Daftar harga ayam
harga_ayam = {
    "D": ("Dada", 2500),
    "P": ("Paha", 2000),
    "S": ("Sayap", 1500)
}

# Input jumlah jenis ayam
while True:
    try:
        banyak_jenis = int(input("\nBanyak Jenis: "))
        if banyak_jenis > 0:
            break
        print("Banyak jenis harus lebih dari 0!")
    except ValueError:
        print("Masukkan angka yang benar!")

# Menyimpan data pembelian
data_pembelian = []
jumlah_bayar = 0

for i in range(banyak_jenis):
    print(f"\nJenis Ke - {i + 1}")

    # Input kode potong
    while True:
        kode = input("Kode Potong [D/P/S]: ").upper()

        if kode in harga_ayam:
            break
        print("Kode salah! Masukkan D, P, atau S.")

    # Input banyak potong
    while True:
        try:
            banyak_potong = int(input("Banyak Potong: "))
            if banyak_potong > 0:
                break
            print("Banyak potong harus lebih dari 0!")
        except ValueError:
            print("Masukkan angka yang benar!")

    jenis, harga_satuan = harga_ayam[kode]
    jumlah_harga = harga_satuan * banyak_potong
    jumlah_bayar += jumlah_harga

    data_pembelian.append(
        (jenis, harga_satuan, banyak_potong, jumlah_harga)
    )

# Perhitungan pajak
pajak = jumlah_bayar * 10 / 100
total_bayar = jumlah_bayar + pajak

# Tampilan keluaran
print("\n" + "=" * 65)
print("                 GEROBAK FRIED CHICKEN")
print("=" * 65)
print(f"{'No':<4}{'Jenis':<12}{'Harga':>10}"
      f"{'Banyak':>10}{'Jumlah':>15}")
print(f"{'':<4}{'Potong':<12}{'Satuan':>10}"
      f"{'Beli':>10}{'Harga':>15}")
print("-" * 65)

for i, data in enumerate(data_pembelian, start=1):
    jenis, harga_satuan, banyak_potong, jumlah_harga = data

    print(f"{i:<4}{jenis:<12}"
          f"Rp {harga_satuan:>7,}"
          f"{banyak_potong:>10}"
          f"Rp {jumlah_harga:>12,}")

print("-" * 65)
print(f"{'Jumlah Bayar':<40}Rp {jumlah_bayar:>12,}")
print(f"{'Pajak 10%':<40}Rp {pajak:>12,.0f}")
print(f"{'Total Bayar':<40}Rp {total_bayar:>12,.0f}")
print("=" * 65)
print("Terima kasih telah berbelanja!")