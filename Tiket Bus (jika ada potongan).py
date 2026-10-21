print('---------------------------------------')
print('           PENJUALAN TIKET BUS         ')
print('---------------------------------------')

print('1. Surabaya - 300.000')
print('2. Bali - 350.000')
print('3. Lampung - 500.000')

nama = str(input('Nama Pembeli: '))
no = int(input('No. Handphone: '))
kode = input('Kode Jurusan yang dipilih(SBY/BL/LMP): ').upper()
# nama_kota = input('Nama Kota Tujuan: ')

#proses
if kode == 'SBY':
    harga = 300000
    kota = 'Surabaya'
elif kode == 'BL':
    harga = 350000
    kota = 'Bali'
elif kode == 'LMP':
    harga = 500000
    kota = 'Lampung'
else:
    print('Tidak ada')

#input jumlah beli
jumlah = int(input('Jumlah Beli: '))

#proses potongan
if jumlah >= 3:
    potongan = (harga * jumlah) * 0.1
else:
    potongan = 0

#proses pembayaran
total = (harga * jumlah) - potongan

#struk
print('Potongan yang didapat: ', potongan)
print('Total Bayar: ', total)
bayar = int(input('Masukkan Uang Bayar: '))
uang_kembali = bayar - total
print('Uang Kembali: ', uang_kembali)
