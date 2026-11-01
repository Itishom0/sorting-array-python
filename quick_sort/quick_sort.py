def quick_sort(arr):
    # Jika array kosong atau cuma 1 elemen, sudah terurut
    if len(arr) <= 1:
        return arr

    # Pilih elemen tengah sebagai pivot
    pivot = arr[len(arr) // 2]

    # Pisahkan menjadi 3 kelompok:
    kiri = [x for x in arr if x < pivot]    # Yang lebih kecil dari pivot
    tengah = [x for x in arr if x == pivot]  # Yang sama dengan pivot
    kanan = [x for x in arr if x > pivot]    # Yang lebih besar dari pivot

    # Urutkan kiri dan kanan, lalu gabungkan
    return quick_sort(kiri) + tengah + quick_sort(kanan)


# Contoh penggunaan
angka = [40, 35, 82, 80, 8, 13, 59]

print("Sebelum diurutkan:", angka)
print("Sesudah diurutkan:", quick_sort(angka))