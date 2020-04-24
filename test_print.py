def SortPart(arr):
    for second_level in range(1, len(arr)):
        first_level = second_level - 1
        print(first_level)
        intermedia_el = arr[second_level]
        print(intermedia_el)
        while first_level >= 0 and arr[first_level] > intermedia_el:
            arr[first_level + 1] = arr[first_level]
            first_level -= 1
            print(first_level)
        arr[first_level + 1] = intermedia_el
    return arr
