def merge_sort(array):
    if len(array) <= 1:
        return array

    tengah = len(array) // 2
    kiri = merge_sort(array[:tengah])
    kanan = merge_sort(array[tengah:])

    return merge(kiri, kanan)


def merge(kiri, kanan):
    hasil = []
    i = j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil


numbers = [40, 35, 82, 80, 8, 13, 59]
print("Array sebelum diurutkan:", numbers)
print("Array setelah diurutkan:", merge_sort(numbers))
