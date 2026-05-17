def quick_sort(arr):
    yield from quick_sort_helper(arr, 0, len(arr) - 1)
    yield arr, None, None, None, False

def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = yield from partition(arr, low, high)

        yield from quick_sort_helper(arr, low, pivot_index - 1)
        yield from quick_sort_helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        yield arr, j, high, i, False

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    yield arr, i + 1, high, i + 1, True

    return i + 1