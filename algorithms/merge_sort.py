def merge_sort(arr):
    yield from merge_sort_helper(arr, 0, len(arr) - 1)
    yield arr, None, None, None, False

def merge_sort_helper(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from merge_sort_helper(arr, left, mid)
    yield from merge_sort_helper(arr, mid + 1, right)
    yield from merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        yield arr, k, left, right, False
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        yield arr, k, left, right, False
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        yield arr, k, left, right, False
        j += 1
        k += 1