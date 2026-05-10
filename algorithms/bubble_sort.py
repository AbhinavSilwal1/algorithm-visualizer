def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            swapped = False

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            sorted_start_index = n - i

            yield arr, j, j + 1, sorted_start_index, swapped

    yield arr, None, None, 0, False