print('=== KASIR SEDERHANA ===')

print('1. Nasi Goreng: Rp 18.000')
print('2. Ayam Geprek: Rp 15.000')
print('3. Mie Ayam: Rp. 12.000')

pilihan = int(input('pilihan(1-3): '))
jumlah = int(input('jumlah: '))

if pilihan == 1:
    harga = 18000
    menu = 'Nasi Goreng'
elif pilihan == 2:
    harga = 15000
    menu = 'Ayam Geprek'
elif pilihan == 3:
    harga = 12000
    menu = 'Mie Ayam'
else:
    print('Tidak Ada')

print('=======================')
total = harga * jumlah

print('Menu: ', menu)
print('Total: ', total)