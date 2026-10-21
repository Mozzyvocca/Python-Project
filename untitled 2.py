n = int(input("Masukin tinggi segitiga: "))
simbol = input("Simbol: ")

for i in range(1, n + 1):
    print(" " * (n - i) + simbol * (2 * i - 1))