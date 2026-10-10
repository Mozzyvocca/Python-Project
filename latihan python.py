nilai1 = 2
nilai2 = 5

hasil = nilai1 + nilai2
print(nilai1, '+', nilai2, '=', hasil)

hasil = nilai1 - nilai2
print(nilai1, '-', nilai2, '=', hasil)

hasil = nilai1 * nilai2
print(nilai1, '*', nilai2, '=', hasil)

hasil = nilai1 / nilai2
print(nilai1, '/', nilai2, '=', hasil)

print('     Tugas Mandiri 1     ')                                                #tugas mandiri 1
print('=========================')

berat = int(input('berat_telur :'))
harga = int(input('harga_telur :'))
transport = int(input('ongkos :'))
uang = int(input('uang :'))

print('=========================')
harga_telur = berat * harga
ongkos = transport * 2
total = harga_telur + transport
uang = uang - total

print('harga_telur =', harga_telur)
print('ongkos =', ongkos)
print('total =', total)
print('uang =', uang)

print('     Tugas Mandiri 2     ')                                                 #tugas mandiri 2
print('=========================')

harga = int(input('harga per kg :'))
berat = int(input('berat pembelian :'))

total = harga * berat
print(harga, '*', berat, '=', total)

print('         TOKO MAINAN         ')                                                    #latihan
print('*****************************')

Masukan_Nama_Pembeli = input('Masukan Nama Pembeli :')
Masukan_Kode_Mainan = input('Masukan Kode Mainan :')
Masukan_Harga = int(input('Masukan Harga :'))
Masukan_Jumlah_Beli = int(input('Masukan Jumlah Beli :'))

total = Masukan_Harga * Masukan_Jumlah_Beli

print('================================================')
print('nama pembeli =', Masukan_Nama_Pembeli)
print('kode mainan =', Masukan_Kode_Mainan)
print('harga =', Masukan_Harga)
print('jumlah beli =', Masukan_Jumlah_Beli)
print('total =', total)

print('       TOKO BUAH     ')                                                          #project iseng
print('=====================')

berat = int(input('berat per kg : '))
harga = int(input('harga : '))

total = harga * berat
print('berat buah   = ', berat)
print('harga buah   = ', harga)
print('total        = ', total)