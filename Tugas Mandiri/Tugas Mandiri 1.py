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