def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n):
    """Занурення; порівнюються лише ключі (перший елемент пари)."""
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n and arr[j + 1][0] > arr[j][0]:
            j += 1
        if arr[k][0] >= arr[j][0]:
            break
        swap(arr, k, j)
        k = j

def heapsort(arr):
    n = len(arr)
    print("Початковий масив:", arr)
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n)
    print("Після побудови купи:", arr)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        print("Обмін кореня з останнім:", arr)
        n -= 1
        sink(arr, 0, n)
        print("Після відновлення купи:  ", arr)
    return arr

# (ключ, мітка): мітка показує початковий порядок однакових ключів
data = [(3, '1'), (3, '2'), (1, '')]
print("Результат:", heapsort(data))
