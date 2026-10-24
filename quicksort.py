def quicksort(arr, low, high, cnt):
    """Швидке сортування (опорний елемент - останній у підмасиві)."""
    if low < high:
        pivot = arr[high]
        cnt[1] += 1  # присвоєння pivot
        i = low - 1
        cnt[1] += 1  # присвоєння i
        for j in range(low, high):
            cnt[0] += 1  # порівняння arr[j] з опорним елементом
            if arr[j] <= pivot:
                i += 1
                cnt[1] += 1  # присвоєння i
                arr[i], arr[j] = arr[j], arr[i]
                cnt[1] += 3  # обмін = 3 присвоювання
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        cnt[1] += 3  # обмін опорного елемента на своє місце
        quicksort(arr, low, i, cnt)
        quicksort(arr, i + 2, high, cnt)

# Моделювання
A = [19, 75, 43, 31, 5, 66, 62, 34, 76]
cnt = [0, 0]  # [порівняння, присвоювання]
quicksort(A, 0, len(A) - 1, cnt)
print(f"Відсортований масив: {A}")
print(f"Загальна кількість порівнянь: {cnt[0]}")
print(f"Загальна кількість присвоювань: {cnt[1]}")
