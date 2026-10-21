#output: range (0, 10)
print(range (10))

#output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(10)))

#output: (2, 3, 4, 5, 6, 7)
print(list(range(2, 8)))

#output: (2, 5, 8, 11, 14, 17)
print(list(range(2, 20, 3)))

#program untuk literasi list menggunakan pengindeksan
mapel = ('matematika', 'fisika', 'kimia')

#literasi list menggunakan indeks
for i in range(len(mapel)):
    print('Saya suka', mapel(i))

#looping
count = 0
while (count < 5):
    print('The count is: ', count)
    count = count + 1
print('Good bye!')

#contoh penggunaan statement break looping
for letter in 'Python Programming':
    if letter == 'g':
        break
    print('Huruf sekarang: ', letter)
print('Good bye')

#while else
count = 0
while(count < 8):
    print(count, 'kurang dari 8')
    count = count + 1
else:
    print(count, 'tidak kurang dari 8')