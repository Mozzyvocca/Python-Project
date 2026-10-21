<<<<<<< HEAD
n = int(input("Masukin tinggi segitiga: "))
simbol = input("Simbol: ")

for i in range(1, n + 1):
    print(" " * (n - i) + simbol * (2 * i - 1))
=======

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol!"
    return a / b


def main():
    while True:
        print("\n=== KALKULATOR PYTHON ===")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Keluar")

        choice = input("Pilih menu (1-5): ")

        if choice == "5":
            print("Terima kasih! Sampai jumpa.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid!")
            continue

        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input salah! Masukkan angka yang valid.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print(f"Hasil: {result}")


if __name__ == "__main__":
    main()

>>>>>>> d9948cb5b1e000b3d75f0fd9c910c4926f3109fc
