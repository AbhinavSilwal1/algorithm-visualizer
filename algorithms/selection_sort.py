def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

            yield arr, i, j, min_index, i, False

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield arr, i, min_index, min_index, i + 1, True
        else:
            yield arr, i, i, min_index, i + 1, False

    yield arr, None, None, None, None, False