"""ЛР3, варіант 22. Сортування купою (HeapSort) з підрахунком базових операцій (Лістинг 3.1)."""

def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    arr[i], arr[j] = arr[j], arr[i]
    return 3  # Кількість присвоювань при обміні

def sink(arr, i, n):
    """Процедура занурення елемента вниз по купі."""
    comparisons = 0
    assignments = 0
    k = i
    assignments += 1  # присвоєння k
    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента
        assignments += 1  # присвоєння j
        if j >= n:
            break
        # Знаходимо індекс найбільшого дочірнього елемента
        if j + 1 < n:
            comparisons += 1
            if arr[j + 1] > arr[j]:
                j += 1
                assignments += 1  # присвоєння j
        # Перевіряємо властивість максимальної купи
        comparisons += 1
        if arr[k] >= arr[j]:
            break
        # Міняємо місцями та продовжуємо занурення
        assignments += swap(arr, k, j)
        k = j
        assignments += 1  # присвоєння k
    return comparisons, assignments

def heapsort(arr):
    """Алгоритм сортування купою."""
    n = len(arr)
    comparisons = 0
    assignments = 0
    print(f"Початковий масив: {arr}\n")
    # Фаза 1: Побудова максимальної купи
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a
    print(f"\nМасив після побудови купи: {arr}\n")
    # Фаза 2: Сортування
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        assignments += swap(arr, 0, i)
        n -= 1
        assignments += 1  # присвоєння n
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        c, a = sink(arr, 0, n)
        comparisons += c
        assignments += a
        print(f"Масив на поточному кроці: {arr}\n")
    return arr, comparisons, assignments

# Моделювання
A = [19, 75, 43, 31, 5, 66, 62, 34, 76]
sorted_A, comparisons, assignments = heapsort(A)
print(f"Відсортований масив: {sorted_A}")
print(f"Загальна кількість порівнянь: {comparisons}")
print(f"Загальна кількість присвоювань: {assignments}")
