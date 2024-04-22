def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            counter += 1
            if arr[j]['index'] > arr[j + 1]['index']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, counter  # Возврат отсортированного списка и количества шагов


def selection_sort(arr):
    counter = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            counter += 1
            if arr[min_idx]['index'] > arr[j]['index']:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, counter


