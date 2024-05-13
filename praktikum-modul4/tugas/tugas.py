import math

def transformasi_gabungan(x, y, z):
    def translasi(tx, ty):
        def inner_func(a, b, c):
            return a + tx, b + ty, c

        return inner_func

    def rotasi(theta):
        def inner_func(a, b, c):
            radians = math.radians(theta)
            x_new = a * math.cos(radians) - b * math.sin(radians)
            y_new = a * math.sin(radians) + b * math.cos(radians)
            return x_new, y_new, c

        return inner_func

    def perbesaran(skala):
        def inner_func(a, b, c):
            return a * skala, b * skala, c * skala

        return inner_func

    def transform(a, b, c, *functions):
        result = (a, b, c)
        for func in functions:
            result = func(*result)
        return result

    return translasi, rotasi, perbesaran, transform

# Input dari pengguna
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))
z = float(input("Masukkan nilai z: "))

# Menerapkan transformasi berdasarkan ketentuan
translasi, rotasi, perbesaran, transform = transformasi_gabungan(x, y, z)

# Menerapkan transformasi berdasarkan ketentuan langsung
hasil_transformasi = transform(translasi(2, 3), rotasi(45), perbesaran(2))

print("Hasil Transformasi:", hasil_transformasi)
