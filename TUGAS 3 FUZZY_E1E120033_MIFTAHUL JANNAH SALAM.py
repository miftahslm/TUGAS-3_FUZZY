import numpy as np

# Inisialisasi bobot
bobot = np.zeros((3, 3))  # Inisialisasi bobot awal ke nol

# Masukkan data training dan target dari pengguna
data_target = [
    (np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]]), 1),
    (np.array([[1, -1, -1], [1, -1, -1], [1, 1, 1]]), -1),
]

# Training dengan aturan Hebb
for data, target in data_target:
    bobot += target * data

# Fungsi aktivasi Hard Limit
def hard_limit(x):
    return 1 if x >= 0 else -1

print(bobot)

# Masukkan inputan baru dari pengguna (hanya menerima nilai 1 atau -1)
inputan_baru = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        while True:
            nilai_input_baru = int(input(f"Masukkan nilai input baru ke-{i + 1},{j + 1} (hanya 1 atau -1): "))
            if nilai_input_baru in [1, -1]:
                inputan_baru[i, j] = nilai_input_baru
                break
            else:
                print("Input tidak valid. Harap masukkan nilai 1 atau -1.")

# Hitung aktivasi
aktivasi = np.dot(inputan_baru.flatten(), bobot.flatten())

# Fungsi aktivasi Hard Limit pada hasil summation
output = hard_limit(aktivasi)

# Menampilkan hasil
print("Input Baru:")
print(inputan_baru)
print("Output (Hard Limit):", output)