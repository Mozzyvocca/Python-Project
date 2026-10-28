nama = input("Masukkan nama karyawan: ")
golongan = int(input("Masukkan golongan (1/2/3): "))
pendidikan = input("Masukkan pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

gaji_pokok = 300000

# Tunjangan Jabatan
if golongan == 1:
    tunjangan_jabatan = gaji_pokok * 5 / 100
elif golongan == 2:
    tunjangan_jabatan = gaji_pokok * 10 / 100
elif golongan == 3:
    tunjangan_jabatan = gaji_pokok * 15 / 100
else:
    tunjangan_jabatan = 0

# Tunjangan Pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = gaji_pokok * 2.5 / 100
elif pendidikan == "D1":
    tunjangan_pendidikan = gaji_pokok * 5 / 100
elif pendidikan == "D3":
    tunjangan_pendidikan = gaji_pokok * 20 / 100
elif pendidikan == "S1":
    tunjangan_pendidikan = gaji_pokok * 30 / 100
else:
    tunjangan_pendidikan = 0

# Honor Lembur
if jam_kerja > 8:
    jam_lembur = jam_kerja - 8
    honor_lembur = jam_lembur * 3500
else:
    jam_lembur = 0
    honor_lembur = 0

# Total gaji
total_gaji = (
    gaji_pokok
    + tunjangan_jabatan
    + tunjangan_pendidikan
    + honor_lembur
)

# Tampilan
print("\n==============================")
print(f"Karyawan yang bernama = {nama}")
print("==============================")
print(f"Gaji Pokok            = Rp {gaji_pokok:,.0f}")
print(f"Tunjangan Jabatan     = Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan  = Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur          = Rp {honor_lembur:,.0f}")
print("------------------------------")
print(f"Total Gaji            = Rp {total_gaji:,.0f}")
print("==============================")