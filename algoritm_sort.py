def SortPart(arr):
    for second_level in range(1, len(arr)):
        first_level = second_level - 1
        intermedia_el = arr[second_level]
        while first_level >= 0 and arr[first_level] > intermedia_el:
            arr[first_level + 1] = arr[first_level]
            first_level -= 1
        arr[first_level + 1] = intermedia_el
    return arr


arr = [4, 6, 1, 2, 3]

print(SortPart(arr))

def SortTim(arr):
    for second_level in range (len(arr) - 1):
        for first_level in range(second_level+1, len(arr)):
            if arr[second_level] > arr[first_level]:
                arr[second_level], arr[first_level] = arr[first_level], arr[second_level]
    return arr

a = [4, 6, 1, 2, 3]
print(SortTim(a))