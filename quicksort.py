def partition(arr, l, h, cnt):
    """Розбиття за лекцією: PickElement - перший елемент підмасиву."""
    p = l  # p <- PickElement(A)
    cnt[1] += 1  # присвоєння p
    arr[p], arr[h] = arr[h], arr[p]  # Swap(A[p], A[h])
    cnt[1] += 3  # обмін = 3 присвоювання
    b = l  # b <- l
    cnt[1] += 1  # присвоєння b
    for i in range(l, h):  # позицію i = h займає опорний елемент
        cnt[0] += 1  # Compare(A[i], A[h])
        if arr[i] < arr[h]:
            arr[i], arr[b] = arr[b], arr[i]  # Swap(A[i], A[b])
            cnt[1] += 3  # обмін = 3 присвоювання
            b += 1  # b <- b + 1
            cnt[1] += 1  # присвоєння b
    arr[h], arr[b] = arr[b], arr[h]  # Swap(A[h], A[b])
    cnt[1] += 3  # обмін опорного елемента на своє місце
    return b

def quicksort(arr, l, h, cnt):
    """Швидке сортування за лекцією."""
    if l < h:
        p = partition(arr, l, h, cnt)  # p <- Partition(A, l, h)
        cnt[1] += 1  # присвоєння p
        quicksort(arr, l, p - 1, cnt)
        quicksort(arr, p + 1, h, cnt)

# Моделювання
A = [19, 75, 43, 31, 5, 66, 62, 34, 76]
cnt = [0, 0]  # [порівняння, присвоювання]
quicksort(A, 0, len(A) - 1, cnt)
print(f"Відсортований масив: {A}")
print(f"Загальна кількість порівнянь: {cnt[0]}")
print(f"Загальна кількість присвоювань: {cnt[1]}")
