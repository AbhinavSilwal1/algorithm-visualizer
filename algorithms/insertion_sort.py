def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]

            yield arr, i, j, key, False

            j -= 1

        arr[j + 1] = key

        yield arr, i, j + 1, key, True

    yield arr, None, None, None, False