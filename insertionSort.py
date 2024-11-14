def insertionSort(arr):
    for j in range(1, len(arr)):
        actual = arr[j]
        i = j - 1

        while i >= 0 and arr[i].numero_documento > actual.numero_documento:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = actual
    return arr
