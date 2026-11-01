def shell_sort(numbers) :
    n = len(numbers)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            print(i, gap, n)
            temp = numbers[i]
            j = i

            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap

            numbers[j] = temp

        gap //= 2

    return numbers
    

numbers = [40,35,82,80,8,13,59]
print(f"Array sebelum diurutkan : {numbers}")
print(f"Array setelah diurutkan : {shell_sort(numbers)}")